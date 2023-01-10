# External
from pandas import Series, DataFrame
from typing import Any
# Internal main
from excelbird.expression import Expr
from excelbird.function import _DelayedFunc
from excelbird.base_types import Style, ImpliedType, Gap
from excelbird.styles import default_table_style
from excelbird.util import (
    get_idx,
    combine_args_and_children_to_list,
    move_dict_args_to_other_dict,
    pass_dict_to_children,
    convert_all_to_type,
    init_container,
    init_from_same_dimension_type,
    move_remaining_kwargs_to_dict,
    get_dimensions,
    insert_separator,
)
# Internal core
from excelbird.core.cell import Cell
from excelbird.core.vec import Col
from excelbird.core.frame import HFrame
from excelbird.core.stack import VStack

class Sheet(VStack):
    def __init__(
        self,
        *args: Any,
        children: list | None = None,
        title: str | None = None,
        sep: Any | None = None,
        tab_color: str | None = None,

        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        table_style: Style | dict | bool | None = None,
        **kwargs,
    ) -> None:
        args = combine_args_and_children_to_list(args, children)
        first_arg = get_idx(args, 0)
        if isinstance(first_arg, str):
            title = args.pop(0)

        # Alternative to init_from_same_dimension_type
        elif len(args) == 1 and isinstance(first_arg, Sheet):
            args = list(first_arg)
            new_kwargs = first_arg.__dict__
            new_kwargs.pop("loc")
            for key, val in new_kwargs.items():
                setattr(self, key, val)
        
        if getattr(self, "title", None) is not None and title is None:
            title = self.title

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
        convert_all_to_type(args, Series, Col)
        convert_all_to_type(args, DataFrame, HFrame)
        convert_all_to_type(args, set, Expr)

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        init_container(self, args,
            loc=None,
            title=title,
            tab_color=tab_color,
            # Dicts that must be passed to children
            cell_style = Style(**cell_style),
            header_style = Style(**header_style),
            table_style = Style(**table_style),
        )

        if sep is not None:
            insert_separator(self, sep)
    
    def move_kwargs_to_args(self, args: list, kwargs: dict) -> None:
        """
        Key -> header OR id
        Types:
            Cell
            Col
            pd.Series
        """
        keys_to_pop = []
        for key, val in kwargs.items():

            if isinstance(val, Cell):
                keys_to_pop.append(key)
                val.id = key
                args.append(val)

            elif get_dimensions(val) == 1:
                keys_to_pop.append(key)
                val.header = key
                args.append(val)

            elif isinstance(val, Series):
                keys_to_pop.append(key)
                args.append(Col(val, header=key))
            
            elif isinstance(val, DataFrame):
                keys_to_pop.append(key)
                args.append(HFrame(val, id=key))

        for key in keys_to_pop:
            kwargs.pop(key)

    def _write(self) -> None:

        if self.tab_color is not None:
            self.loc.ws.sheet_properties.tabColor = self.tab_color

        pass_dict_to_children(self, "cell_style")
        pass_dict_to_children(self, "header_style")
        pass_dict_to_children(self, "table_style")

        for elem in self:
            elem._write()
