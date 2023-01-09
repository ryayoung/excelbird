# External
from pandas import Series, DataFrame
from typing import Any, Iterable
import re
# Internal main
from excelbird.styles import default_table_style
from excelbird.base_types import Gap, Style, Loc, ImpliedType
from excelbird.util import (
    combine_args_and_children_to_list,
    move_dict_args_to_other_dict,
    get_idx,
    pass_dict_to_children,
    convert_all_to_type,
    init_container,
    init_from_same_dimension_type,
    move_remaining_kwargs_to_dict,
    require_each_element_to_be_cls_type,
    convert_sibling_types,
    ensure_value_is_not_number,
    insert_separator,
)
from excelbird.expression import Expr
from excelbird.function import _DelayedFunc
# Internal core
from excelbird.core.cell import Cell
from excelbird.core.vec import (
    _Vec,
    Col,
    Row,
    _HorizontalVec,
    _VerticalVec,
)

class _Frame(_Vec):
    dimensions = 2
    elem_type = _Vec

    def __init__(
        self,
        *args: Any,
        children: list | None = None,
        id: str | int | None = None,
        schema: None = None,
        sep: Any | None = None,
        border_top: bool | str | None = None,
        border_right: bool | str | None = None,
        border_bottom: bool | str | None = None,
        border_left: bool | str | None = None,
        border: bool | str | Iterable | None = None,

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
        self.explode_all_dataframes(args)

        vec_type = self.__class__.elem_type
        convert_all_to_type(args, Series, vec_type)
        convert_all_to_type(args, set, Expr)
        ImpliedType.resolve_all_in_container(args, vec_type)
        convert_sibling_types(self, args)

        move_remaining_kwargs_to_dict(kwargs, cell_style)

        init_container(self, args,
            loc = None,
            id = id,
            schema = schema,
            header_style = Style(**header_style),
            table_style = Style(**table_style),
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
        if sep is not None:
            insert_separator(self, sep)
    
    def move_kwargs_to_args(self, args: list, kwargs: dict) -> None:
        """
        Key -> header
        Types:
            set,
            elem_type,
            Series,
            Expr,
            _DelayedFunc
        """
        vec_type = self.__class__.elem_type
        keys_to_pop = []
        for key, val in kwargs.items():

            if isinstance(val, set):
                if len(val) == 1:
                    keys_to_pop.append(key)
                    args.append(Expr(val.pop(), header=key))

            elif isinstance(val, (vec_type, Expr, _DelayedFunc)):
                keys_to_pop.append(key)
                val.header = key
                args.append(val)

            elif isinstance(val, Series):
                keys_to_pop.append(key)
                args.append(vec_type(val, header=key))

            elif isinstance(val, ImpliedType):
                keys_to_pop.append(key)
                new_vec = val.astype(vec_type, header=key)
                args.append(new_vec)

        for key in keys_to_pop:
            kwargs.pop(key)
    
    def explode_all_dataframes(self, args: list) -> None:
        """
        Explodes each dataframe in self or args to separate vecs

        Mutates inplace: `container`
        """
        for i, elem in enumerate(args):
            if isinstance(elem, DataFrame):
                df = args.pop(i)
                for col in reversed(df.columns):
                    args.insert(i, self.__class__.elem_type(df[col]))

    def key_to_idx(self, key: str | int) -> int:
        try:
            return super().key_to_idx(key)
        except (KeyError, IndexError):
            headers = [i.header if hasattr(i, "_header") else None for i in self]
            if key in headers:
                return headers.index(key)

            raise KeyError(f"Invalid key, {key}")

    def _write(self) -> None:
        require_each_element_to_be_cls_type(self)
        self.apply_border()
        # Safely set each style to the element's header style, if it hasn't already
        # been set.
        pass_dict_to_children(self, "header_style")
        pass_dict_to_children(self, "cell_style")

        for elem in self:
            # If a schema has been declared, check if the
            # value of the first cell is present in the schema. If it is,
            # replace the value with its output label in the schema
            if self.schema is not None:
                if len(elem) != 0:
                    schema_var = self.schema.get(elem.header)
                    if schema_var is not None:
                        elem.header = schema_var.output

            elem._write()

    @property
    def shape(self) -> tuple[int,int]:
        return (
            max([v.shape[0] for v in self if hasattr(v, "shape")] + [0]),
            sum([1 if not isinstance(i, Gap) else i for i in self]),
        )

    def resolve_gaps(self) -> None:
        Gap.explode_all_to_vecs(self, self.__class__.elem_type, self.gap_size)
        for elem in self:
            elem.resolve_gaps()
    


class VFrame(_Frame, _VerticalVec):
    sibling_type = None # these are set after class declaration
    elem_type = Row

    @property
    def width(self) -> int:
        return self.shape[0]

    @property
    def height(self) -> int:
        return self.shape[1]
    
    @property
    def gap_size(self) -> int:
        return self.width


class HFrame(_Frame, _HorizontalVec):
    sibling_type = None # these are set after class declaration
    elem_type = Col

    def _write(self) -> None:
        if len(self.table_style) > 0:
            self.format_headers_for_table_format()

        super()._write()

        if len(self.table_style) > 0:
            table_location = self.range().expr_value()
            self.apply_table_format_to_worksheet()

    def format_headers_for_table_format(self) -> None:
        """
        To apply excel table format, all column headers must be strings,
        with no duplicates.

        1. Ensure all headers are strings. Throw error otherwise
        2. Add headers where missing:
            ('foo', None, 'bar', None) -> ('foo', 'Unnamed', 'bar', 'Unnamed2')
        3. Append counter to duplicate headers:
            ('a', 'b', 'b', 'b') -> ('a', 'b', 'b2', 'b3')

        Mutates inplace: `self`
        """
        for i, vec in enumerate(self):
            if vec.header is None:
                vec.header = f"Unnamed"
            else:
                ensure_value_is_not_number(vec.header)

        header_counts = dict()
        for i, vec in enumerate(self):
            if vec.header in header_counts:
                header_counts[vec.header] += 1
            else:
                header_counts[vec.header] = 1

        header_counts = {k: v for k, v in header_counts.items() if v > 1}

        for header in header_counts.keys():
            columns = [i for i in self if i.header == header]
            for i, col in enumerate(columns):
                if i > 0:
                    col.header += str(i + 1)
    
    def apply_table_format_to_worksheet(self):
        """
        NOTE: THIS WILL FAIL IF HEADERS ARE REFERENCES FROM
        A DIFFERENT SHEET. To fix:
            Check for "!" in header names. If found, trace the
            cell_range expression back to the original cells and
            copy their values


        Formats self's cell range in worksheet as excel table

        Mutates inplace:
            `self.loc.ws`
            `self.table_style`
        """

        import openpyxl.worksheet.table as xl_tbl
        style = self.table_style
        cell_range = self.range().expr_value().replace(self.loc.title_str, "")
        ws = self.loc.ws

        if "displayName" in style:
            name = style.pop("displayName")
        else:
            name = "Table1"

        valid_table_name = True
        valid_table_name, attempts = False, 0
        while valid_table_name is False and attempts < 3:
            attempts += 1
            try:
                table = xl_tbl.Table(displayName=name, ref=cell_range)
                table.tableStyleInfo = xl_tbl.TableStyleInfo(**style)
                ws.add_table(table)
                valid_table_name = True
            except ValueError as e:
                name_and_num = re.search(r"(.+)(\d+)", name)
                if name_and_num is None:
                    name += "1"
                else:
                    label, num = name_and_num.groups()
                    name = f"{label}{int(num)+1}"

        if valid_table_name is False:
            print("Error when formatting table")

    @property
    def width(self) -> int:
        return self.shape[1]

    @property
    def height(self) -> int:
        return self.shape[0]
    
    @property
    def gap_size(self) -> int:
        return self.height


VFrame.sibling_type = HFrame
HFrame.sibling_type = VFrame
