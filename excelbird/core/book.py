"""
Detailed documentation and code examples coming soon.
"""
# External
from pandas import Series, DataFrame
import openpyxl as xl
from typing import Any
from copy import copy
import os

# Internal main
from excelbird._utils.util import (
    fill_frames,
    set_duplicate_objects_to_ref,
)
from excelbird._utils.argument_parsing import (
    combine_args_and_children_to_list,
    move_remaining_kwargs_to_dict,
)
from excelbird._utils.pass_attributes import (
    pass_dict_to_children,
    pass_attr_to_children,
)
from excelbird._utils.validation import (
    require_each_element_to_be_cls_type,
)
from excelbird.exceptions import (
    AutoOpenFileError,
    InvalidSheetName,
    ExpressionResolutionError,
    UnsavedWorkbookError,
)
from excelbird._layout_references import Globals
from excelbird.styles import default_table_style

from excelbird.core.expression import Expr
from excelbird.core.function import Func
from excelbird.core.item import Item
from excelbird.core.gap import Gap
from excelbird.core.cell import Cell
from excelbird.core.frame import _Frame, Frame
from excelbird.core.stack import _Stack, Stack
from excelbird.core.series import _Series, Col
from excelbird.core.sheet import Sheet

from excelbird._base.container import ListIndexableById
from excelbird._base.dotdict import Style
from excelbird._base.loc import Loc


