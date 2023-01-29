"""
Expr docstring
"""
import re
from typing import TypeVar

from excelbird._layout_references import Globals
from excelbird.styles.styles import default_table_style
from excelbird._base.dotdict import Style
from excelbird._base.math import CanDoMath

from excelbird._utils.pass_attributes import (
    pass_attr_without_override,
    pass_dict_without_override,
)

TExpr = TypeVar("TExpr", bound="Expr")

class Expr(CanDoMath):
    """
    Reference elements in parent container by name or index in a string
    expression. Immediately upon instantiating and Expr, all references
    enclosed in square brackets are parsed out and stored in a dictionary,
    where all values are None. The parent container of an Expr is responsible
    for resolving each of these keys by filling them with their corresponding
    element in the layout, and then evaluating.

    Pass a string containing the code to be executed. It should look like normal python code, but instead
    of variable names, use square brackets and enclose the ``id`` or ``header`` of another layout element
    that may or may not exist yet. Quote marks are *not* necessary inside the brackets. For instance,
    * ``Expr("[some_cell_id] / ([some_column_header] + 2)", id="new_col")``
    **Shorthand Syntax**: If you don't need to pass any keyword arguments, ``Expr`` can be more concisely
    written as a single-element ``set``, containing the expression string:
    * ``{"[some_cell_id] / ([some_column_header] + 2)"}``
    This is useful when building a ``Func``, where you might list many ``Expr`` together in succession.

    Parameters
    ----------
    expr_str : str
        The contents of the expression to be executed. It should look like normal python code, but instead
        of variables, use square brackets and enclose an ``id`` or ``header`` of another layout element.
        Example: ``"[some_cell_id] / ([some_column_header] + 2)"``
    id : str, default None
        Id of the resulting element once the Expr is evaluated
    header : str, default None
        Header of the resulting element once the Expr is evaluated. This will only have an effect if the
        resulting element can take a header
    cell_style : dict, default None
        To be applied to the resulting element
    header_style : dict, default None
        To be applied to the resulting element
    table_style : dict, default None
        To be applied to the resulting element
    **kwargs :
        Any other keyword arguments will be set as attributes on the resulting element

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
        # that has at least one character and no brackets inside, and is NOT
        # not ONLY digits
        # r_elem = r"\[((?:[^\[\]]|\d+)+?)\]"
        r_elem = r"\[([^\[\]]+?)\]"
        # r_elem = r"\[([^\[\]\d]+?)\]"
        # r_elem = r"\[([^\[\]](?:[a-zA-Z\d]+)+?)\]"

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

        # expr = re.sub(r"[^\[]\[", 'self.refs["', expr_str)
        # expr = re.sub(r"[^\d]\]", '"]', expr)
        # expr = re.sub(r'"(-?\d+)"', r"\1", expr)

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
        if table_style is None or table_style is False: table_style = dict()
        elif table_style is True: table_style = default_table_style

        self.refs = refs
        self._is_ref = is_ref
        self._use_ref = use_ref

        self.expr = expr
        self.expr_str = expr_str
        self.id = id

        self.header = header

        self.cell_style = Style(**cell_style)
        self.header_style = Style(**header_style)
        self.table_style = Style(**table_style)
        self.kwargs = kwargs

    def _refs_resolved(self) -> bool:
        """
        Whether all references are resolved
        """
        return not any(i is None for i in self.refs.values())

    def _eval(self):
        """
        Call once all references are resolved.
        - Calls python's ``eval()`` on ``self.expr``
        - Applies stored attributes to the result object
        - Returns result object
        """

        if self._refs_resolved() is False:
            raise ValueError("All references must be resolved before calling .eval()")

        res = eval(self.expr)

        if self._use_ref is True:
            res = res.ref()

        # If returning cell, set each style value as attribute on cell
        if getattr(type(res), "_dimensions", None) == 0:
            res._inherit_style_without_override(self.cell_style)
            res.id = self.id

        # If returning _Series, pass down attributes
        if getattr(type(res), "_dimensions", None) >= 1:
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

    def _attempt_to_resolve(self, container: list) -> bool:
        """
        Given a container, attempt to resolve all refs

        A valid reference might be:
            An integer index of an item in the container
            A string id in `Globals.ids`

        Returns True if a match was found for each reference

        Mutates inplace: `self`
        """
        from excelbird.core.function import Func
        for key in self.refs.keys():
            try:
                ref = container[container._key_to_idx(key)]
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
        
        return self._refs_resolved()
    
    @classmethod
    def _resolve_container_recursive(cls, container: list) -> bool:
        """
        For each Expr element, try to resolve its references. If all references
        were resolved, it's replaced with its evaluated form.

        Returns True if all expressions in the container were resolved

        Mutates inplace: `container`
        """
        all_expressions_resolved = True

        for i, elem in enumerate(container):
            if isinstance(elem, cls):

                if elem._attempt_to_resolve(container) is True:
                    container[i] = elem._eval()
                else:
                    all_expressions_resolved = False

            elif isinstance(elem, list):
                if cls._resolve_container_recursive(elem) is False:
                    all_expressions_resolved = False

        return all_expressions_resolved
    
    @classmethod
    def _set_use_ref_for_container_recursive(cls, container: list) -> None:
        """
        Tells all expressions in a container to use references.
        Mutates inplace: `container`
        """
        for elem in container:
            if isinstance(elem, cls):
                if elem._is_ref is True:
                    elem._use_ref = True
            elif isinstance(elem, list):
                cls._set_use_ref_for_container_recursive(elem)
    
    def __repr__(self):
        return f"{type(self).__name__}(...)"


