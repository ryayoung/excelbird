# External
from pandas import Series
from typing import Iterable, Any
from copy import copy, deepcopy
# Internal main
from excelbird.base_types import (
    Gap,
    ListIndexableById,
    HasId,
    HasBorder,
    Style,
    DotDict,
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
)
from excelbird.math import CanDoMath, elem_math
from excelbird.expression import Expr
from excelbird.function import _DelayedFunc
# Internal core
from excelbird.core.cell import Cell

class _Vec(CanDoMath, ListIndexableById, HasId, HasBorder):
    dimensions = 1
    elem_type = Cell

    def __init__(
        self,
        *args,
        children: list | None = None,
        id: str | None = None,
        header: str | None = None,
        border_left: bool | str | None = None,
        border_right: bool | str | None = None,
        border_top: bool | str | None = None,
        border_bottom: bool | str | None = None,
        border: bool | str | Iterable | None = None,

        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        **kwargs,
    ) -> None:
        args = combine_args_and_children_to_list(args, children)
        if len(args) > 1 and isinstance(get_idx(args, 0), str) and header is None:
            header = args.pop(0)
        
        args = init_from_same_dimension_type(self, args)
        if getattr(self, "header", None) is not None and header is None:
            header = self.header

        if cell_style is None: cell_style = dict()
        if header_style is None: header_style = dict()

        move_dict_args_to_other_dict(args, cell_style)
        self.move_kwargs_to_args(args, kwargs)
        if len(args) == 1 and isinstance(get_idx(args, 0), Series):
            if args[0].name is not None and header is None:
                header = args[0].name

        convert_all_to_type(args, set, Expr)
        Cell.convert_all_values(args)
        self.explode_all_series(args)
        ImpliedType.resolve_all_in_container(args, self.__class__.elem_type)

        Cell.explode_all_lists_tuples(args)

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        init_container(self, args,
            loc = None,
            id = id,
            header = header,
            header_style = Style(**header_style),
            # Dicts that must be passed to children
            cell_style = Style(**cell_style),
        )
        self.init_border(
            border,
            border_top,
            border_right,
            border_bottom,
            border_left,
        )
    
    
    def explode_all_series(self, args: list) -> None:
        for i, elem in enumerate(args):
            if isinstance(elem, Series):
                sr = args.pop(i)
                for cell in reversed(sr):
                    args.insert(i, self.__class__.elem_type(cell))
    
    def move_kwargs_to_args(self, args: list, kwargs: dict) -> None:
        """
        Key -> id
        Types:
            set
            elem_type
            Expr
            _DelayedFunc
            I
        """
        keys_to_pop = []
        for key, val in kwargs.items():

            if isinstance(val, set):
                if len(val) == 1:
                    keys_to_pop.append(key)
                    args.append(Expr(val.pop(), id=key))

            elif isinstance(val, (Cell, Expr, _DelayedFunc)):
                keys_to_pop.append(key)
                val.id = key
                args.append(val)

            elif isinstance(val, ImpliedType):
                keys_to_pop.append(key)
                new_cell = val.astype(Cell, id=key)
                args.append(new_cell)

        for key in keys_to_pop:
            kwargs.pop(key)

    def set(self, **kwargs):
        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)
        return self

    def range(self):
        return self.first_cell >> self.last_cell

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

    def _write(self) -> None:
        require_each_element_to_be_cls_type(self)

        self.apply_border()

        for cell in self:
            cell.inherit_style_without_override(self.cell_style)

        if self.header is not None:
            if isinstance(self.header, Cell):
                ensure_value_is_not_number(self.header.value)
                new_header = self.header
            else:
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


        for cell in self:
            cell._write()

    def apply_border(self) -> None:
        if len(self) == 0 or self.border == [None, None, None, None]:
            return
        
        first = self[0]

        if len(self) == 1:
            first.border = self.border

        elif len(self) >= 2:
            mask = self.border_mask(*self.border)
            last = self[-1]
            vecs_in_between = self[1:-1]

            first.border = mask.first
            last.border = mask.last
            if len(self) > 2:
                for vec in vecs_in_between:
                    vec.border = mask.middle

    def key_to_idx(self, key: str | int) -> int:
        try:
            return super().key_to_idx(key)
        except (KeyError, IndexError):
            values = [i.value if hasattr(i, "value") else None for i in self]
            if key in values:
                return values.index(key)

            raise KeyError(f"Invalid key, {key}")

    def __getitem__(self, key):
        if not isinstance(key, list):
            return super().__getitem__(key)

        new_elements = [self[self.key_to_idx(k)] for k in key]
        new_dict = {
            k:v for k,v in self.__dict__.items() if k not in ["_id", "loc"]
        }

        return self.__class__(*new_elements, **new_dict)
    
    # def __getattr__(self, key):
    #     try:
    #         if hasattr(self, key):
    #             return object.__getattr__(self, key)
    #     except (KeyError, IndexError):
    #         return self[self.key_to_idx(key)]

    def __rshift__(self, other):
        if get_dimensions(other) < get_dimensions(self):
            return elem_math(self[0], other, lambda a,b: a >> b, " >> ")
        return self[0] >> other[-1]
    
    def __rrshift__(self, other):
        if get_dimensions(other) < get_dimensions(self):
            return elem_math(other, self[-1], lambda a,b: a >> b, " >> ")
        return other[0] >> self[-1]

    def ref(self, inherit_style: bool = False, **kwargs):
        new_elements = [i.ref(inherit_style=inherit_style, **kwargs) for i in self]
        new_dict = kwargs
        if inherit_style is True:
            self_dict = deepcopy(self.__dict__)
            for key, val in self_dict.items():
                if key == "_border":
                    key = "border"
                if key not in new_dict and key not in ["_id", "loc"]:
                    new_dict[key] = val
        return self.__class__(*new_elements, **new_dict)
    
    def astype(self, other: type, **kwargs):
        elements = list(self)
        new = other(*elements)
        for key, val in self.__dict__.items():
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
    
    @property
    def first_cell(self) -> Cell:
        if self.__class__.dimensions == 1:
            return self[0]
        elif self.__class__.dimensions == 2:
            return self[0][0]
    
    @property
    def last_cell(self) -> Cell:
        if self.__class__.dimensions == 1:
            return self[-1]
        elif self.__class__.dimensions == 2:
            return self[-1][-1]
    

