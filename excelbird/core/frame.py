# External
from pandas import Series, DataFrame, concat
from typing import Any, Iterable
from copy import deepcopy
import re

from excelbird.styles.styles import default_table_style
from excelbird._base.container import ListIndexableById
from excelbird._base.identifier import HasId
from excelbird._base.styling import HasBorder
from excelbird.core.item import Item
from excelbird._base.dotdict import Style
from excelbird._base.loc import Loc
from excelbird._base.math import CanDoMath, elem_math

from excelbird._utils.util import (
    get_dimensions,
    init_from_same_dimension_type,
)
from excelbird._utils.argument_parsing import (
    combine_args_and_children_to_list,
    convert_all_to_type,
    move_remaining_kwargs_to_dict,
    convert_sibling_types,
)

from excelbird._utils.pass_attributes import (
    pass_dict_to_children,
)
from excelbird._utils.validation import (
    require_each_element_to_be_cls_type,
    ensure_value_is_not_number,
)

from excelbird.core.expression import Expr

from excelbird.core.gap import Gap
from excelbird.core.series import (
    _Series,
    Col,
    Row,
)


class _Frame(CanDoMath, ListIndexableById, HasId, HasBorder):
    _dimensions = 2
    elem_type = _Series

    def __init__(
        self,
        *args: Any,
        children: list | None = None,
        id: str | int | None = None,
        schema: None = None,
        sep: Any | None = None,
        sizes: list | None = None,
        border_top: bool | str | None = None,
        border_right: bool | str | None = None,
        border_bottom: bool | str | None = None,
        border_left: bool | str | None = None,
        border: bool | str | Iterable | None = None,
        background_color: str | None = None,
        fill_empty: bool | None = None,
        cell_style: Style | dict | None = None,
        header_style: Style | dict | None = None,
        table_style: Style | dict | bool | None = None,
        **kwargs,
    ) -> None:
        children = combine_args_and_children_to_list(args, children)

        children = [i for i in children if i is not None]

        children = init_from_same_dimension_type(self, children)
        if getattr(self, "_id", None) is not None and id is None:
            id = self.id

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

        self.loc = None
        self.id = id
        self.schema = schema
        self.sizes = sizes
        self.background_color = background_color
        self.fill_empty = fill_empty
        self.header_style = Style(**header_style)
        self.table_style = Style(**table_style)
        # Dicts that must be passed to children
        self.cell_style = Style(**cell_style)

        self._init(children)

        self.init_border(
            border,
            border_top,
            border_right,
            border_bottom,
            border_left,
        )
        if sep is not None:
            self._insert_separator(sep)

    @property
    def shape(self) -> tuple[int, int]:
        return (
            max([v.shape[0] for v in self if hasattr(v, "shape")] + [0]),
            sum([1 if not isinstance(i, Gap) else i for i in self]),
        )

    @property
    def headers(self) -> list:
        return [i.header if hasattr(i, "_header") else None for i in self]

    def range(self, include_headers: bool = False):

        if self[0].header_written is True and include_headers is False:
            first = self[0][1]
        else:
            first = self[0][0]

        last = self[-1][-1]
        return first >> last

    def ref(self, inherit_style: bool = False, **kwargs):
        new_elements = [
            i.ref(inherit_style=inherit_style, **kwargs)
            if not isinstance(i, Gap)
            else deepcopy(i)
            for i in self
        ]
        new_dict = kwargs
        if inherit_style is True:
            self_dict = deepcopy(self.__dict__)
            for key, val in self_dict.items():
                if key == "_header":
                    key = "header"
                if key not in new_dict and key not in ["_id", "loc"]:
                    new_dict[key] = val
        return type(self)(*new_elements, **new_dict)

    def astype(self, other: type, **kwargs):
        elements = list(self)
        new = other(*elements)
        for key, val in self.__dict__.items():
            if key == "_header":
                key = "header"
            if key != "_id":
                setattr(new, key, val)
        for key, val in kwargs.items():
            setattr(new, key, val)
        return new

    def _format_args(self, args: list) -> None:
        self._explode_all_dataframes(args)
        convert_all_to_type(args, Series, type(self).elem_type)
        convert_all_to_type(args, set, Expr)
        Item._resolve_all_in_container(args, type(self).elem_type)
        convert_sibling_types(self, args)

    def _explode_all_dataframes(self, args: list) -> None:
        for i, elem in enumerate(args):
            if isinstance(elem, DataFrame):
                df = args.pop(i)
                for col in reversed(df.columns):
                    args.insert(i, type(self).elem_type(df[col]))

    def _resolve_background_color(self) -> None:
        for elem in self:
            if hasattr(elem, "_resolve_background_color"):
                if (
                    self.background_color not in [None, False]
                    and elem.background_color is None
                ):
                    elem.background_color = self.background_color
                elem._resolve_background_color()

        if self.background_color not in [None, False]:
            for elem in self:
                if isinstance(elem, Gap):
                    if "fill_color" not in elem.kwargs:
                        elem.fill = True
                        elem.kwargs["fill_color"] = self.background_color

    def _key_to_idx(self, key: str | int) -> int:
        try:
            return super()._key_to_idx(key)
        except (KeyError, IndexError):
            if key in self.headers:
                return self.headers.index(key)

            raise KeyError(f"Invalid key, {key}")

    def __getitem__(self, key):
        if not isinstance(key, list):
            # return super().__getitem__(key)
            return ListIndexableById.__getitem__(self, key)

        new_elements = [self[self._key_to_idx(k)] for k in key]
        new_dict = {k: v for k, v in self.__dict__.items() if k not in ["_id", "loc"]}
        if "_header" in new_dict:
            new_dict["header"] = new_dict.pop("_header")

        return type(self)(*new_elements, **new_dict)

    def _set_loc(self, loc: Loc) -> None:
        self.loc = loc

        offset = self._starting_offset()
        for elem in self:
            elem._set_loc(
                Loc((self.loc.y + offset.y, self.loc.x + offset.x), self.loc.ws)
            )
            offset = self._inc_offset(offset, elem)

    def _apply_sizes(self) -> None:
        def set_elem_size(elem, size):
            if not isinstance(elem, (Col, Row)):
                return
            attr = "col_width" if isinstance(elem, Col) else "row_height"

            elem.cell_style[attr] = size
            if elem.header is not None:
                elem.header_style[attr] = size

        if isinstance(self.sizes, (list, tuple)):
            for elem, size in zip(self, self.sizes):
                set_elem_size(elem, size)

        elif isinstance(self.sizes, dict):
            for key, val in self.sizes.items():
                elem = self.get(key)
                if elem is not None:
                    set_elem_size(elem, val)

    def _validate_child_types(self) -> None:
        cls_name = type(self).__name__
        elem_type_name = type(self).elem_type.__name__
        valid_types = (
            type(self).elem_type,
            Gap,
        )
        for elem in self:
            if not isinstance(elem, valid_types):
                raise TypeError(
                    f"At write time, a {cls_name} can only hold {elem_type_name}s or Gaps. "
                    "To arrange mixed types, place them in a Stack or VStack"
                )
            if hasattr(elem, "_validate_child_types"):
                elem._validate_child_types()

    def _write(self) -> None:
        require_each_element_to_be_cls_type(self)
        self._apply_border()

        # Safely set each style to the element's header style, if it hasn't already
        # been set.
        pass_dict_to_children(self, "header_style")
        pass_dict_to_children(self, "cell_style")

        self._apply_sizes()

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

    def _resolve_gaps(self) -> None:
        Gap._explode_all_to_series(self, type(self).elem_type, self._gap_size)
        for elem in self:
            if hasattr(elem, "_resolve_gaps"):
                elem._resolve_gaps()

    def __rshift__(self, other):
        if get_dimensions(other) < get_dimensions(self):
            return elem_math(self[0], other, lambda a, b: a >> b, " >> ")
        return self[0] >> other[-1]

    def __rrshift__(self, other):
        if get_dimensions(other) < get_dimensions(self):
            return elem_math(other, self[-1], lambda a, b: a >> b, " >> ")
        return other[0] >> self[-1]


