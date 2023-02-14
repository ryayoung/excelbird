"""
.. _header:

Headers
------------------------

A Series' :attr:`header <excelbird._Series.header>` attribute is a string which will
*later* be inserted as a :class:`Cell <excelbird.Cell>`. It has several purposes:

* Ignored by formulas and cell references, and is instead treated as a stylistic attribute
  of the parent container.
* Declared manually, or automatically if a :class:`pd.Series <pandas.Series>` is given
* Its styling is independent of the other child cells, and must be styled separately with :attr:`header_style <excelbird._Series.header_style>`.
* It can be referenced globally by other :class:`Exprs <excelbird.Expr>` in the layout, just like an ``id``. This is to avoid
  redundancy, and also provide convenience when headers are set automatically from :mod:`pandas` objects.

"""
# External
from __future__ import annotations
from pandas import Series
from numpy import ndarray
from typing import Iterable, Any, overload
from copy import copy, deepcopy

from excelbird._base.container import ListIndexableById
from excelbird._base.identifier import HasId
from excelbird._base.identifier import HasHeader
from excelbird._base.styling import HasBorder
from excelbird._base.dotdict import Style
from excelbird._base.loc import Loc
from excelbird._base.math import CanDoMath, elem_math

from excelbird._utils.util import (
    get_dimensions,
    get_idx,
    init_from_same_dimension_type,
)
from excelbird._utils.validation import (
    require_each_element_to_be_cls_type,
    ensure_value_is_not_number,
)
from excelbird._utils.argument_parsing import (
    combine_args_and_children_to_list,
    convert_all_to_type,
    move_remaining_kwargs_to_dict,
)

from excelbird.core.cell import Cell
from excelbird.core.expression import Expr
from excelbird.core.function import Func
from excelbird.core.gap import Gap
from excelbird.core.item import Item



