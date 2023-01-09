# External
from pandas import Series, DataFrame
import openpyxl as xl
from typing import Any
from copy import copy
import os
# Internal main
from excelbird.exceptions import (
    AutoOpenFileError,
    InvalidSheetName,
    ExpressionResolutionError,
)
from excelbird.globals import global_ids
from excelbird.base_types import Style, Loc, ImpliedType, Gap, HasHelp
from excelbird.styles import default_table_style
from excelbird.util import (
    get_idx,
    combine_args_and_children_to_list,
    move_dict_args_to_other_dict,
    pass_dict_to_children,
    pass_attr_to_children,
    convert_all_to_type,
    init_container,
    init_from_same_dimension_type,
    move_remaining_kwargs_to_dict,
    require_each_element_to_be_cls_type,
    mark_all_cells_as_written_recursive,
)
from excelbird.expression import Expr
from excelbird.function import _DelayedFunc
# Internal core
from excelbird.core.cell import Cell
from excelbird.core.vec import _Vec, Col
from excelbird.core.frame import HFrame
from excelbird.core.stack import HStack
from excelbird.core.sheet import Sheet


class Book(list, HasHelp):
    """
Contains Sheets.

Call `.place()` to write contents to `path`.
    """

    elem_type = Sheet
    def __init__(
        self,
        *args: str | Sheet,
        children: list | None = None,
        wb: xl.Workbook | None = None,
        path: str | None = None,
        auto_open: bool = False,

        tab_color: str | None = None,

        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        table_style: Style | dict | bool | None = None,
        **kwargs,
    ) -> None:
        args = combine_args_and_children_to_list(args, children)
        if isinstance(get_idx(args, 0), str):
            path = args.pop(0)

        if cell_style is None: cell_style = dict()
        if header_style is None: header_style = dict()
        if table_style is None: table_style = dict()
        elif table_style is True: table_style = default_table_style

        move_dict_args_to_other_dict(args, cell_style)
        self.move_kwargs_to_args(args, kwargs)
        ImpliedType.resolve_all_in_container(args, Sheet)

        self.format_args(args)

        original_workbook = xl.Workbook()

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        init_container(self, args,
            original_workbook = original_workbook,
            wb = copy(original_workbook),
            path = path,
            auto_open = auto_open,
            # Attrs that must be passed to children
            tab_color = tab_color,
            # Dicts that must be passed to children
            cell_style = Style(**cell_style),
            header_style = Style(**header_style),
            table_style = Style(**table_style),
        )
    
    def format_args(self, args: list) -> None:
        """
        DataFrame -> Sheet(HFrame(data))
        Series, list -> Sheet(Col(data))
        _Vec -> Sheet(data)
        Gap(2) -> *[Sheet(), Sheet()]
        """
        elem_type = self.__class__.elem_type
        for i, elem in enumerate(args):
            if isinstance(elem, elem_type):
                continue

            if isinstance(elem, DataFrame):
                args[i] = elem_type(HFrame(elem))

            elif isinstance(elem, Series):
                args[i] = elem_type(Col(elem))

            elif isinstance(elem, _Vec):
                args[i] = elem_type(elem)
            
            elif isinstance(elem, Gap):
                gap = args.pop(i)
                for _ in range(gap):
                    args.insert(i, Sheet(**gap.kwargs))

            elif isinstance(elem, Cell):
                args[i] = elem_type(elem)
            
            elif isinstance(elem, (int, str, float)) and not isinstance(elem, Gap):
                args[i] = elem_type(Cell(elem))
            
            elif type(elem) in [list, tuple]:
                if len(elem) == 0:
                    args.pop(i)
                else:
                    if isinstance(elem[0], (Cell, int, str, float)):
                        args[i] = elem_type(Col(*elem))
                    elif isinstance(elem[0], (list, tuple, Series)):
                        args[i] = elem_type(HFrame(*elem))
                    else:
                        args[i] = elem_type(HStack(*elem))
    

    def move_kwargs_to_args(self, args: list, kwargs: dict) -> None:
        """
        Key -> title
        Types:
            Sheet
            I
        """
        elem_type = self.__class__.elem_type
        keys_to_pop = []
        for key, val in kwargs.items():
            if isinstance(val, elem_type):
                keys_to_pop.append(key)
                val.title = key
                args.append(val)
            
            elif isinstance(val, ImpliedType):
                keys_to_pop.append(key)
                new_sheet = val.astype(elem_type, title=key)
                args.append(new_sheet)
            
            elif isinstance(val, DataFrame):
                keys_to_pop.append(key)
                new_sheet = elem_type(HFrame(val), title=key)
                args.append(new_sheet)

            elif isinstance(val, Series):
                keys_to_pop.append(key)
                new_sheet = elem_type(Col(val), title=key)
                args.append(new_sheet)
            
            elif isinstance(val, (_Vec)):
                keys_to_pop.append(key)
                new_sheet = elem_type(val, title=key)
                args.append(new_sheet)
            
            elif isinstance(val, Cell):
                keys_to_pop.append(key)
                if isinstance(val, Cell):
                    new_sheet = elem_type(val, title=key)
                else:
                    new_sheet = elem_type(Cell(val), title=key)
                args.append(new_sheet)
            
            elif isinstance(val, Gap):
                keys_to_pop.append(key)
                if "title" in val.kwargs:
                    val.kwargs.pop("title")
                for i in range(val):
                    args.append(elem_type(title=key, **val.kwargs))
        
        for key in keys_to_pop:
            kwargs.pop(key)

    def write(self) -> None:
        if self.path is None:
            raise ValueError("Workbook needs a path")
        
        require_each_element_to_be_cls_type(self)

        if self.auto_open == True:
            self.save_close_currently_open_excel_file()

        Expr.set_use_ref_for_container_recursive(self)

        all_resolved = False
        attempts = 0
        while not all_resolved and attempts <= 30:
            all_resolved = True
            attempts += 1
            if Expr.resolve_container_recursive(self) is False:
                all_resolved = False
            if _DelayedFunc.resolve_container_recursive(self) is False:
                all_resolved = False

        if all_resolved is False:
            raise ExpressionResolutionError()
        elif attempts > 1:
            print(f"Took {attempts} attempts to resolve all expressions")

        for sheet in self:
            sheet.resolve_gaps()

        self.set_loc()

        pass_attr_to_children(self, "tab_color")
        pass_dict_to_children(self, "cell_style")
        pass_dict_to_children(self, "header_style")
        pass_dict_to_children(self, "table_style")

        for sheet in self:
            sheet._write()

        self.wb.save(self.path)
        print(f"Book '{self.path}' saved")
        if self.auto_open == True:
            self.open_excel_file()

        global global_ids
        global_ids = {}
    
    def set_loc(self):
        for i, sheet in enumerate(self):
            if i == 0:
                ws = self.wb.active
            else:
                ws = self.wb.create_sheet(f"Sheet{i+1}")

            if sheet.title is None:
                sheet.title = f"Sheet{i+1}"
            
            invalid_sheet_name_chars = [":", "\\", "/", "?", "*", "[", "]"]
            if any(c in sheet.title for c in invalid_sheet_name_chars):
                raise InvalidSheetName(f"Sheet name must not contain, {invalid_sheet_name_chars}")

            ws.title = sheet.title
            sheet.set_loc(Loc((0,0), ws))

    def __repr__(self):
        return ""
    

    def save_close_currently_open_excel_file(self):
        if self.auto_open is True:
            xw = self.try_to_import_xlwings()
            # Calling `xw.books` will raise error if excel is not already open
            # If excel isn't open, just call `xw.App`
            try:
                base_name = os.path.basename(self.path).lower()
                if base_name in xw.books:
                    book = xw.Book(self.path)
                    book.save()
                    book.close()
            except xw.XlwingsError as e:
                raise AutoOpenFileError(
                    "Couldn't access Excel file. A common cause of this issue is having your "
                    "file stored in OneDrive, AND it being currently open before executing your code. "
                    "To fix this, EITHER move the file out of OneDrive, OR close the file before code execution."
                    f'\nThis error was triggered by an `XlwingsError` being raised. Its message is:\n"{e}"'
                )
    
    def open_excel_file(self):
        if self.auto_open is True:
            xw = self.try_to_import_xlwings()
            try:
                print("Opening Book...")
                xw.Book(self.path)
            except xw.XlwingsError as e:
                raise AutoOpenFileError(
                    "Couldn't access Excel file. A common cause of this issue is having your "
                    "file stored in OneDrive, AND it being currently open before executing your code. "
                    "To fix this, EITHER move the file out of OneDrive, OR close the file before code execution."
                    f'\nThis error was triggered by an `XlwingsError` being raised. Its message is:\n"{e}"'
                )

    def try_to_import_xlwings(self) -> None:
        try:
            import xlwings as xw
            return xw
        except Exception:
            raise ModuleNotFoundError(
                "The `auto_open` option uses the `xlwings` library to handle opening/closing "
                "Excel sessions. Please 'pip install xlwings' to continue, or set `auto_open=False`"
            )