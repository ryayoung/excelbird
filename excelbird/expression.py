import re
from typing import TypeVar

from excelbird.globals import global_ids, global_headers
from excelbird.styles import default_table_style
from excelbird.base_types import Style

from excelbird.util import (
    pass_attr_without_override,
    pass_dict_without_override,
)

TExpr = TypeVar("TExpr", bound="Expr")

class Expr:
    """
    Expression
    ----------
    Reference elements in parent container by name or index in a string
    expression. Immediately upon instantiating and Expr, all references
    enclosed in square brackets are parsed out and stored in a dictionary,
    where all values are None. The parent container of an Expr is responsible
    for resolving each of these keys by filling them with their corresponding
    element in the layout, and then evaluating.
    """

    def __init__(
        self,
        expr_str: str | set,
        id: str | None = None,

        header: str | None = None,

        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        table_style: Style | dict | bool | None = None,
        **kwargs,
    ) -> None:
        if isinstance(expr_str, set):
            expr_str = expr_str.pop()
        matches = re.findall(r"\[(.*?)\]", expr_str)
        for i, match in enumerate(matches):
            match = match.strip()
            try:
                matches[i] = int(match)
            except Exception:
                matches[i] = match.replace("'", "").replace('"', "")

        refs = {match: None for match in matches}
        expr = (
            expr_str
            # Add dub quotes around every ref name
            .replace(r"[", 'self.refs["').replace(r"]", '"]')
        )
        # Remove quotes around integers
        expr = re.sub(r'"(-?\d+)"', r"\1", expr)

        # Check to see if they're just referencing an object without doing
        # calculations on it. If so, we MIGHT want to return that element's
        # .ref() expression, instead of the element itself. Like if they just
        # list this expression as a cell or a column, we'll want to make a cell
        # reference to that element instead of copying it over. However, if
        # they are referencing an element from inside a function, we want to
        # return the referenced object itself. We'll have to let the parent
        # container determine what to do. If it's a single element reference,
        # we'll set `is_ref` to True right here. The parent container can then
        # set `use_ref` to True for any standalone expressions, not inside functions.
        use_ref = False
        is_ref = False
        if len(refs) == 1:
            if expr.startswith("self") and expr.endswith('"]'):
                is_ref = True

        if cell_style is None: cell_style = dict()
        if header_style is None: header_style = dict()
        if table_style is None: table_style = dict()
        elif table_style is True: table_style = default_table_style

        self.expr = expr
        self.expr_str = expr_str
        self.refs = refs
        self.id = id
        self.is_ref = is_ref
        self.use_ref = use_ref

        self.header = header

        self.cell_style = Style(**cell_style)
        self.header_style = Style(**header_style)
        self.table_style = Style(**table_style)
        self.kwargs = kwargs

    def refs_resolved(self) -> bool:
        return not any(i is None for i in self.refs.values())

    def eval(self):
        if self.refs_resolved() is False:
            raise ValueError("Not all refs resolved")

        res = eval(self.expr)
        if self.use_ref is True:
            res = res.ref()

        # If returning cell, set each style value as attribute on cell
        if getattr(res.__class__, "dimensions", None) == 0:
            res.inherit_style_without_override(self.cell_style)
            res.id = self.id

        # If returning _Vec, pass down attributes
        if getattr(res.__class__, "dimensions", None) >= 1:
            pass_attr_without_override(self, res, "header")
            pass_attr_without_override(self, res, "id")

            pass_dict_without_override(self, res, "cell_style")
            pass_dict_without_override(self, res, "header_style")
            pass_dict_without_override(self, res, "table_style")

            for key, val in self.kwargs.items():
                if hasattr(res, key):
                    if getattr(res, key) is None:
                        setattr(res, key, val)

        return res

    def ref(self):
        raise ValueError("Can't make a cell reference to an unresolved Expr")

    def attempt_to_resolve(self, container: list) -> bool:
        """
        Given a container, attempt to resolve all refs

        A valid reference might be:
            An integer index of an item in the container
            A string id in `global_ids`

        Returns True if a match was found for each reference

        Mutates inplace: `self`
        """
        for key, val in self.refs.items():
            try:
                ref = container[container.key_to_idx(key)]
            except (KeyError, IndexError):
                try:
                    ref = global_ids[key]
                except (KeyError, IndexError):
                    ref = global_headers.get(key, None)

            if ref is not None:
                self.refs[key] = ref
        
        return self.refs_resolved()
    
    @classmethod
    def resolve_container_recursive(cls, container: list) -> bool:
        """
        For each Expr element, try to resolve its references. If all references
        were resolved, it's replaced with its evaluated form.

        Returns True if all expressions in the container were resolved

        Mutates inplace: `container`
        """
        all_expressions_resolved = True

        for i, elem in enumerate(container):
            if isinstance(elem, cls):

                if elem.attempt_to_resolve(container) is True:
                    container[i] = elem.eval()
                else:
                    all_expressions_resolved = False

            elif isinstance(elem, list):
                if cls.resolve_container_recursive(elem) is False:
                    all_expressions_resolved = False

        return all_expressions_resolved
    
    @classmethod
    def set_use_ref_for_container_recursive(cls, container: list) -> None:
        """
        Tells all expressions in a container to use references.
        Mutates inplace: `container`
        """
        for elem in container:
            if isinstance(elem, cls):
                if elem.is_ref is True:
                    elem.use_ref = True
            elif isinstance(elem, list):
                cls.set_use_ref_for_container_recursive(elem)
    