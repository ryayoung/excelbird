# External
from pandas import Series, DataFrame
from typing import Any
from copy import deepcopy

# Internal main
from excelbird.styles.styles import default_table_style

from excelbird._base.container import ListIndexableById
from excelbird._base.identifier import HasId
from excelbird._base.dotdict import Style
from excelbird._base.loc import Loc
from excelbird._base.styling import (
    HasMargin, 
    HasPadding,
)
from excelbird._utils.util import (
    init_from_same_dimension_type,
)
from excelbird._utils.pass_attributes import (
    pass_attr_to_children,
    pass_dict_to_children,
)
from excelbird._utils.argument_parsing import (
    combine_args_and_children_to_list,
    move_dict_args_to_other_dict,
    convert_all_to_type,
    move_remaining_kwargs_to_dict,
)

from excelbird.core.cell import Cell
from excelbird.core.series import (
    _Series,
    Col,
)
from excelbird.core.gap import Gap
from excelbird.core.frame import _Frame, Frame, VFrame
from excelbird.core.expression import Expr


class _Stack(ListIndexableById, HasId, HasMargin, HasPadding):

    sibling_type = None
    elem_type = None
    _dimensions = -1

    def __init__(
        self,
        *args: Any,
        children: list | None = None,
        id: str | int | None = None,
        sep: Any | None = None,
        background_color: str | None = None,
        margin: int | list[int] | None = None,
        margin_top: int | None = None,
        margin_right: int | None = None,
        margin_bottom: int | None = None,
        margin_left: int | None = None,
        padding: int | list[int] | None = None,
        padding_top: int | None = None,
        padding_right: int | None = None,
        padding_bottom: int | None = None,
        padding_left: int | None = None,
        schema: None = None,
        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        table_style: Style | dict | bool | None = None,
        **kwargs,
    ) -> None:
        children = combine_args_and_children_to_list(args, children)

        children = [i for i in children if i is not None]

        children = init_from_same_dimension_type(self, children)
        if getattr(self, "_id", None) is not None and id is None:
            id = self.id

        if cell_style is None:
            cell_style = dict()
        if header_style is None:
            header_style = dict()
        if table_style is None or table_style is False:
            table_style = dict()
        elif table_style is True:
            table_style = default_table_style

        self._format_args(children)

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        self.loc = None
        self.id = id
        self.background_color = background_color
        # Attrs that must be passed to children
        self.schema = schema
        # Dicts that must be passed to children
        self.cell_style = Style(**cell_style)
        self.header_style = Style(**header_style)
        self.table_style = Style(**table_style)

        self._init(children)

        self.init_margin(
            margin,
            margin_top,
            margin_right,
            margin_bottom,
            margin_left,
        )
        self.init_padding(
            padding,
            padding_top,
            padding_right,
            padding_bottom,
            padding_left,
        )

        if sep is not None:
            self._insert_separator(sep)


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
        return type(self)(*new_elements, **new_dict)

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

    def _format_args(self, args: list) -> None:
        convert_all_to_type(args, (str, int, float), Cell, strict=True)
        convert_all_to_type(args, Series, Col)
        convert_all_to_type(args, DataFrame, Frame)
        convert_all_to_type(args, set, Expr)

    @property
    def _elem_widths(self) -> list:
        return [i.width for i in self if hasattr(i, "width")]

    @property
    def _elem_heights(self) -> list:
        return [i.height for i in self if hasattr(i, "height")]

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
                    if "fill_color" not in elem.kwargs and elem.is_margin is False:
                        elem.fill = True
                        elem.kwargs["fill_color"] = self.background_color

                # Child's margins should be filled with self's background color
                elif hasattr(elem, "margin"):
                    if elem.margin != HasMargin.empty:
                        for item in elem:
                            if isinstance(item, Gap):
                                if (
                                    "fill_color" not in item.kwargs
                                    and item.is_margin is True
                                ):
                                    item.fill = True
                                    item.kwargs["fill_color"] = self.background_color
                            elif hasattr(item, "margin"):
                                for x in item:
                                    if isinstance(x, Gap):
                                        if (
                                            "fill_color" not in x.kwargs
                                            and x.is_margin is True
                                        ):
                                            x.fill = True
                                            x.kwargs[
                                                "fill_color"
                                            ] = self.background_color

    def _resolve_padding(self) -> None:
        for elem in self:
            if hasattr(elem, "padding"):
                elem._resolve_padding()

        def get_gap(amount, elem) -> Gap:
            if getattr(elem, "background_color", None) not in [None, False]:
                return Gap(amount, fill_color=elem.background_color)
            return Gap(amount, fill_color=None)

        for i, elem in enumerate(self):
            if hasattr(elem, "padding"):
                if elem.padding != HasPadding.empty:
                    top, right, bottom, left = elem.padding
                    elem_type = type(elem)
                    new_elements = []
                    for i, item in reversed(list(enumerate(elem))):
                        new_elements.insert(0, elem.pop(i))

                    if issubclass(elem_type, Stack):
                        if left is not None:
                            elem.append(get_gap(left, elem))

                        elem.append(
                            elem_type.sibling_type(
                                get_gap(top, elem) if top is not None else None,
                                elem_type(*new_elements),
                                get_gap(bottom, elem) if bottom is not None else None,
                            )
                        )
                        if right is not None:
                            elem.append(get_gap(right, elem))

                    elif issubclass(elem_type, VStack):
                        if top is not None:
                            elem.append(get_gap(top, elem))

                        elem.append(
                            elem_type.sibling_type(
                                get_gap(left, elem) if left is not None else None,
                                elem_type(*new_elements),
                                get_gap(right, elem) if right is not None else None,
                            ),
                        )
                        if bottom is not None:
                            elem.append(get_gap(bottom, elem))

    def _resolve_margin(self) -> None:
        for elem in self:
            if hasattr(elem, "margin"):
                elem._resolve_margin()

        for i, elem in enumerate(self):
            if hasattr(elem, "margin"):
                if elem.margin != HasMargin.empty:
                    top, right, bottom, left = elem.margin
                    elem_type = type(elem)
                    new_elements = []
                    for i, item in reversed(list(enumerate(elem))):
                        new_elements.insert(0, elem.pop(i))

                    if issubclass(elem_type, Stack):
                        if left is not None:
                            elem.append(Gap(left, is_margin=True))

                        elem.append(
                            elem_type.sibling_type(
                                Gap(top, is_margin=True) if top is not None else None,
                                elem_type(*new_elements),
                                Gap(bottom, is_margin=True)
                                if bottom is not None
                                else None,
                            ),
                        )
                        if right is not None:
                            elem.append(Gap(right, is_margin=True))

                    elif issubclass(elem_type, VStack):
                        if top is not None:
                            elem.append(Gap(top, is_margin=True))

                        elem.append(
                            elem_type.sibling_type(
                                Gap(left, is_margin=True) if left is not None else None,
                                elem_type(*new_elements),
                                Gap(right, is_margin=True)
                                if right is not None
                                else None,
                            ),
                        )
                        if bottom is not None:
                            elem.append(Gap(bottom, is_margin=True))

    def _resolve_gaps(self) -> None:
        Gap._convert_all_to_frames(self, type(self).elem_type, self._gap_size)
        for elem in self:
            if hasattr(elem, "_resolve_gaps"):
                elem._resolve_gaps()

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

    def _validate_child_types(self) -> None:
        valid_types = (
            _Stack,
            _Frame,
            _Series,
            Cell,
            Gap,
        )
        for elem in self:
            if not isinstance(elem, valid_types):
                raise TypeError(
                    f"At write time, a {type(self).__name__} can only hold "
                    "the following types:\n{valid_types}"
                )
            if hasattr(elem, "_validate_child_types"):
                elem._validate_child_types()

    def _write(self) -> None:
        pass_attr_to_children(self, "schema")
        pass_dict_to_children(self, "cell_style")
        pass_dict_to_children(self, "header_style")
        pass_dict_to_children(self, "table_style")

        if len(self.cell_style) > 0:
            for elem in self:
                if isinstance(elem, Cell):
                    elem._inherit_style_without_override(self.cell_style)

        for elem in self:
            elem._write()