class Book(ListIndexableById):
    """
    The outer-most parent container for a layout. Only `Book` has the ability to write
    to an Excel file.

    Call ``.write(path)`` to save to an Excel file.

    * Child Type: :class:`Sheet`

    Parameters
    ----------
    *args : Union[Sheet, Stack, VStack, Frame, VFrame, Col, Row, Cell, list, tuple, str, int, float, pd.Series, pd.DataFrame, np.ndarray, Gap, Expr, Func, set]
        Each element, if not a :class:`Sheet`, will be placed in its own separate `Sheet`.
        Vectors which aren't layout types (like `list`, or `pd.DataFrame`) will be inferred
        as :class:`Col` or :class:`Frame`
    children : list, optional
        Will be combined with args
    path : str, optional
        Path to write Book. Can be omitted and passed to ``.write()`` instead
    auto_open : bool, default False
        Attempt to automatically open after calling ``.write()``. If a file with the same name
        is already open, it will be closed first. Requires dependency, xlwings
    sep : Gap or bool or int or dict, optional
        A sep in any excelbird layout element inserts a Gap between each of its children.
        If True, a default of ``Gap(1)`` is used. If int, ``Gap(sep)`` will be used. If a dict,
        ``Gap(1, **sep)`` will be used.
    tab_color : str, optional
        Applied to each child Sheet
    end_gap : bool or int or dict or Gap, optional
        Applied to each child Sheet
    isolate : bool, optional
        Applied to each child Sheet
    zoom : int, optional
        Applied to each child Sheet
    cell_style : dict, optional
        Applied to each child Sheet
    header_style : dict, optional
        Applied to each child Sheet
    table_style : dict or bool, optional
        Applied to each child Sheet
    **kwargs :
        Remaining keyword arguments applied to ``cell_style``, to be passed down to children

    """

    _dimensions = -1

    elem_type = Sheet

    def __init__(
        self,
        *args: Any,
        children: list | None = None,
        path: str | None = None,
        auto_open: bool = False,
        sep: Any | None = None,
        tab_color: str | None = None,
        end_gap: bool | int | dict | Gap | None = None,
        isolate: bool | None = None,
        zoom: int | None = None,
        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        table_style: Style | dict | bool | None = None,
        **kwargs,
    ) -> None:
        children = combine_args_and_children_to_list(args, children)

        children = [i for i in children if i is not None]

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

        original_workbook = xl.Workbook()

        self.original_workbook = original_workbook
        self.wb = copy(original_workbook)
        self.path = path
        self.auto_open = auto_open
        # Attrs that must be passed to children
        self.tab_color = tab_color
        self.end_gap = end_gap
        self.isolate = isolate
        self.zoom = zoom
        # Dicts that must be passed to children
        self.cell_style = Style(**cell_style)
        self.header_style = Style(**header_style)
        self.table_style = Style(**table_style)

        self._init(children)

        if sep is not None:
            self._insert_separator(sep)

    def write(self, path: str | None = None) -> None:
        """
        Evaluates the layout tree and writes the completed layout to a ``.xlsx`` file.

        Parameters
        ----------
        path : str, optional
            Full path to the output file. Only exclude if `path` attribute
            has already been set.

        Notes
        -----

        **The algorithm, step by step**

        * First, all references inside each :class:`Expr <excelbird.Expr>` in the layout is resolved and evaluated
        * Now that the true size and shape of each layout element is known, spatial styling
          can be resolved

          * Margin and padding values are interpreted to create correctly sized :class:`Gap <excelbird.Gap>` spacing
          * Background colors are applied to the appropriate cells, drilling breadth-first through the tree.
          * Then, all `Gaps` are evaluated as correctly sized and styled layout elements.

        * Now that the layout structure, input data, and styling is complete

          * Traverse the tree and iteratevely assign a true sheet/column/row coordinate
            to each :class:`Cell <excelbird.Cell>` individually. Notice that *only* cells
            who were placed directly inside the `Book` get assigned a location. Later on,
            this lets us ensure that the formulas and cell references we create are valid.
          * Call each child's ``._write()`` method. Each layout element's write method will 
            safely pass down styling to its children, and then call each child's write method.

        * `Cells` which contain cell references don't know the value of their formula
          until their ``._write()`` is called. At this point, their expression is nothing
          more than a binary tree of references to other Python objects. When recursively expanding
          the tree to a formula string, we're able to tell whether a referenced `Cell` is actually
          being placed in the workbook or not, since unplaced `Cells` were never assigned locations.
          Therefore, we will always end up with a valid formula, because instead of trying to
          reference a non-existent cell, we take its value or formula and include it in
          our own.

        """
        if path is not None:
            self.path = path

        if self.path is None:
            raise ValueError("Workbook needs a path")

        require_each_element_to_be_cls_type(self)

        if self.auto_open == True:
            self._save_close_currently_open_excel_file()

        if self._resolve_all_references() is False:
            raise ExpressionResolutionError()

        pass_attr_to_children(self, "end_gap")

        self._validate_child_types()

        set_duplicate_objects_to_ref(self, [])

        for sheet in self:
            fill_frames(sheet)
            sheet._resolve_padding()
            sheet._resolve_margin()
            sheet._resolve_background_color()
            sheet._resolve_gaps()

        self._set_loc()

        pass_attr_to_children(self, "tab_color")
        pass_attr_to_children(self, "isolate")
        pass_attr_to_children(self, "zoom")
        pass_dict_to_children(self, "cell_style")
        pass_dict_to_children(self, "header_style")
        pass_dict_to_children(self, "table_style")

        for sheet in self:
            sheet._write()

        self.wb.save(self.path)
        print(f"Book '{self.path}' saved")
        if self.auto_open == True:
            self._open_excel_file()

        Globals.clear_references()
        Globals.clear_global_references()

    def _format_args(self, args: list) -> None:
        """
        Please refactor so that any element that isn't sheet or gap
        is simply passed to the Sheet constructor
        """

        Item._resolve_all_in_container(args, Sheet)

        elem_type = type(self).elem_type
        for i, elem in enumerate(args):
            if isinstance(elem, elem_type):
                continue

            if isinstance(elem, DataFrame):
                args[i] = elem_type(Frame(elem))

            elif isinstance(elem, Series):
                args[i] = elem_type(Col(elem))

            elif isinstance(elem, (_Series, _Frame, _Stack)):
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
                        args[i] = elem_type(Frame(*elem))
                    else:
                        args[i] = elem_type(Stack(*elem))

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

    def _validate_child_types(self) -> None:
        valid_types = (
            _Stack,
            _Frame,
            _Series,
            Cell,
            Gap,
        )
        type_names = [e.__name__ for e in valid_types]
        for elem in self:
            if not isinstance(elem, valid_types):
                raise TypeError(
                    f"At write time, a Book can only hold the following types:\n{type_names}"
                )
            if hasattr(elem, "_validate_child_types"):
                elem._validate_child_types()

    def _set_loc(self):
        for i, sheet in enumerate(self):
            if i == 0:
                ws = self.wb.active
            else:
                ws = self.wb.create_sheet(f"Sheet{i+1}")

            if sheet.title is None:
                sheet.title = f"Sheet{i+1}"

            invalid_sheet_name_chars = [":", "\\", "/", "?", "*", "[", "]"]
            if any(c in sheet.title for c in invalid_sheet_name_chars):
                raise InvalidSheetName(
                    f"Sheet name must not contain, {invalid_sheet_name_chars}"
                )

            ws.title = sheet.title
            sheet._set_loc(Loc((0, 0), ws))

    def __repr__(self):
        return ""

    def _save_close_currently_open_excel_file(self):
        if self.auto_open is True:
            xw = self._try_to_import_xlwings()
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
                    "An error was enountered while trying to save and close an already-open version of book, "
                    f"'{self.path}'. There are two likely causes of this issue: Either the workbook has unsaved changes, "
                    "or the file is stored in OneDrive, is currently open. To fix this, make sure the file doesn't have unsaved changes. "
                    "If the error persists, try closing the file first. If that doesn't work, move the file out of OneDrive, or set 'auto_open=False'. "
                    f'\nThis error was triggered by an `XlwingsError` being raised. Its message is:\n"{e}"'
                )

    def _open_excel_file(self):
        if self.auto_open is True:
            xw = self._try_to_import_xlwings()

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

    def _try_to_import_xlwings(self) -> None:
        try:
            import xlwings as xw

            return xw
        except Exception:
            raise ModuleNotFoundError(
                "The `auto_open` option uses the `xlwings` library to handle opening/closing "
                "Excel sessions. Please 'pip install xlwings' to continue, or set `auto_open=False`"
            )