class Frame(_Frame):
    """
    A 2-dimensional vector that holds 1-dimensional vectors. Frame holds Col, and arranges its
    children horizontally. VFrame holds Row, and arranges its children vertically. Only Frame
    can be formatted as an Excel table.

    Frame and VFrame can be used in a python expression with any other layout element with equal or
    or lower number of dimensions. See the math module for further explanation.

    * Direction: **horizontal**
    * Child Type: ``Col``

    Parameters
    ----------
    \*args: `Any`
        Children must be (or resolve to) a series. Frame holds Cols, and VFrame
        holds Rows - ``Gap`` and ``Item`` will be interpreted as the respective element. Can also
        take any value that will be resolved to one of the above types, such as a list, tuple,
        pandas Series, etc. 2-dimensional arguments, such as pandas DataFrame, will be 'exploded'
        inplace into separate 1-dimensional elements.
    children: *list, default None*
        Will be combined with args
    id: *str, default None*
        Unique identifier to store globally so that this element can be referenced
        elsewhere in the layout without being assigned to a variable
    schema: *Schema, default None*
        A Schema object to use to rename child headers to desired output names at write time.
    sep: *Gap | bool | int | dict, default None*
        A sep in any excelbird layout element inserts a Gap between each of its children.
        If True, a default of Gap(1) is used. If int, Gap(sep) will be used. If a dict,
        ``Gap(1, **sep)`` will be used.
    sizes: *dict[str, int], default None*
        Specify the column width (or row height, if VFrame) for any child element by header.
        Keys should be the header of a child element, and values should be integers representing
        that element's size. Note: unlike most excelbird styling, this argument will override any
        other column widths / row heights given to the children.
    background_color: *str, default None*
        Hex code for background color. Will be applied to fill_color of any Gap child who hasn't specified its own
        fill_color. Will also be passed down to any Col/Row child who hasn't specified its own background_color.
    fill_empty: *bool, default None*
        Fill shorter children (if children vary in length) with `Cell("")` so that all lengths are matching,
        and all Cells inside the child will follow the same style. If False or None, these empty spaces will instead
        be filled with `Gap()`, to which the child's background_color will be applied, if present.
    cell_style: *dict, default None*
        Will be applied to each child's cell_style
    header_style: *dict, default None*
        Will be applied to each child's header_style
    table_style: *dict | bool, default None*
        Format a Frame as an Excel table. (ignored for VFrame). If True, default style
        'name="TableStyleMedium2"' is used. If dict, key 'displayName' will be used as the
        table name, and all other key/values will be passed to openpyxl.worksheet.table.TableStyleInfo.
    border: *list[tuple | str | bool] | tuple[str | bool, str | bool] | str | bool, default None*
        Syntax inspired by CSS. A non-list value will be applied to all 4 sides. If list,
        length can be 2, 3, or 4 elements. Order is [top, right, bottom, left]. If length 2,
        apply the first element to top and bottom border, and apply the second element to right and left.
        To apply border to children instead, use cell_style.
    border_top: *tuple[str | bool, str | bool] | str | bool, default None*
        Top border. If True, a thin black border is used. If string (6 char hex code),
        use the default weight and apply the specified color. If string (valid weight name),
        use the default color and apply the specified weight. If tuple, apply the first
        element as weight, and second element as color.
    border_right: *tuple[str | bool, str | bool] | str | bool, default None*
        Right border. See border_top
    border_bottom: *tuple[str | bool, str | bool] | str | bool, default None*
        Bottom border. See border_top
    border_left: *tuple[str | bool, str | bool] | str | bool, default None*
        Left border. See border_top
    \*\*kwargs:
        Remaining kwargs will be applied to cell_style

    """

    sibling_type = None  # these are set after class declaration
    elem_type = Col

    @property
    def width(self) -> int:
        return self.shape[1]

    @property
    def height(self) -> int:
        return self.shape[0]

    def _write(self) -> None:
        if len(self.table_style) > 0:
            self._format_headers_for_table_format()

        super()._write()

        if len(self.table_style) > 0:
            self._apply_table_format_to_worksheet()

    def _format_headers_for_table_format(self) -> None:
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
        for i, series in enumerate(self):
            if series.header is None:
                series.header = f"Unnamed"
            else:
                ensure_value_is_not_number(series.header)

        header_counts = dict()
        for i, series in enumerate(self):
            if series.header in header_counts:
                header_counts[series.header] += 1
            else:
                header_counts[series.header] = 1

        header_counts = {k: v for k, v in header_counts.items() if v > 1}

        for header in header_counts.keys():
            columns = [i for i in self if i.header == header]
            for i, col in enumerate(columns):
                if i > 0:
                    col.header += str(i + 1)

    def _apply_table_format_to_worksheet(self):
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
        cell_range = (
            self.range(include_headers=True)
            .expr_value()
            .replace(self.loc.title_str, "")
        )
        ws = self.loc.ws

        if "displayName" in style:
            name = style.pop("displayName")
        else:
            if isinstance(ws.title, str):
                friendly_title = re.sub(r"[^A-Za-z]", "", ws.title)
                name = friendly_title + "Table1"
            else:
                name = "Table1"

        valid_table_name = True
        valid_table_name, attempts = False, 0
        err_msg = ""
        while valid_table_name is False and attempts < 30:
            attempts += 1
            try:
                table = xl_tbl.Table(displayName=name, ref=cell_range)
                table.tableStyleInfo = xl_tbl.TableStyleInfo(**style)
                ws.add_table(table)
                valid_table_name = True
            except Exception as e:
                err_msg = e
                name_and_num = re.search(r"(.+)(\d+)", name)
                if name_and_num is None:
                    name += "1"
                else:
                    label, num = name_and_num.groups()
                    name = f"{label}{int(num)+1}"

        if valid_table_name is False:
            raise ValueError(
                f"Couldn't properly format table on sheet, '{ws.title}', cell range '{cell_range}'."
                "This is either due to invalid data formatting, or a duplicate table name. Here is the "
                f"error message from openpyxl:\n{err_msg}"
            )

    @property
    def _gap_size(self) -> int:
        return self.height

    def _repr_html_(self):
        elements = [
            Series(
                list(e) + [""],
                name=e.header if getattr(e, "_header", None) is not None else "",
            )
            for e in self
        ]

        return (
            concat(elements, axis=1).fillna("").style.hide(axis="index")._repr_html_()
        )

    def _border_mask(self, top, right, bottom, left) -> Style:
        return Style(
            first=[top, False, bottom, left],
            last=[top, right, bottom, False],
            middle=[top, False, bottom, False],
        )

    @staticmethod
    def _inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.x += elem.width
        return offset

    def _starting_offset(self) -> Loc:
        offset = Loc((0, 0), self.loc.ws)
        if getattr(self, "_header", None) is not None:
            offset.x += 1
        return offset