class _Series(CanDoMath, ListIndexableById, HasId, HasHeader, HasBorder):
    _doc_primary_summary = """
    A 1-dimensional vector that can be used in a python expression
    and can be prefixed with a :ref:`header <header>`.
    """
    _doc_params = """
    Parameters
    ----------
    *args : Union[Cell, Col, Row, str, int, float, list, tuple, pd.Series, np.ndarray, Gap, Item, Expr, Func, set]
        Children must be, or resolve to, `Cell`. Iterables will be *exploded* inplace. So, if given
        ``1, pandas.Series([2, 3]), 4``, it will be read as ``1, 2, 3, 4`` before converting the
        ints to `Cell`. If a :class:`pandas.Series` is passed as the *only* argument, its name
        (if present) will be used as :ref:`header <header>`.
    children : list, optional
        Will be combined with args
    id : str, optional
        Unique identifier to store globally so that this element can be referenced
        elsewhere in the layout without being assigned to a variable
    header : str, optional
        Unique identifier to be inserted as a Cell at position 0 at write time. Can be referenced
        by an `Expr` elsewhere in the layout. Set automatically if a named ``pandas.Series`` is given.
        :ref:`Read more <header>`
    sep : Gap or bool or int or dict, optional
        A sep in any excelbird layout element inserts a `Gap` between each of its children.
        If True, a default of ``Gap(1)`` is used. If int, ``Gap(sep)`` will be used. If a dict,
        ``Gap(1, **sep)`` will be used.
    background_color : str, optional
        Hex code for background color. Will be applied to any Gap child who hasn't specified its own
        fill_color.
    cell_style : dict, optional
        Each key/value will be used to set an attribute on each child Cell (header excluded)
        only if the respective attribute has not already been set on the child Cell (its value is None).
        This mimics HTML/CSS behavior, where styling declared at the parent level is passed down
        to children, but each child can override the parent.
    header_style : dict, optional
        Just like cell_style, but for the header only. Ignored if header is None.
    border : list[tuple or str or bool] or tuple[str or bool, str or bool] or str or bool, optional
        Syntax inspired by CSS. A non-list value will be applied to all 4 sides. If list,
        length can be 2, 3, or 4 elements. Order is [top, right, bottom, left]. If length 2,
        apply the first element to top and bottom border, and apply the second element to right and left.
        To apply border to children instead, use cell_style.
    border_top : tuple[str or bool, str or bool] or str or bool, optional
        Top border. If True, a thin black border is used. If string (6 char hex code),
        use the default weight and apply the specified color. If string (valid weight name),
        use the default color and apply the specified weight. If tuple, apply the first
        element as weight, and second element as color.
    border_right : tuple[str or bool, str or bool] or str or bool, optional
        Right border. See border_top
    border_bottom : tuple[str or bool, str or bool] or str or bool, optional
        Bottom border. See border_top
    border_left : tuple[str or bool, str or bool] or str or bool, optional
        Left border. See border_top
    **kwargs : Any
        Remaining kwargs will be applied to cell_style
    """

    _dimensions = 1
    elem_type = Cell

    @overload
    def __new__(cls, fn: str | Func, **kwargs) -> Func:
        ...

    @overload
    def __new__(cls, func: str | Func, **kwargs) -> Func:
        ...

    @overload
    def __new__(cls, ex: str | set | Expr, **kwargs) -> Expr:
        ...

    @overload
    def __new__(cls, expr: str | set | Expr, **kwargs) -> Expr:
        ...

    @overload
    def __new__(cls, *args, **kwargs) -> _Series:
        ...

    def __new__(cls, *args, fn=None, func=None, ex=None, expr=None, **kwargs):
        fn = fn if fn is not None else func
        ex = ex if ex is not None else expr
        if isinstance(fn, Func):
            fn = fn.inner
        if isinstance(ex, Expr):
            ex = ex.expr_str

        if fn is not None:
            new_func = Func.__new__(Func)
            new_func.__init__(fn, res_type=cls, **kwargs)
            return new_func

        if ex is not None:
            new_expr = Expr.__new__(Expr)
            new_expr.__init__(ex, res_type=cls, **kwargs)
            return new_expr

        return super().__new__(cls)

    def __init__(
        self,
        *args: Any,
        children: list | None = None,
        id: str | None = None,
        header: str | None = None,
        sep: Any | None = None,
        border_left: bool | str | None = None,
        border_right: bool | str | None = None,
        border_top: bool | str | None = None,
        border_bottom: bool | str | None = None,
        border: bool | str | Iterable | None = None,
        background_color: str | None = None,
        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        fn: str | Func | None = None,
        func: str | Func | None = None,
        ex: str | set | Expr | None = None,
        expr: str | set | Expr | None = None,
        **kwargs,
    ) -> None:
        del fn
        del func
        del ex
        del expr
        children = combine_args_and_children_to_list(args, children)

        children = [i for i in children if i is not None]

        if cell_style is None:
            cell_style = dict()
        if header_style is None:
            header_style = dict()

        if len(children) == 1 and isinstance(get_idx(children, 0), Series):
            if children[0].name is not None and header is None:
                header = children[0].name

        self._format_args(children)

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        self._loc = None
        self.id = id
        self.header = header
        self.background_color = background_color
        self.header_style = Style(**header_style)
        # Dicts that must be passed to children
        self.cell_style = Style(**cell_style)

        self._init(children)

        self._init_border(
            border,
            border_top,
            border_right,
            border_bottom,
            border_left,
        )
        if sep is not None:
            self._insert_separator(sep)

        self.header_written = False

    def from_valid_children(
        self,
        children: list,
        id: str | None = None,
        header: str | None = None,
        sep: Any | None = None,
        border_left: bool | str | None = None,
        border_right: bool | str | None = None,
        border_top: bool | str | None = None,
        border_bottom: bool | str | None = None,
        border: bool | str | Iterable | None = None,
        background_color: str | None = None,
        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        **kwargs,
    ):
        if cell_style is None:
            cell_style = dict()
        if header_style is None:
            header_style = dict()

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        self._loc = None
        self.id = id
        self.header = header
        self.background_color = background_color
        self.header_style = Style(**header_style)
        # Dicts that must be passed to children
        self.cell_style = Style(**cell_style)

        self._init(children)

        self._init_border(
            border,
            border_top,
            border_right,
            border_bottom,
            border_left,
        )
        if sep is not None:
            self._insert_separator(sep)

        self.header_written = False

    def ref(self, inherit_style: bool = False, **kwargs):
        """
        Get a new object with cell references to those in the caller.
        This assumes that **both** the calling object
        and the returned object will be placed in the workbook.

        .. note::

            Calling ``.ref()`` is **not** necessary  when an object is used in
            a python expression (i.e. ``some_cell + some_row``) and should `only`
            be used to duplicate data across a workbook.

        Parameters
        ----------
        inherit_style : bool, default False
            Copy the caller's style to the returned object.
        **kwargs : Any
            Extra keyword arguments are set as attributes on the returned
            object.

        Returns
        -------
        :class:`Self`

        Notes
        -----

        .. note::

            ``self.header`` is a stylistic attribute, and therefore will **not** be
            passed to the returned object unless ``inherit_style=True``. And, if style
            is inherited, the header will be copied to its new cell, instead of having
            a cell reference made to it.

        """
        new_elements = [
            i.ref(inherit_style=inherit_style, **kwargs)
            for i in self
        ]
        new_dict = kwargs
        if inherit_style is True:
            self_dict = deepcopy(self.__dict__)
            for key, val in self_dict.items():
                if key == "_header":
                    key = "header"
                if key not in new_dict and key not in ["_id", "_loc"]:
                    new_dict[key] = val
        return type(self)(*new_elements, **new_dict)

    def transpose(self, **kwargs):
        """
        Convert to sibling type. Places current children into the returned object,
        without copying or making cell references to them.

        Parameters
        ----------
        **kwargs : Any
            Keyword arguments to apply as attributes to the new object.

        Returns
        -------
        :class:`Col <excelbird.Col>` or :class:`Row <excelbird.Row>`
            The opposite to self's type. Try ``type(my_obj).sibling_type``

        Notes
        -----
        **Assumes that the caller won't be placed in the layout**. Do not
        place both the calling object and returned object in the layout, since
        they both contain the same children.

        .. code-block::

            # 'current' must not be placed in the workbook.
            new = current.transpose()

        To include the caller and make cell references to it, get a reference
        first:

        .. code-block::

            new = current.ref().transpose()

        """
        elements = list(self)
        new = type(self).sibling_type(*elements)
        for key, val in self.__dict__.items():
            if key == "_header":
                key = "header"
            if key == "_id":
                key = "id"
            setattr(new, key, val)

        for key, val in kwargs.items():
            if hasattr(new, key):
                setattr(new, key, val)
            elif hasattr(new, 'cell_style'):
                new.cell_style[key] = val
        return new

    def range(self, include_headers: bool = False) -> Cell:
        """
        Get a reference to the range of the series, instead of a vector of
        cell references.

        Parameters
        ----------
        include_headers : bool, default False
            If True, the header cell will be included in the range reference.

        Returns
        -------
        :class:`Cell <excelbird.Cell>`
        """
        if self.header_written is True and include_headers is False:
            first = self[1]
        else:
            first = self[0]
        last = self[-1]
        return first >> last

    @property
    def shape(self) -> tuple[int]:
        length = sum([1 if not isinstance(i, Gap) else i for i in self])
        if self.header is not None:
            length += 1
        return (length,)

    def _format_args(self, args: list) -> None:
        self._explode_all_1d_iterables(args)
        convert_all_to_type(args, set, Expr)
        convert_all_to_type(args, int, Cell, strict=True)
        convert_all_to_type(args, (str, float), Cell)
        Item._resolve_all_in_container(args, type(self).elem_type)
        for i, elem in enumerate(args):
            if not isinstance(elem, (Cell, Iterable, Gap, Expr, Func)):
                args[i] = Cell(elem)

    def _explode_all_1d_iterables(self, args: list) -> None:

        for i, elem in enumerate(args):
            if isinstance(elem, Series):
                sr = args.pop(i)
                for cell in reversed(sr.reset_index(drop=True)):
                    args.insert(i, cell)

            elif isinstance(elem, (list, tuple, ndarray)):
                sr = args.pop(i)
                for value in reversed(sr):
                    args.insert(i, value)

    def _resolve_background_color(self) -> None:
        for elem in self:
            if hasattr(elem, "_resolve_background_color"):
                if (
                    self.background_color not in [None, False]
                    and elem.background_color is None
                ):
                    elem.background_color = self.background_color
                elem._resolve_background_color()

        if self.background_color not in [None, False]:
            for elem in self:
                if isinstance(elem, Gap):
                    if "fill_color" not in elem.kwargs:
                        elem.fill = True
                        elem.kwargs["fill_color"] = self.background_color

    def _resolve_gaps(self):
        Gap._explode_all_to_values(self, Cell)

    def _set_loc(self, loc: Loc) -> None:
        self._loc = loc

        offset = self._starting_offset()
        for elem in self:
            elem._set_loc(
                Loc((self._loc.y + offset.y, self._loc.x + offset.x), self._loc.ws)
            )
            offset = self._inc_offset(offset, elem)

    def __getitem__(self, key):
        if not isinstance(key, list):
            # return super().__getitem__(key)
            return ListIndexableById.__getitem__(self, key)

        new_elements = [self[self._key_to_idx(k)] for k in key]
        new_dict = {k: v for k, v in self.__dict__.items() if k not in ["_id", "_loc"]}
        if "_header" in new_dict:
            new_dict["header"] = new_dict.pop("_header")

        return type(self)(*new_elements, **new_dict)

    # def __rshift__(self, other):
    #     if get_dimensions(other) < get_dimensions(self):
    #         return elem_math(self[0], other, lambda a, b: a >> b, " >> ")
    #     return self[0] >> other[-1]
    #
    # def __rrshift__(self, other):
    #     if get_dimensions(other) < get_dimensions(self):
    #         return elem_math(other, self[-1], lambda a, b: a >> b, " >> ")
    #     return other[0] >> self[-1]

    def _validate_child_types(self) -> None:
        cls_name = type(self).__name__
        elem_type_name = type(self).elem_type.__name__
        valid_types = (
            type(self).elem_type,
            Gap,
        )
        for elem in self:
            if not isinstance(elem, valid_types):
                raise TypeError(
                    f"At write time, a {cls_name} can only hold {elem_type_name}s or Gaps. "
                    "To arrange mixed types, place them in a Stack or VStack"
                )
            if hasattr(elem, "_validate_child_types"):
                elem._validate_child_types()

    def _write(self) -> None:
        require_each_element_to_be_cls_type(self)

        self._apply_border()

        for cell in self:
            cell._inherit_style_without_override(self.cell_style)

        if self.header is not None:
            ensure_value_is_not_number(self.header)
            new_header = Cell(self.header)

            new_header._set_loc(self._loc)

            new_header._inherit_style_without_override(self.header_style)

            if (
                self.cell_style.get("autofit") is True
                and self.header_style.get("autofit") is not False
            ):
                new_header.autofit = True

            self.insert(0, new_header)
            self.header_written = True

        for cell in self:
            cell._write()

    def _starting_offset(self) -> Loc:
        ...