class _HorizontalVec(_Vec):
    def border_mask(self, top, right, bottom, left) -> Style:
        return DotDict(
            first=(top, False, bottom, left),
            last=(top, right, bottom, False),
            middle=(top, False, bottom, False),
        )

    @staticmethod
    def inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.x += elem.width
        return offset

    def starting_offset(self) -> Loc:
        offset = Loc((0,0), self.loc.ws)
        if getattr(self, "header", None) is not None:
            offset.x += 1
        return offset


class _VerticalVec(_Vec):
    def border_mask(self, top, right, bottom, left) -> Style:
        return DotDict(
            first=(top, right, False, left),
            last=(False, right, bottom, left),
            middle=(False, right, False, left),
        )

    @staticmethod
    def inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.y += elem.height
        return offset
    
    def starting_offset(self) -> Loc:
        offset = Loc((0,0), self.loc.ws)
        if getattr(self, "header", None) is not None:
            offset.y += 1
        return offset


class Row(_HorizontalVec):
    sibling_type = None # these are set after class declaration

    @property
    def width(self):
        return self.shape[0]

    @property
    def height(self):
        return 1


class Col(_VerticalVec):
    sibling_type = None # these are set after class declaration

    @property
    def width(self):
        return 1

    @property
    def height(self):
        return self.shape[0]


Col.sibling_type = Row
Row.sibling_type = Col