class VFrame(_Frame):
    """

    The vertically-arranged sibling to ``Frame``

    Excel doesn't support table formatting for vertical tables

    * Direction: **vertical**
    * Child Type: ``Row``

    """

    sibling_type = None  # these are set after class declaration
    elem_type = Row

    @property
    def width(self) -> int:
        return self.shape[0]

    @property
    def height(self) -> int:
        return self.shape[1]

    @property
    def _gap_size(self) -> int:
        return self.width

    def _repr_html_(self):
        max_len = max([len(e) for e in self if isinstance(e, _Series)] + [0])
        elements = [
            Series(
                list(e),
                name=e.header if getattr(e, "_header", None) is not None else "",
            )
            for e in self
        ] + [Series(["" for _ in range(max_len)], name="")]

        df = DataFrame(elements)
        df.columns = ["" for _ in range(max(len(e) for e in elements))]

        if not any(getattr(e, "_header", None) is not None for e in self):
            return df.fillna("").style.hide(axis="index")._repr_html_()
        return df.fillna("")._repr_html_()

    def _border_mask(self, top, right, bottom, left) -> Style:
        return Style(
            first=[top, right, False, left],
            last=[False, right, bottom, left],
            middle=[False, right, False, left],
        )

    @staticmethod
    def _inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.y += elem.height
        return offset

    def _starting_offset(self) -> Loc:
        offset = Loc((0, 0), self.loc.ws)
        if getattr(self, "_header", None) is not None:
            offset.y += 1
        return offset


VFrame.sibling_type = Frame
Frame.sibling_type = VFrame
