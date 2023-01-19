# External
from pandas import Series, DataFrame
from typing import Any, Iterable
# Internal main
from excelbird.expression import Expr
from excelbird.function import Func
from excelbird.styles import default_table_style
from excelbird.base_types import Style, Loc, Gap, ImpliedType, ListIndexableById, HasId, HasBorder
from excelbird.util import (
    get_dimensions,
    get_idx,
    combine_args_and_children_to_list,
    move_dict_args_to_other_dict,
    pass_attr_to_children,
    pass_dict_to_children,
    convert_all_to_type,
    init_from_same_dimension_type,
    init_container,
    move_remaining_kwargs_to_dict,
    insert_separator,
)
# Internal core
from excelbird.core.cell import Cell
from excelbird.core.vec import (
    _Vec,
    Col,
    Row,
    _HorizontalVec,
    _VerticalVec,
)
from excelbird.core.frame import _Frame, Frame, VFrame

class _Stack(ListIndexableById, HasId, HasBorder):
    sibling_type = None
    elem_type = None
    dimensions = -1

    def __init__(
        self,
        *args: Any,
        children: list | None = None,
        id: str | int | None = None,
        sep: Any | None = None,
        border_top: bool | str | None = None,
        border_right: bool | str | None = None,
        border_bottom: bool | str | None = None,
        border_left: bool | str | None = None,
        border: bool | str | Iterable | None = None,

        schema: None = None,

        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        table_style: Style | dict | bool | None = None,
        **kwargs,
    ) -> None:
        args = combine_args_and_children_to_list(args, children)
        # if isinstance(get_idx(args, 0), str) and id is None:
        #     id = args.pop(0)
        args = [i for i in args if i is not None]

        args = init_from_same_dimension_type(self, args)
        if getattr(self, "_id", None) is not None and id is None:
            id = self.id

        if cell_style is None: cell_style = dict()
        if header_style is None: header_style = dict()
        if table_style is None: table_style = dict()
        elif table_style is True: table_style = default_table_style

        move_dict_args_to_other_dict(args, cell_style)
        Cell.convert_all_values(args)

        frame_type = self.__class__.elem_type
        vec_type = frame_type.elem_type
        ImpliedType.resolve_all_in_container(args, frame_type)
        convert_all_to_type(args, Series, vec_type)
        convert_all_to_type(args, DataFrame, frame_type)
        convert_all_to_type(args, set, Expr)

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        init_container(self, args,
            loc = None,
            id = id,
            # Attrs that must be passed to children
            schema = schema,
            # Dicts that must be passed to children
            cell_style = Style(**cell_style),
            header_style = Style(**header_style),
            table_style = Style(**table_style),
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


    @property
    def elem_widths(self) -> list:
        return [i.width for i in self if hasattr(i, "width")]

    @property
    def elem_heights(self) -> list:
        return [i.height for i in self if hasattr(i, "height")]

    def resolve_gaps(self) -> None:
        Gap.convert_all_to_frames(self, self.__class__.elem_type, self.gap_size)
        for elem in self:
            elem.resolve_gaps()
    
    def set_loc(self, loc: Loc) -> None:
        _Vec.set_loc(self, loc)
    
    def apply_border(self) -> None:
        return _Vec.apply_border(self)
    
    def __getitem__(self, key):
        return _Vec.__getitem__(self, key)
    
    def ref(self, inherit_style: bool = False, **kwargs):
        return _Vec.ref(self, inherit_style, **kwargs)
    
    def astype(self, other: type, **kwargs):
        return _Vec.astype(self, other, **kwargs)

    def validate_child_types(self) -> None:
        valid_types = (
            Stack,
            VStack,
            Frame, 
            VFrame, 
            Col, 
            Row, 
            Cell, 
            Gap,
        )
        for elem in self:
            if not isinstance(elem, valid_types):
                raise TypeError(
                    f"At write time, a {self.__class__.__name__} can only hold "
                    "the following types:\n{valid_types}"
                )
            if hasattr(elem, "validate_child_types"):
                elem.validate_child_types()

    def _write(self) -> None:
        self.apply_border()

        pass_attr_to_children(self, "schema")
        pass_dict_to_children(self, "cell_style")
        pass_dict_to_children(self, "header_style")
        pass_dict_to_children(self, "table_style")

        if len(self.cell_style) > 0:
            for elem in self:
                if isinstance(elem, Cell):
                    elem.inherit_style_without_override(self.cell_style)

        for elem in self:
            elem._write()


class VStack(_Stack, _VerticalVec):
    sibling_type = None # these are set after class declaration
    elem_type = VFrame

    def border_mask(self, top, right, bottom, left) -> Style:
        return _VerticalVec.border_mask(self, top, right, bottom, left)

    @staticmethod
    def inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.y += elem.height
        return offset
    
    def starting_offset(self) -> Loc:
        return Loc((0,0), self.loc.ws)

    @property
    def width(self) -> int:
        return max(self.elem_widths + [0])

    @property
    def height(self) -> int:
        return sum(self.elem_heights + [0])
    
    @property
    def gap_size(self) -> int:
        return self.width


class Stack(_Stack, _HorizontalVec):
    sibling_type = None # these are set after class declaration
    elem_type = Frame

    def border_mask(self, top, right, bottom, left) -> Style:
        return _HorizontalVec.border_mask(self, top, right, bottom, left)

    @staticmethod
    def inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.x += elem.width
        return offset

    def starting_offset(self) -> Loc:
        return Loc((0,0), self.loc.ws)

    @property
    def width(self) -> int:
        return sum(self.elem_widths + [0])

    @property
    def height(self) -> int:
        return max(self.elem_heights + [0])

    @property
    def gap_size(self) -> int:
        return self.height


Stack.sibling_type = VStack
VStack.sibling_type = Stack
