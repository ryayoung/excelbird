import re
from typing import TypeVar

from excelbird.globals import Globals
from excelbird.styles import default_table_style
from excelbird.base_types import Style
from excelbird.math import CanDoMath

from excelbird.util import (
    pass_attr_without_override,
    pass_dict_without_override,
)

TExpr = TypeVar("TExpr", bound="Expr")

class Expr(CanDoMath):
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

        # Match group for the inner contents of a square bracket enclosure
        # that has at least one character and no brackets inside
        r_elem = r"\[([^\[\]]+?)\]"

        # Get the element at the start of the string, if one
        match_start: list = re.findall(r"^" + r_elem, expr_str)

        # For all other matches, make sure the enclosure isn't immediately
        # preceded by a bracket or parenthese. Those should
        # be left alone and treated as regular __getitem__ calls in python
        match_others: list = re.findall(r"[^\]\)\[\(]" + r_elem, expr_str)

        matches = match_start + match_others

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
        """
        Note to self: why are we passing down without override to a
        result that just got evaluated? Shouldn't the new object
        have an empty slate of attributes? Instead, just loop through
        kwargs and:
            If element has the attribute set it. Else, check if it has
            a cell_style, and set it as a key/value inside cell_style.
        """
        if self.refs_resolved() is False:
            raise ValueError("All references must be resolved before calling .eval()")

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
                elif hasattr(res, "cell_style"):
                    if key not in res.cell_style:
                        res.cell_style[key] = val

        return res

    def ref(self):
        raise ValueError("Can't make a cell reference to an unresolved Expr")

    def attempt_to_resolve(self, container: list) -> bool:
        """
        Given a container, attempt to resolve all refs

        A valid reference might be:
            An integer index of an item in the container
            A string id in `Globals.ids`

        Returns True if a match was found for each reference

        Mutates inplace: `self`
        """
        from excelbird.function import Func
        for key in self.refs.keys():
            try:
                ref = container[container.key_to_idx(key)]
            except (KeyError, IndexError):
                ref = Globals.ids.get(key, None)
                if ref is None:
                    ref = Globals.headers.get(key, None)
                if ref is None:
                    ref = Globals.global_ids.get(key, None)
                if ref is None:
                    ref = Globals.global_headers.get(key, None)

            if ref is not None and not isinstance(ref, (Func, Expr)):
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
    
    def __repr__(self):
        return f"{self.__class__.__name__}(...)"


