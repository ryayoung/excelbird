from typing import Any
from excelbird.expression import Expr
from excelbird.styles import default_table_style
from excelbird.base_types import Style

from excelbird.util import (
    get_dimensions,
    convert_all_to_type,
)

class _DelayedFunc:
    """
    Returned by `fun()` when any of the references in the function are
    expressions. Once the parent container resolves all expressions,
    it can call `get_function()` which will call `fun()` again with the
    resolved arguments.
    """

    def __init__(
        self,
        res_type: type,
        name: str,
        inner: list,
        id: str | None,
        header: str | None,

        cell_style: Style | dict | None,
        header_style: Style | dict | None,
        table_style: Style | dict | bool | None,
        kwargs: dict,
    ) -> None:
        if cell_style is None: cell_style = dict()
        if header_style is None: header_style = dict()
        if table_style is None: table_style = dict()
        elif table_style is True: table_style = default_table_style

        self.res_type = res_type
        self.name = name
        self.inner = inner
        self.id = id
        self.header = header
        self.cell_style = Style(**cell_style)
        self.header_style = Style(**header_style)
        self.table_style = Style(**table_style)
        self.kwargs = kwargs

    def exprs(self) -> list:
        return [i for i in self.inner if isinstance(i, Expr)]

    def all_resolved(self) -> bool:
        if any(i.refs_resolved() is False for i in self.exprs()):
            return False
        return True

    def get_function(self):
        if not self.all_resolved():
            raise ValueError("Not all refs resolved")

        return fun(
            res_type=self.res_type,
            name=self.name,
            inner=self.inner,
            id=self.id,
            header=self.header,
            cell_style=self.cell_style,
            header_style=self.header_style,
            table_style=self.table_style,
            **self.kwargs,
        )

    def ref(self):
        raise ValueError("Can't make a cell reference to an unresolved _DelayedFunc")

    def attempt_to_resolve(self, container: list) -> bool:
        """
        Given a parent container, try to resolve each expression
        in self's `inner`

        Returns True if all expressions were resolved

        Mutates inplace: `self`
        """
        for i, elem in enumerate(self.inner):
            if isinstance(elem, Expr):
                if elem.attempt_to_resolve(container) is True:
                    self.inner[i] = elem.eval()
        
        return self.all_resolved()
    
    @classmethod
    def resolve_container_recursive(cls, container: list) -> bool:
        """
        For each _DelayedFunc in a container, attempt to resolve each of
        its expressions.

        Returns True if all were resolved

        Mutates inplace: `container`
        """
        all_dfuncs_resolved = True

        for i, elem in enumerate(container):
            if isinstance(elem, cls):

                if elem.attempt_to_resolve(container) is True:
                    container[i] = elem.get_function()
                else:
                    all_dfuncs_resolved = False

            elif isinstance(elem, list):
                if cls.resolve_container_recursive(elem) is False:
                    all_dfuncs_resolved = False

        return all_dfuncs_resolved


def fun(
    res_type: type,
    name: str,
    inner: list,
    id: str | None = None,
    header: str | None = None,

    cell_style: Style | dict | None = None,
    header_style: Style | dict | None = None,
    table_style: Style | dict | bool | None = None,
    **kwargs: Any,
) -> Any:
    """
    Create an excel function.
    `name` is the string name of the function in Excel.
    `inner` is the contents to be enclosed inside the parentheses. These can
    be Cells, Vecs, or expressions.
    `res_type` must be either `Cell`, `Row`, or `Col`. This cannot be assumed,
    from the contents of `inner`, because the same type of arguments could be
    used to return either a vector or a Cell. For instance, you might use
    "SUM(col, col)" to return a single cell, whereas you might use "CONCAT(col, col)"
    to return a vector where each cell concatenates two cells from the corresponding
    columns.

    If any of the contents of `inner` are Expr, a _DelayedFunc will be returned,
    which will need to be resolved by its parent container.
    """
    if cell_style is None: cell_style = dict()
    if header_style is None: header_style = dict()
    if table_style is None: table_style = dict()
    elif table_style is True: table_style = default_table_style

    cell_style = Style(**cell_style)
    header_style = Style(**header_style)
    table_style = Style(**table_style)

    # Checking type instead of isinstance() because _Vec subclasses list
    if type(inner) not in [list, tuple]:
        inner = [inner]
    
    # Convert sets to expressions
    convert_all_to_type(inner, set, Expr)

    if any(isinstance(i, (Expr, _DelayedFunc)) for i in inner):
        return _DelayedFunc(
            res_type=res_type,
            name=name,
            inner=inner,
            id=id,
            header=header,
            cell_style=cell_style,
            header_style=header_style,
            table_style=table_style,
            kwargs=kwargs,
        )
    
    if not hasattr(res_type, "dimensions"):
        raise TypeError("`res_type` must have `dimensions` class attribute")
    
    if res_type.dimensions == 0:
        return res_type(func=[name.upper()] + inner, id=id, **cell_style)

    if not any(hasattr(i.__class__, "dimensions") for i in inner):
        raise TypeError(
            f"To return a '{res_type.__name__}', at least one item in "
            f"`inner` needs a `dimensions` class attribute."
        )
    if not any(
        i.__class__.dimensions >= res_type.dimensions
        for i in inner if hasattr(i.__class__, "dimensions")
    ):
        raise TypeError(
            f"To return a '{res_type.__name__}', at least one item in `inner` "
            f"needs to have an equal or greater number of dimensions than "
            f"'{res_type.__name__}'. For instance, you can't sum two cells "
            f"and return a column."
        )

    kwargs["header_style"] = header_style
    kwargs["header"] = header
    kwargs["table_style"] = table_style

    # Return a vector of some kind
    # Say 'inner' is a list with integers, cells, and vectors. We want to return
    # a vector no longer than the shortest vector in 'inner'. This returned
    # vector will call fun() again for each cell, where, for each item in 'inner',
    # if it's a vector, use a single element, else just repeat the value
    # So `fun(Col, "CONCAT", [1, Col(1,2)])` returns something like:
    # Col([fun(Cell, "CONCAT", [1, Cell(1)]), fun(Cell, "CONCAT", [1, Cell(2)])])

    
    return res_type(
        *[
            fun(
                res_type=res_type.elem_type,
                name=name,
                inner=[item[i] if get_dimensions(item) == 1 else item for item in inner],
            )
            for i in range(min(len(x) for x in inner if get_dimensions(x) == 1))
        ],
        id=id,
        cell_style=cell_style,
        **kwargs,
    )
