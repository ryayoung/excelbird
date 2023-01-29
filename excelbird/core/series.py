"""
Here is the docstring for series module
"""
# External
from pandas import Series
from typing import Iterable, Any
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

    _dimensions = 1
    elem_type = Cell

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
        **kwargs,
    ) -> None:
        children = combine_args_and_children_to_list(args, children)

        children = [i for i in children if i is not None]

        children = init_from_same_dimension_type(self, children)
        if getattr(self, "_header", None) is not None and header is None:
            header = self.header

        if cell_style is None:
            cell_style = dict()
        if header_style is None:
            header_style = dict()

        if len(children) == 1 and isinstance(get_idx(children, 0), Series):
            if children[0].name is not None and header is None:
                header = children[0].name

        self._format_args(children)

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        self.loc = None
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
        Ref doc
        """
        new_elements = [
            i.ref(inherit_style=inherit_style, **kwargs)
            if not isinstance(i, Gap)
            else deepcopy(i)
            for i in self
        ]
        new_dict = kwargs
        if inherit_style is True:
            self_dict = deepcopy(self.__dict__)
            for key, val in self_dict.items():
                if key == "_header":
                    key = "header"
                if key not in new_dict and key not in ["_id", "loc"]:
                    new_dict[key] = val
        return type(self)(*new_elements, **new_dict)

    def astype(self, other: type, **kwargs):
        """
        Astype doc

        Parameters
        ----------
        other : type
            The type we want to convert to
        """
        elements = list(self)
        new = other(*elements)
        for key, val in self.__dict__.items():
            if key == "_header":
                key = "header"
            if key != "_id":
                setattr(new, key, val)
        for key, val in kwargs.items():
            setattr(new, key, val)
        return new

    @property
    def shape(self) -> tuple[int]:
        length = sum([1 if not isinstance(i, Gap) else i for i in self])
        if self.header is not None:
            length += 1
        return (length,)

    def range(self, include_headers: bool = False):
        """
        Range doc
        """
        if self.header_written is True and include_headers is False:
            first = self[1]
        else:
            first = self[0]
        last = self[-1]
        return first >> last

    def _format_args(self, args: list) -> None:
        convert_all_to_type(args, set, Expr)
        convert_all_to_type(args, (str, int, float), Cell, strict=True)
        self._explode_all_series(args)
        Item._resolve_all_in_container(args, type(self).elem_type)

    def _explode_all_series(self, args: list) -> None:
        for i, elem in enumerate(args):
            if isinstance(elem, Series):
                sr = args.pop(i)
                for cell in reversed(sr.reset_index(drop=True)):
                    args.insert(i, type(self).elem_type(cell))

            elif type(elem) in [list, tuple]:
                sr = args.pop(i)
                for value in reversed(sr):

                    if isinstance(value, set):
                        value = Expr(value.pop())

                    if isinstance(value, (Cell, Gap, Expr, Func)):
                        args.insert(i, value)
                    else:
                        args.insert(i, Cell(value))

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
        self.loc = loc

        offset = self._starting_offset()
        for elem in self:
            elem._set_loc(
                Loc((self.loc.y + offset.y, self.loc.x + offset.x), self.loc.ws)
            )
            offset = self._inc_offset(offset, elem)

    def __getitem__(self, key):
        if not isinstance(key, list):
            # return super().__getitem__(key)
            return ListIndexableById.__getitem__(self, key)

        new_elements = [self[self._key_to_idx(k)] for k in key]
        new_dict = {k: v for k, v in self.__dict__.items() if k not in ["_id", "loc"]}
        if "_header" in new_dict:
            new_dict["header"] = new_dict.pop("_header")

        return type(self)(*new_elements, **new_dict)

    def __rshift__(self, other):
        if get_dimensions(other) < get_dimensions(self):
            return elem_math(self[0], other, lambda a, b: a >> b, " >> ")
        return self[0] >> other[-1]

    def __rrshift__(self, other):
        if get_dimensions(other) < get_dimensions(self):
            return elem_math(other, self[-1], lambda a, b: a >> b, " >> ")
        return other[0] >> self[-1]

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

            new_header._set_loc(self.loc)

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



class Col(_Series):
    """
    A series (1-dimensional vector) that holds ``Cell`` and arranges itself vertically.

    .. code-block::
       :caption: A cool example

       The output of this line starts with four spaces.

    * Direction: **vertical**
    * Child Type: ``Cell``

    .. warning:: Warning text.

    .. note:: Note text.

    Parameters
    ----------
    *args: Any
        Children must be (or resolve to) Cells. ``Gap`` and ``Item`` will be interpreted
        as Cell.
    children : list, default None
        Will be combined with args
    id : str, default None
        Unique identifier to store globally so that this element can be referenced
        elsewhere in the layout without being assigned to a variable
    header : str, default None
        Unique identifier to be inserted as a Cell at position 0 at write time. Headers are
        stored globally, and can be referenced elsewhere in the layout just like ids. Headers are
        ignored during expression evaluation, so for instance, `col2 = col1 + row1`, where col1 and
        row1 each have headers, will return a Col with no header, whose children each reference an
        element in col1 and row1.
    sep : Gap or bool or int or dict, default None
        A sep in any excelbird layout element inserts a Gap between each of its children.
        If True, a default of Gap(1) is used. If int, Gap(sep) will be used. If a dict,
        ``Gap(1, **sep)`` will be used.
    background_color : str, default None
        Hex code for background color. Will be applied to any Gap child who hasn't specified its own
        fill_color.
    cell_style : dict, default None
        Each key/value will be used to set an attribute on each child Cell (header excluded)
        only if the respective attribute has not already been set on the child Cell (its value is None).
        This mimics HTML/CSS behavior, where styling declared at the parent level is passed down
        to children, but each child can override the parent.
    header_style : dict, default None
        Just like cell_style, but for the header only. Ignored if header is None.
    border : list[tuple or str or bool] or tuple[str or bool, str or bool] or str or bool, default None
        Syntax inspired by CSS. A non-list value will be applied to all 4 sides. If list,
        length can be 2, 3, or 4 elements. Order is [top, right, bottom, left]. If length 2,
        apply the first element to top and bottom border, and apply the second element to right and left.
        To apply border to children instead, use cell_style.
    border_top : tuple[str or bool, str or bool] or str or bool, default None
        Top border. If True, a thin black border is used. If string (6 char hex code),
        use the default weight and apply the specified color. If string (valid weight name),
        use the default color and apply the specified weight. If tuple, apply the first
        element as weight, and second element as color.
    border_right : tuple[str or bool, str or bool] or str or bool, default None
        Right border. See border_top
    border_bottom : tuple[str or bool, str or bool] or str or bool, default None
        Bottom border. See border_top
    border_left : tuple[str or bool, str or bool] or str or bool, default None
        Left border. See border_top
    **kwargs:
        Remaining kwargs will be applied to cell_style

    """
    sibling_type = None  # these are set after class declaration
    elem_type = Cell

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
        offset = Loc((0, 0), self.loc.ws)
        if getattr(self, "_header", None) is not None:
            offset.y += 1
        return offset


class Row(_Series):
    """
    The horizontally-arranged sibling to ``Col`` . Otherwise functionally identical.

    * Direction: **horizontal**
    * Child Type: ``Cell``

    """
    elem_type = Cell
    sibling_type = None  # these are set after class declaration

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
        offset = Loc((0, 0), self.loc.ws)
        if getattr(self, "_header", None) is not None:
            offset.x += 1
        return offset


Col.sibling_type = Row
Row.sibling_type = Col
