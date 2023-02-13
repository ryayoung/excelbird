# External
from typing import Any

# Internal main
from excelbird._layout_references import Globals
from excelbird._base.dotdict import Style
from excelbird.styles import default_table_style
from excelbird._utils.util import (
    get_idx,
)
from excelbird._utils.argument_parsing import (
    combine_args_and_children_to_list,
    move_remaining_kwargs_to_dict,
)
from excelbird._utils.pass_attributes import (
    pass_dict_to_children,
)
# Internal core
from excelbird.core.gap import Gap
from excelbird.core.cell import Cell
from excelbird.core.series import Col, Row
from excelbird.core.frame import Frame, VFrame
from excelbird.core.stack import VStack, Stack
from excelbird.core.expression import Expr
from excelbird.core.function import Func


class Sheet(VStack):
    """
    Behaves similar to :class:`VStack` - it can hold any element, and arranges its children vertically - but
    lacks some styling features like margin and padding.

    * Direction: **vertical**
    * Child Type: :class:`Stack`, :class:`VStack`, :class:`Frame`, :class:`VFrame`, :class:`Col`, :class:`Row`, :class:`Cell`

    .. note:: If the first argument in ``*args`` is a string, it will be used as the ``title`` attribute. This allows for better readability in complex layouts with multiple sheets, so a sheet's title can be visible at the start of the container.

    Parameters
    ----------
    *args : Union[Stack, VStack, Frame, VFrame, Col, Row, Cell, list, tuple, str, int, float, pd.Series, pd.DataFrame, np.ndarray, Gap, Expr, Func, set]
        Can take any layout element (besides `Book` and `Sheet`) or any value that can
        be used to construct a layout element.
    children : list, optional
        Will be combined with args
    title : str, optional
        Sheet name
    sep : Gap or bool or int or dict, optional
        A sep in any excelbird layout element inserts a Gap between each of its children.
        If True, a default of Gap(1) is used. If int, Gap(sep) will be used. If a dict,
        ``Gap(1, **sep)`` will be used.
    tab_color : str, optional
        Hex color for tab color.
    end_gap : bool or int or dict or Gap, optional
        Applies a Gap to cells below and to the right of the Sheet. The Gap determines
        the number of columns filled, and 1/3 the number of rows filled. The default
        is Gap(35, fill_color="FFFFFF") (white). This means apply whitespace (hide grid)
        for 35 columns, and 105 rows surrounding the Sheet contents.
    isolate : bool, optional
        After initialization, clear the global memory of ids and headers, so references
        in future declared Sheets won't conflict with previous ones. This will also isolate
        previously declared Sheets, so they musn't reference elements declared after the current
        one.
    hidden : bool, optional
        Whether to hide the Sheet
    zoom : int, optional
        Percentage zoom level. (Passing None or 100 will have the same effect)
    background_color : str, optional
        Hex code for background_color. Will be applied to fill_color of any Gap child who hasn't
        specified its own fill_color, and to any child Stack/VStack's margins. Will also be passed
        down to any child (Cell excluded) who hasn't specified its own background_color.
    cell_style : dict, optional
        Applied to each child who has cell_style
    header_style : dict, optional
        Applied to each child who has header_style
    table_style : dict or bool, optional
        Applied to each child who has table_style
    **kwargs : Any
        Remaining kwargs will be applied to self.cell_style

    """

    _dimensions = -1

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
        children = combine_args_and_children_to_list(args, children)
        first_arg = get_idx(children, 0)
        if isinstance(first_arg, str):
            title = children.pop(0)

        children = [i for i in children if i is not None]

        # Alternative to init_from_same_dimension_type
        if len(children) == 1 and isinstance(first_arg, Sheet):
            children = list(first_arg)
            new_kwargs = first_arg.__dict__
            new_kwargs.pop("_loc")
            for key, val in new_kwargs.items():
                setattr(self, key, val)

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

        self._loc = None
        self.title = title
        self.tab_color = tab_color
        self.end_gap = end_gap
        self.isolate = isolate
        self.hidden = hidden
        self.zoom = zoom
        self.background_color = background_color
        # Dicts that must be passed to children
        self.cell_style = Style(**cell_style)
        self.header_style = Style(**header_style)
        self.table_style = Style(**table_style)

        self._init(children)

        if sep is not None:
            self._insert_separator(sep)

        if self.isolate is True:
            self._resolve_all_references()
            self._resolve_all_references()
            self._resolve_all_references()
            #     raise ExpressionResolutionError(
            #         "Couldn't resolve all expression references.\nThis error was raised during the "
            #         f"creation of sheet, '{self.title}'.\nWhen `isolate=True` for "
            #         "a sheet, it will try to resolve all of its expression references "
            #         "immediately after being created, and then clear the global memory of references "
            #         "so any element created afterwards won't be able to reference them."
            #     )
            Globals.clear_references()

    def _resolve_all_references(self) -> bool:
        Expr._set_use_ref_for_container_recursive(self)

        all_resolved = False
        attempts = 0
        while not all_resolved and attempts <= 5:
            all_resolved = True
            attempts += 1
            if Expr._resolve_container_recursive(self) is False:
                all_resolved = False
            if Func._resolve_container_recursive(self) is False:
                all_resolved = False

        return all_resolved

    def _apply_end_gap(self) -> None:
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

    def _resolve_gaps(self) -> None:
        super()._resolve_gaps()
        self._apply_end_gap()

    def _write(self) -> None:

        if self.tab_color is not None:
            self._loc.ws.sheet_properties.tabColor = self.tab_color

        if self.hidden is True:
            self._loc.ws.sheet_state = "hidden"

        if self.zoom is not None:
            self._loc.ws.sheet_view.zoomScale = self.zoom

        pass_dict_to_children(self, "cell_style")
        pass_dict_to_children(self, "header_style")
        pass_dict_to_children(self, "table_style")

        for elem in self:
            elem._write()

        if self.isolate is True:
            Globals.clear_references(self._loc.ws.title)
