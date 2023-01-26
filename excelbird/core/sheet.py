# External
from pandas import Series, DataFrame
from typing import Any

# Internal main
from excelbird.globals import Globals
from excelbird.exceptions import ExpressionResolutionError
from excelbird.expression import Expr
from excelbird.function import Func
from excelbird.base_types import Style, ImpliedType, Gap, Loc
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
from excelbird.core.vec import Col, Row
from excelbird.core.frame import Frame, VFrame
from excelbird.core.stack import VStack, Stack


class Sheet(VStack):
    """

    Parameters
    ----------
    *args: Any
        Can take any layout element (besides Book and Sheet) or any value that can
        be used to construct a layout element. NOTE: If the first element is a string,
        it will be used the Sheet's title to allow for better readability.
    children: list, default None
        Will be combined with *args
    title: str, default None
        Sheet name
    sep: Gap | bool | int | dict, default None
        A sep in any excelbird layout element inserts a Gap between each of its children.
        If True, a default of Gap(1) is used. If int, Gap(sep) will be used. If a dict,
        Gap(1, **sep) will be used.
    tab_color: str, default None
        Hex color for tab color.
    end_gap: bool | int | dict | Gap, default None
        Applies a Gap to cells below and to the right of the Sheet. The Gap determines
        the number of columns filled, and 1/3 the number of rows filled. The default
        is Gap(35, fill_color="FFFFFF") (white). This means apply whitespace (hide grid)
        for 35 columns, and 105 rows surrounding the Sheet contents.
    isolate: bool, default None
        After initialization, clear the global memory of ids and headers, so references
        in future declared Sheets won't conflict with previous ones. This will also isolate
        previously declared Sheets, so they musn't reference elements declared after the current
        one.
    hidden: bool, default None
        Whether to hide the Sheet
    zoom: int, default None
        Percentage zoom level. (Passing None or 100 will have the same effect)
    background_color: str, default None
        Hex code for background_color. Will be applied to fill_color of any Gap child who hasn't
        specified its own fill_color, and to any child Stack/VStack's margins. Will also be passed
        down to any child (Cell excluded) who hasn't specified its own background_color.
    cell_style: dict, default None
        Applied to each child who has cell_style
    header_style: dict, default None
        Applied to each child who has header_style
    table_style: dict | bool, default None
        Applied to each child who has table_style
    **kwargs Any
        Remaining kwargs will be applied to self.cell_style
    """

    dimensions = -1

    def __init__(
        self,
        *args: Any,
        children: list | None = None,
        title: str | None = None,
        sep: Any | None = None,
        tab_color: str | None = None,
        end_gap: bool | int | dict | Gap | None = None,
        isolate: bool | None = None,
        hidden: bool | None = None,
        zoom: int | None = None,
        background_color: str | None = None,
        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        table_style: Style | dict | bool | None = None,
        **kwargs,
    ) -> None:
        args = combine_args_and_children_to_list(args, children)
        first_arg = get_idx(args, 0)
        if isinstance(first_arg, str):
            title = args.pop(0)

        args = [i for i in args if i is not None]

        # Alternative to init_from_same_dimension_type
        if len(args) == 1 and isinstance(first_arg, Sheet):
            args = list(first_arg)
            new_kwargs = first_arg.__dict__
            new_kwargs.pop("loc")
            for key, val in new_kwargs.items():
                setattr(self, key, val)

        if cell_style is None:
            cell_style = dict()
        if header_style is None:
            header_style = dict()
        if table_style is None:
            table_style = dict()
        elif table_style is True:
            table_style = default_table_style

        move_dict_args_to_other_dict(args, cell_style)
        Cell.convert_all_values(args)

        frame_type = self.__class__.elem_type
        vec_type = frame_type.elem_type
        ImpliedType.resolve_all_in_container(args, frame_type)
        self.format_args(args)

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        init_container(
            self,
            args,
            loc=None,
            title=title,
            tab_color=tab_color,
            end_gap=end_gap,
            isolate=isolate,
            hidden=hidden,
            zoom=zoom,
            background_color=background_color,
            # Dicts that must be passed to children
            cell_style=Style(**cell_style),
            header_style=Style(**header_style),
            table_style=Style(**table_style),
        )

        if sep is not None:
            insert_separator(self, sep)

        if self.isolate is True:
            self.resolve_all_references()
            self.resolve_all_references()
            self.resolve_all_references()
            #     raise ExpressionResolutionError(
            #         "Couldn't resolve all expression references.\nThis error was raised during the "
            #         f"creation of sheet, '{self.title}'.\nWhen `isolate=True` for "
            #         "a sheet, it will try to resolve all of its expression references "
            #         "immediately after being created, and then clear the global memory of references "
            #         "so any element created afterwards won't be able to reference them."
            #     )
            Globals.clear_references()

    def format_args(self, args: list) -> None:
        convert_all_to_type(args, Series, Col)
        convert_all_to_type(args, DataFrame, Frame)
        convert_all_to_type(args, set, Expr)

    def resolve_all_references(self) -> bool:
        Expr.set_use_ref_for_container_recursive(self)

        all_resolved = False
        attempts = 0
        while not all_resolved and attempts <= 5:
            all_resolved = True
            attempts += 1
            if Expr.resolve_container_recursive(self) is False:
                all_resolved = False
            if Func.resolve_container_recursive(self) is False:
                all_resolved = False

        return all_resolved

    def apply_end_gap(self) -> None:
        gap = self.end_gap
        if gap is None or gap is False:
            return

        if (
            not type(gap) in [bool, int]
            and not isinstance(gap, Gap)
            and not isinstance(gap, dict)
        ):
            raise ValueError("end_gap must be bool, int, Gap, dict")

        default_size = 35
        # default_color = "FFFFFF"  # white

        if gap is True:
            gap = Gap(default_size)
        elif type(gap) == int:
            gap = Gap(gap)
        elif isinstance(gap, dict):
            if "size" in gap:
                gap = Gap(gap.pop("size"), **gap)
            else:
                gap = Gap(default_size, **gap)

        if "fill_color" not in gap.kwargs and self.background_color is not None:
            gap.kwargs["fill_color"] = self.background_color

        if "row_multiplier" not in gap.kwargs:
            gap.kwargs["row_multiplier"] = 3

        size, kwargs = int(gap), gap.kwargs
        row_multiplier = kwargs.pop("row_multiplier")
        width, height = self.width, self.height
        new_elements = []
        for i, elem in reversed(list(enumerate(self))):
            new_elements.insert(0, self.pop(i))
        new_cols = size
        new_rows = size * row_multiplier
        full_height = height + new_rows
        self.append(
            Stack(
                VStack(
                    *new_elements,
                    VFrame(
                        *[
                            Row(*[Cell("", **kwargs) for _ in range(width)])
                            for _ in range(new_rows)
                        ]
                    ),
                ),
                Frame(
                    *[
                        Col(*[Cell("", **kwargs) for _ in range(full_height)])
                        for _ in range(new_cols)
                    ]
                ),
            )
        )

    def resolve_gaps(self) -> None:
        super().resolve_gaps()
        self.apply_end_gap()

    def _write(self) -> None:

        if self.tab_color is not None:
            self.loc.ws.sheet_properties.tabColor = self.tab_color

        if self.hidden is True:
            self.loc.ws.sheet_state = "hidden"

        if self.zoom is not None:
            self.loc.ws.sheet_view.zoomScale = self.zoom

        pass_dict_to_children(self, "cell_style")
        pass_dict_to_children(self, "header_style")
        pass_dict_to_children(self, "table_style")

        for elem in self:
            elem._write()

        if self.isolate is True:
            Globals.clear_references(self.loc.ws.title)
