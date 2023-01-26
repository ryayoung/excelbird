# External
from pandas import Series
from typing import Iterable, Any
from copy import copy, deepcopy

# Internal main
from excelbird.base_types import (
    Gap,
    ListIndexableById,
    HasId,
    HasHeader,
    HasBorder,
    Style,
    Loc,
    ImpliedType,
)
from excelbird.util import (
    get_dimensions,
    get_idx,
    combine_args_and_children_to_list,
    move_dict_args_to_other_dict,
    ensure_value_is_not_number,
    convert_all_to_type,
    init_container,
    init_from_same_dimension_type,
    move_remaining_kwargs_to_dict,
    require_each_element_to_be_cls_type,
    insert_separator,
)
from excelbird.math import CanDoMath, elem_math
from excelbird.expression import Expr
from excelbird.function import Func

# Internal core
from excelbird.core.cell import Cell


class _Vec(CanDoMath, ListIndexableById, HasId, HasHeader, HasBorder):
    """
    A 1-dimensional vector that holds Cells.

    Parameters
    ----------
    *args Any
        Children must be (or resolve to) Cells. Gap and ImpliedType will be interpreted
        as Cell.
    children: list, default None
        Will be combined with *args
    id: str, default None
        Unique identifier to store globally so that this element can be referenced
        elsewhere in the layout without being assigned to a variable
    header: str, default None
        Unique identifier to be inserted as a Cell at position 0 at write time. Headers are
        stored globally, and can be referenced elsewhere in the layout just like ids. Headers are
        ignored during expression evaluation, so for instance, `col2 = col1 + row1`, where col1 and
        row1 each have headers, will return a Col with no header, whose children each reference an
        element in col1 and row1.
    sep: Gap | bool | int | dict, default None
        A sep in any excelbird layout element inserts a Gap between each of its children.
        If True, a default of Gap(1) is used. If int, Gap(sep) will be used. If a dict,
        Gap(1, **sep) will be used.
    background_color: str, default None
        Hex code for background color. Will be applied to any Gap child who hasn't specified its own
        fill_color.
    cell_style: dict, default None
        Each key/value will be used to set an attribute on each child Cell (header excluded)
        only if the respective attribute has not already been set on the child Cell (its value is None).
        This mimics HTML/CSS behavior, where styling declared at the parent level is passed down
        to children, but each child can override the parent.
    header_style: dict, default None
        Just like cell_style, but for the header only. Ignored if header is None.
    border: list[tuple | str | bool] | tuple[str | bool, str | bool] | str | bool, default None
        Syntax inspired by CSS. A non-list value will be applied to all 4 sides. If list,
        length can be 2, 3, or 4 elements. Order is [top, right, bottom, left]. If length 2,
        apply the first element to top and bottom border, and apply the second element to right and left.
        To apply border to children instead, use cell_style.
    border_top: tuple[str | bool, str | bool] | str | bool, default None
        Top border. If True, a thin black border is used. If string (6 char hex code),
        use the default weight and apply the specified color. If string (valid weight name),
        use the default color and apply the specified weight. If tuple, apply the first
        element as weight, and second element as color.
    border_right: tuple[str | bool, str | bool] | str | bool, default None
        Right border. See border_top
    border_bottom: tuple[str | bool, str | bool] | str | bool, default None
        Bottom border. See border_top
    border_left: tuple[str | bool, str | bool] | str | bool, default None
        Left border. See border_top
    **kwargs: Any
        Remaining kwargs will be applied to cell_style
    """

    dimensions = 1
    elem_type = Cell

    def __init__(
        self,
        *args,
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
        args = combine_args_and_children_to_list(args, children)

        args = [i for i in args if i is not None]

        args = init_from_same_dimension_type(self, args)
        if getattr(self, "_header", None) is not None and header is None:
            header = self.header

        if cell_style is None:
            cell_style = dict()
        if header_style is None:
            header_style = dict()

        move_dict_args_to_other_dict(args, cell_style)
        # self.move_kwargs_to_args(args, kwargs)
        if len(args) == 1 and isinstance(get_idx(args, 0), Series):
            if args[0].name is not None and header is None:
                header = args[0].name

        convert_all_to_type(args, set, Expr)
        Cell.convert_all_values(args)
        self.explode_all_series(args)
        ImpliedType.resolve_all_in_container(args, self.__class__.elem_type)

        Cell.explode_all_lists_tuples(args)

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        init_container(
            self,
            args,
            loc=None,
            id=id,
            header=header,
            header_style=Style(**header_style),
            background_color=background_color,
            # Dicts that must be passed to children
            cell_style=Style(**cell_style),
        )
        self.init_border(
            border,
            border_top,
            border_right,
            border_bottom,
            border_left,
        )
        if sep is not None:
            insert_separator(self, sep)

        self.header_written = False

    def explode_all_series(self, args: list) -> None:
        for i, elem in enumerate(args):
            if isinstance(elem, Series):
                sr = args.pop(i)
                for cell in reversed(sr.reset_index(drop=True)):
                    args.insert(i, self.__class__.elem_type(cell))

    def resolve_background_color(self) -> None:
        for elem in self:
            if hasattr(elem, "resolve_background_color"):
                if (
                    self.background_color not in [None, False]
                    and elem.background_color is None
                ):
                    elem.background_color = self.background_color
                elem.resolve_background_color()

        if self.background_color not in [None, False]:
            for elem in self:
                if isinstance(elem, Gap):
                    if "fill_color" not in elem.kwargs:
                        elem.fill = True
                        elem.kwargs["fill_color"] = self.background_color

    def resolve_gaps(self):
        Gap.explode_all_to_values(self, Cell)

    def set_loc(self, loc: Loc) -> None:
        self.loc = loc

        offset = self.starting_offset()
        for elem in self:
            elem.set_loc(
                Loc((self.loc.y + offset.y, self.loc.x + offset.x), self.loc.ws)
            )
            offset = self.inc_offset(offset, elem)

    def __getitem__(self, key):
        if not isinstance(key, list):
            # return super().__getitem__(key)
            return ListIndexableById.__getitem__(self, key)

        new_elements = [self[self.key_to_idx(k)] for k in key]
        new_dict = {k: v for k, v in self.__dict__.items() if k not in ["_id", "loc"]}
        if "_header" in new_dict:
            new_dict["header"] = new_dict.pop("_header")

        return self.__class__(*new_elements, **new_dict)

    def __rshift__(self, other):
        if get_dimensions(other) < get_dimensions(self):
            return elem_math(self[0], other, lambda a, b: a >> b, " >> ")
        return self[0] >> other[-1]

    def __rrshift__(self, other):
        if get_dimensions(other) < get_dimensions(self):
            return elem_math(other, self[-1], lambda a, b: a >> b, " >> ")
        return other[0] >> self[-1]

    def ref(self, inherit_style: bool = False, **kwargs):
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
        return self.__class__(*new_elements, **new_dict)

    def astype(self, other: type, **kwargs):
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
        if self.header_written is True and include_headers is False:
            first = self[1]
        else:
            first = self[0]
        last = self[-1]
        return first >> last

    def validate_child_types(self) -> None:
        cls_name = self.__class__.__name__
        elem_type_name = self.__class__.elem_type.__name__
        valid_types = (
            self.__class__.elem_type,
            Gap,
        )
        for elem in self:
            if not isinstance(elem, valid_types):
                raise TypeError(
                    f"At write time, a {cls_name} can only hold {elem_type_name}s or Gaps. "
                    "To arrange mixed types, place them in a Stack or VStack"
                )
            if hasattr(elem, "validate_child_types"):
                elem.validate_child_types()

    def _write(self) -> None:
        require_each_element_to_be_cls_type(self)

        self.apply_border()

        for cell in self:
            cell.inherit_style_without_override(self.cell_style)

        if self.header is not None:
            ensure_value_is_not_number(self.header)
            new_header = Cell(self.header)

            new_header.set_loc(self.loc)

            new_header.inherit_style_without_override(self.header_style)

            if (
                self.cell_style.get("autofit") is True
                and self.header_style.get("autofit") is not False
            ):
                new_header.autofit = True

            self.insert(0, new_header)
            self.header_written = True

        for cell in self:
            cell._write()