class Stack(_Stack):
    """
    A general container that can hold any element, including itself. Offers unique spatial
    styling features, like margin and padding, described below.

    ----

    * Direction: **horizontal**
    * Child Type: **Any** (excluding ``Book`` and ``Sheet``)

    ----

    Parameters
    ----------
    \*args: `Any`
        Can take any layout element (besides Book or Sheet), or any value that
        can be used to construct a layout element. Stack is the only layout element
        that can store other instances of itself as children
    children: *list, default None*
        Will be combined with args
    id: *str, default None*
        Unique identifier to store globally so that this element can be referenced
        elsewhere in the layout without being assigned to a variable
    sep: *Gap | bool | int | dict, default None*
        A sep in any excelbird layout element inserts a Gap between each of its children.
        If True, a default of Gap(1) is used. If int, Gap(sep) will be used. If a dict,
        ``Gap(1, **sep)`` will be used.
    background_color: *str, default None*
        Hex code for background_color. Will be applied to fill_color of padding, any Gap
        child who hasn't specified its own fill_color, and to any child Stack/VStack's margins.
        Will also be passed down to any child (Cell excluded) who hasn't specified its own
        background_color.
    schema: *Schema, default None*
        Applied to each child who takes schema
    cell_style: *dict, default None*
        Applied to each child who has cell_style
    header_style: *dict, default None*
        Applied to each child who has header_style
    table_style: *dict | bool, default None*
        Applied to each child who has table_style
    margin: *int | list[int], default None*
        Margin, like padding, will apply space around the element. Unlike padding, margin space
        will NOT inherit any of the element's styling. It will, however, be filled with the
        parent container's background_color, if present. Syntax inspired by CSS. An int,
        if passed, will be applied to all 4 sides. If list, length can be 2, 3, or 4 elements.
        Order is [top, right, bottom, left]. If length 2, apply the first element to top and
        bottom margin, and second to right and left.
    margin_top: *int, default None*
        Top margin, measured in number of cells
    margin_right: *int, default None*
        Right margin, measured in number of cells
    margin_bottom: *int, default None*
        Bottom marign, measured in number of cells
    margin_left: *int, default None*
        Left margin, measured in number of cells
    padding: *int | list[int], default None*
        Padding, like margin, will apply space around the element. Unlike margin, padding space
        WILL inherit the element's styling, like background_color. Syntax inspired by CSS. An int,
        if passed, will be applied to all 4 sides. If list, length can be 2, 3, or 4 elements.
        Order is [top, right, bottom, left]. If length 2, apply the first element to top and
        bottom margin, and second to right and left.
    padding_top: *int, default None*
        Top padding, measured in number of cells
    padding_right: *int, default None*
        Right padding, measured in number of cells
    padding_bottom: *int, default None*
        Bottom padding, measured in number of cells
    padding_left: *int, default None*
        Left padding, measured in number of cells
    \*\*kwargs:
        Remaining kwargs will be applied to cell_style
    """
    sibling_type = None  # these are set after class declaration
    elem_type = Frame

    @property
    def width(self) -> int:
        return sum(self._elem_widths + [0])

    @property
    def height(self) -> int:
        heights = [i.height for i in self if hasattr(i, 'height') and not isinstance(i, Gap)]
        return max(heights + [0])

    @staticmethod
    def _inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.x += elem.width
        return offset

    def _starting_offset(self) -> Loc:
        return Loc((0, 0), self.loc.ws)

    @property
    def _gap_size(self) -> int:
        return self.height


class VStack(_Stack):
    """
    The vertically-arranged sibling to ``Stack``. Otherwise functionally identical.

    ----

    * Direction: **vertical**
    * Child Type: **Any** (excluding ``Book`` and ``Sheet``)

    ----

    """
    sibling_type = None  # these are set after class declaration
    elem_type = VFrame

    @property
    def width(self) -> int:
        widths = [i.width for i in self if hasattr(i, 'width') and not isinstance(i, Gap)]
        return max(widths + [0])

    @property
    def height(self) -> int:
        return sum(self._elem_heights + [0])

    @staticmethod
    def _inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.y += elem.height
        return offset

    def _starting_offset(self) -> Loc:
        return Loc((0, 0), self.loc.ws)

    @property
    def _gap_size(self) -> int:
        return self.width


Stack.sibling_type = VStack
VStack.sibling_type = Stack