class Col(_Series):
    _doc_custom_summary = """
    * Direction: **vertical**
    * Child Type: :class:`Cell`
    """

    sibling_type: type = None  # these are set after class declaration
    elem_type = Cell

    def transpose(self, **kwargs) -> Row:
        return super().transpose(**kwargs)

    def ref(self, inherit_style: bool = False, **kwargs) -> Col:
        return super().ref(inherit_style, **kwargs)

    @property
    def width(self):
        return 1

    @property
    def height(self):
        return self.shape[0]

    def _repr_html_(self):
        from pandas import DataFrame

        header = "" if self.header is None else self.header
        elems_to_show = list(self) if len(self) <= 10 else list(self)[:10]

        if len(self) > 10:
            elems_to_show.append(f"(+{len(self)-10})")

        df = DataFrame(elems_to_show + [""], columns=[header])
        return df.style.hide(axis="index")._repr_html_()

    def _border_mask(self, top, right, bottom, left) -> Style:
        return Style(
            first=[top, right, False, left],
            last=[False, right, bottom, left],
            middle=[False, right, False, left],
        )

    @staticmethod
    def _inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.y += elem.height
        return offset

    def _starting_offset(self) -> Loc:
        offset = Loc((0, 0), self._loc.ws)
        if getattr(self, "_header", None) is not None:
            offset.y += 1
        return offset


