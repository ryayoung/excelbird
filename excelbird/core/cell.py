# External
import pandas as pd
import re
from pandas import Series
from typing import Any
from copy import copy, deepcopy
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.styles.colors import Color
from openpyxl.utils import FORMULAE
# Internal main
from excelbird.globals import Globals
from excelbird.base_types import HasId, HasBorder, Style, Loc, Gap
from excelbird.styles import formats
# ---------
from excelbird.colors import theme
# ---------
from excelbird.util import (
    autofit_algorithm,
    get_dimensions,
    remove_paren_enclosure,
    prefix_non_formulae_funcs,
)
from excelbird.color_algorithms import (
    color_is_light,
    get_alt_shade,
)
from excelbird.exceptions import AlreadyWrittenError, CellReferenceError
from excelbird.math import CanDoMath
from excelbird.expression import Expr
from excelbird.function import Func

cell_reference_warning_issued = False

class Cell(HasId, HasBorder, CanDoMath):
    dimensions = 0
    elem_type = None

    def __init__(self,
        value: Any | None = None,
        id: str | None = None,
        align_x: str | None = None,
        align_y: str | None = None,
        indent: float | None = None,
        center: bool | None = None,  # center align horizontal and vertical
        wrap: bool | None = None,
        size: int | None = None,  # font size
        bold: bool | None = None,
        italic: bool | None = None,
        color: str | None = None,
        num_fmt: str | None = None,
        currency: bool | None = None,
        ignore_format: bool | None = None,
        fill_color: str | None = None,
        auto_color_font: bool | str | None = None,
        auto_shade_font: bool | float | None = None,

        border_left: bool | str | None = None,
        border_right: bool | str | None = None,
        border_top: bool | str | None = None,
        border_bottom: bool | str | None = None,
        border: bool | str | None = None,  # MUST be last border attr set

        col_width: int | None = None,  # finds the cell's column and adjust it
        row_height: int | None = None,  # finds the cell's row and adjusts it
        merge: tuple[int, int] | None = None,  # (y, x) counts of how many merges. Ex: (0, 1) merges cell with right adjacent
        expr: list | None = None,
        func: list | None = None,
        autofit: bool | None = None,
        cell_style: dict | None = None,
    ) -> None:
        self.written = False
        self.loc = None

        self.value = value
        self.id = id
        self.align_x = align_x
        self.align_y = align_y
        self.indent = indent
        self.wrap = wrap
        self.size = size
        self.bold = bold
        self.italic = italic
        self.color = color
        self.num_fmt = num_fmt
        self.currency = currency
        self.ignore_format = ignore_format
        self.fill_color = fill_color
        self.auto_color_font = auto_color_font
        self.auto_shade_font = auto_shade_font
        self.col_width = col_width
        self.row_height = row_height
        self.merge = merge
        self.expr = expr
        self.func = func
        self.autofit = autofit
        self.center = center

        self.init_border(
            border,
            border_top,
            border_right,
            border_bottom,
            border_left,
        )
        self.inherit_style_without_override(cell_style)

        if isinstance(self.value, Cell):
            cell = self.value
            self.value = None
            new_dict = {
                k:v for k,v in cell.__dict__.items() if k not in ["_id", "loc"]
            }
            for key, val in new_dict.items():
                if getattr(self, key) is None:
                    setattr(self, key, val)

        elif isinstance(self.value, (Expr, Func)):
            raise ValueError(
                "Can't pass expression or function as a Cell's `value`. "
                "Instead, use the expression/function by itself, and pass any "
                "Cell styling as a dict to `cell_style`."
            )


    def _write(self) -> None:

        assert self.loc is not None, (
            "Excelbird developer error: Somehow, ._write() got called "
            "on a Cell that doesn't have a location. This is a serious issue!"
        )

        if self.written is True:
            raise AlreadyWrittenError(
                "Excelbird objects can only be written to a workbook once. This is "
                "because when `.write()` is called on a `Book`, the state of each of its elements "
                "changes: expressions are evaluated, series headers are inserted as actual cells, "
                "and cells with references are filled with the string locations of their references. "
                "\nSupport for repeated writes is possible, but hasn't been implemented yet."
            )

        if self.func is not None:
            self.value = "=" + self.func_value()
            self.value = self.value.replace(self.loc.title_str, "")

        if self.expr is not None:
            self.value = self.expr_value()
            if "UNKNOWN" not in self.value:
                self.value = "=" + self.value
            self.value = self.value.replace(self.loc.title_str, "")

        if self.value is None:
            return

        # Remove trailing commas
        if ", )" in str(self.value):
            self.value = re.sub(r"(, )(\))", r"\2", self.value)
        
        try:
            if pd.isnull(self.value):
                return
        except Exception:
            # Just making sure pd.isnull doesn't throw, if given a data type it doesn't like
            pass

        y, x = self.loc.y, self.loc.x
        cell = self.loc.cell
        cell.value = self.value

        def get_number_format():
            if self.ignore_format is True:
                return

            if isinstance(self.num_fmt, str):
                return self.num_fmt

            if isinstance(self.value, str):
                return

            if isinstance(self.value, float):
                if self.currency is True:
                    return formats.accounting_float
                return formats.comma_float

            if isinstance(self.value, int):
                if self.currency is True:
                    return formats.accounting_int
                return formats.comma_int

        number_format = get_number_format()
        if number_format is not None:
            cell.number_format = number_format

        align, font, fill, border = {}, {}, {}, {}

        if self.center is True:
            align["horizontal"] = 'center'
            align["vertical"] = 'center'

        if self.align_x is not None:
            align["horizontal"] = self.align_x
        if self.align_y is not None:
            align["vertical"] = self.align_y
        
        if isinstance(self.indent, (int, float)):
            align["indent"] = self.indent

        if self.wrap is not None:
            align["wrap_text"] = self.wrap

        if self.size is not None:
            font["size"] = self.size
        if self.bold is not None:
            font["bold"] = self.bold
        if self.italic is not None:
            font["italic"] = self.italic
        if self.color is not None:
            font["color"] = self.color
        else:
            if self.auto_color_font is True and isinstance(self.fill_color, str):
                if not color_is_light(self.fill_color):
                    font["color"] = "FFFFFF"  # white
            elif self.auto_shade_font is not None and isinstance(self.fill_color, str):
                if isinstance(self.auto_shade_font, float):
                    font["color"] = get_alt_shade(self.fill_color, self.auto_shade_font)
                else:
                    font["color"] = get_alt_shade(self.fill_color)

        if self.fill_color is not None:
            fill = {"patternType": "solid", "fgColor": Color(self.fill_color)}

        def get_border(border) -> dict:
            def get_side(side) -> Side:
                if side is None or side is False or side == (None, None) or side == (False, False):
                    return None
                assert isinstance(side, tuple), f"Internal developer error processing border. Border side value, {side} is invalid"
                if isinstance(side[0], str) and isinstance(side[1], str):
                    return Side(style=side[0], color=side[1])
                if isinstance(side[0], str):
                    return Side(style=side[0])
                if isinstance(side[1], str):
                    return Side(style=HasBorder.default_weight, color=side[1])
                raise ValueError(side)

            res = {}
            top, right, bottom, left = border
            if (side_top := get_side(top)) is not None:
                res["top"] = side_top
            if (side_right := get_side(right)) is not None:
                res["right"] = side_right
            if (side_bottom := get_side(bottom)) is not None:
                res["bottom"] = side_bottom
            if (side_left := get_side(left)) is not None:
                res["left"] = side_left
            return res

        border = get_border(self.border)

        if len(font) > 0:
            cell.font = Font(**font)
        if len(fill) > 0:
            cell.fill = PatternFill(**fill)
        if len(border) > 0:
            cell.border = Border(**border)
        if len(align) > 0:
            cell.alignment = Alignment(**align)

        if self.merge is not None:
            end_row = 1 + y + self.merge[0]
            end_column = 1 + x + self.merge[1]
            self.loc.ws.merge_cells(
                start_row=y + 1,
                start_column=x + 1,
                end_row=end_row,
                end_column=end_column,
            )

        if self.col_width is not None:
            self.loc.column_dimensions.width = self.col_width

        if self.autofit is True and self.col_width is None:
            curr = self.loc.column_dimensions.width
            new = autofit_algorithm(self.value)
            if new > curr:
                self.loc.column_dimensions.width = new

        if self.row_height is not None:
            self.loc.row_dimensions.height = self.row_height
        
        self.written = True

    def set_loc(self, loc: Loc) -> None:
        self.loc = loc

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def eval_func(self, func: list) -> str:

        def format_element(elem) -> str:
            if isinstance(elem, str):
                return elem

            if isinstance(elem, (int, float)):
                return str(elem)

            if get_dimensions(elem) > 0:
                cell_range = elem.range().expr
                evaluated = self.eval_expr(cell_range)
                return remove_paren_enclosure(evaluated)
            
            if elem.loc is not None:
                return elem.loc.full_str
            
            if elem.expr is not None:
                evaluated = self.eval_expr(elem.expr)
                return remove_paren_enclosure(evaluated)

            if elem.value is not None:
                return str(elem.value)  # Don't put quotes around strings here

        res = "".join([format_element(e) for e in func])
        res = prefix_non_formulae_funcs(res)
        return res
    
    def eval_expr(self, expr: list) -> str:

        def format_element(elem) -> str:
            if not isinstance(elem, Cell):
                return str(elem)
            
            if elem.loc is not None:
                return elem.loc.full_str
            
            if elem.expr is not None:
                return self.eval_expr(elem.expr)
            
            if elem.func is not None:
                return self.eval_func(elem.func)
            else:
                global cell_reference_warning_issued
            
                if elem.value is not None:
                    if cell_reference_warning_issued is False:
                        print(
                            "Warning: A cell in your book is trying to reference a cell which "
                            "won't be placed in the book. The missing cell's value has been applied "
                            "as a hardcoded value in the valid cell's expression."
                        )
                        cell_reference_warning_issued = True

                    if isinstance(elem.value, str):
                        quote_stripped_val = elem.value.strip('"')
                        return f'"{quote_stripped_val}"'
                    else:
                        return str(elem.value)
                
                if cell_reference_warning_issued is False and Globals.force_valid_references is False:
                    CellReferenceError.issue_warning()
                    cell_reference_warning_issued = True
                else:
                    raise CellReferenceError()

                return "UNKNOWN"

        res = [format_element(e) for e in expr]
        
        if len(res) > 2:
            res = ["("] + res + [")"]

        return "".join(res)

    def expr_value(self):
        if self.expr is None:
            return None
        expr = self.eval_expr(self.expr)
        return remove_paren_enclosure(expr)

    def func_value(self) -> str:
        if self.func is None:
            return None
        return self.eval_func(self.func)

    def ref(self, inherit_style: bool = False, **kwargs):
        if inherit_style is True:
            self_dict = deepcopy(self.__dict__)
            for key, val in self_dict.items():
                if key not in kwargs and key not in ["_id", "loc", "expr", "func"]:
                    kwargs[key] = val
        return Cell(expr=[self], **kwargs)

    def resolve_expressions(self):
        return True

    def resolve_gaps(self):
        pass

    def inherit_style_without_override(self, new_style: dict | Style | None) -> None:
        if new_style is not None:
            for key, val in new_style.items():
                check_unset = lambda x: x is None
                if key == "border":
                    check_unset = lambda x: x == [None, None, None, None]

                if check_unset(getattr(self, key, None)):
                    setattr(self, key, val)

    @property
    def shape(self) -> tuple:
        return tuple()
    
    @property
    def width(self) -> int:
        return 1
    
    @property
    def height(self) -> int:
        return 1
    
    @classmethod
    def explode_all_lists_tuples(cls, container: list) -> None:
        for i, elem in enumerate(container):
            if isinstance(elem, (list, tuple)):
                if all(
                    isinstance(i, (cls, str, int, float))
                    and not isinstance(i, Gap)
                    for i in elem
                ):
                    series = container.pop(i)
                    for value in reversed(series):
                        if isinstance(value, cls):
                            container.insert(i, value)
                        else:
                            container.insert(i, cls(value))
    
    @classmethod
    def convert_all_values(cls, container: list) -> None:
        for i, elem in enumerate(container):
            if isinstance(elem, (str, int, float)) and not isinstance(elem, (Gap, bool)):
                container[i] = cls(elem)
    
