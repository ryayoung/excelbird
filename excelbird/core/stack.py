# External
from pandas import Series, DataFrame
from typing import Any, Iterable
# Internal main
from excelbird.expression import Expr
from excelbird.function import _DelayedFunc
from excelbird.styles import default_table_style
from excelbird.base_types import Style, Loc, Gap, ImpliedType
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
from excelbird.core.frame import HFrame, VFrame

class _Stack(_Vec):
    dimensions = None
    elem_type = None

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
        if isinstance(get_idx(args, 0), str) and id is None:
            id = args.pop(0)

        args = init_from_same_dimension_type(self, args)
        if getattr(self, "_id", None) is not None and id is None:
            id = self.id

        if cell_style is None: cell_style = dict()
        if header_style is None: header_style = dict()
        if table_style is None: table_style = dict()
        elif table_style is True: table_style = default_table_style

        move_dict_args_to_other_dict(args, cell_style)
        self.move_kwargs_to_args(args, kwargs)
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

        if sep is not None:
            print("sep is not None")
            for i, elem in reversed(list(enumerate(self))):
                if i > 0:
                    self.insert(i, sep)

    
    def move_kwargs_to_args(self, args: list, kwargs: dict) -> None:
        """
        Key -> header OR id, depending on type
        Types:
            set
            Expr, _DelayedFunc
            Cell
            elem_type
        """
        frame_type = self.__class__.elem_type
        vec_type = frame_type.elem_type
        keys_to_pop = []
        for key, val in kwargs.items():

            if isinstance(val, set):
                if len(val) == 1:
                    keys_to_pop.append(key)
                    # Expr can take header and id safely and decide upon resolution which
                    # attribute to use
                    args.append(Expr(val.pop(), header=key, id=key))

            elif isinstance(val, (Expr, _DelayedFunc)):
                keys_to_pop.append(key)
                val.header = key
                val.id = key
                args.append(val)

            elif isinstance(val, Cell):
                keys_to_pop.append(key)
                val.id = key
                args.append(val)

            elif isinstance(val, vec_type):
                keys_to_pop.append(key)
                val.header = key
                args.append(val)

            elif isinstance(val, Series):
                keys_to_pop.append(key)
                args.append(vec_type(val, header=key))

            elif isinstance(val, DataFrame):
                keys_to_pop.append(key)
                args.append(frame_type(val, id=key))

        for key in keys_to_pop:
            kwargs.pop(key)

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

    def raise_no_math_error(self, msg: str | None = None):
        if msg is None:
            msg = "Can't do math operations on a Stack"
        raise ValueError(msg)

    def __add__(self, other):
        self.raise_no_math_error()

    @property
    def all_widths(self) -> list:
        return [i.width for i in self if hasattr(i, "width")]

    @property
    def all_heights(self) -> list:
        return [i.height for i in self if hasattr(i, "height")]

    def resolve_gaps(self) -> None:
        Gap.convert_all_to_frames(self, self.__class__.elem_type, self.gap_size)
        for elem in self:
            elem.resolve_gaps()


class VStack(_Stack, _VerticalVec):
    sibling_type = None # these are set after class declaration
    elem_type = VFrame

    @property
    def width(self) -> int:
        return max(self.all_widths + [0])

    @property
    def height(self) -> int:
        return sum(self.all_heights + [0])
    
    @property
    def gap_size(self) -> int:
        return self.width


class HStack(_Stack, _HorizontalVec):
    sibling_type = None # these are set after class declaration
    elem_type = HFrame

    @property
    def width(self) -> int:
        return sum(self.all_widths + [0])

    @property
    def height(self) -> int:
        return max(self.all_heights + [0])

    @property
    def gap_size(self) -> int:
        return self.height


HStack.sibling_type = VStack
VStack.sibling_type = HStack