class Row(_Series):
    _doc_custom_summary = """
    * Direction: **horizontal**
    * Child Type: :class:`Cell`
    """
    sibling_type = Col  # these are set after class declaration
    elem_type = Cell

    def transpose(self, **kwargs) -> Col:
        return super().transpose(**kwargs)

    def ref(self, inherit_style: bool = False, **kwargs) -> Row:
        return super().ref(inherit_style, **kwargs)

    @property
    def width(self):
        return self.shape[0]

    @property
    def height(self):
        return 1

    def _repr_html_(self):
        from pandas import DataFrame

        header = "" if self.header is None else self.header
        elems_to_show = list(self) if len(self) <= 10 else list(self)[:10]

        if len(self) > 10:
            elems_to_show.append(f"(+{len(self)-10})")

        df = DataFrame(
            [elems_to_show, ["" for _ in elems_to_show]],
            index=[header, ""],
            columns=["" for _ in elems_to_show],
        )

        if self.header is None:
            return df.style.hide(axis="index")._repr_html_()
        return df._repr_html_()

    def _border_mask(self, top, right, bottom, left) -> Style:
        return Style(
            first=[top, False, bottom, left],
            last=[top, right, bottom, False],
            middle=[top, False, bottom, False],
        )

    @staticmethod
    def _inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.x += elem.width
        return offset

    def _starting_offset(self) -> Loc:
        offset = Loc((0, 0), self._loc.ws)
        if getattr(self, "_header", None) is not None:
            offset.x += 1
        return offset

Col.sibling_type = Row

Col.__doc__ = f"""
    {_Series._doc_primary_summary}

    {Col._doc_custom_summary}

    {_Series._doc_params}

    """

Row.__doc__ = f"""
    {_Series._doc_primary_summary}

    {Row._doc_custom_summary}

    {_Series._doc_params}

    """




