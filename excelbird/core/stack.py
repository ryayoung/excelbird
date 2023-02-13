"""
Detailed documentation and code examples coming soon.
"""
from __future__ import annotations
# External
from pandas import Series, DataFrame
from typing import Any
from copy import deepcopy

# Internal main
from excelbird.styles import default_table_style

from excelbird._base.container import ListIndexableById
from excelbird._base.identifier import HasId
from excelbird._base.dotdict import Style
from excelbird._base.loc import Loc
from excelbird._base.styling import (
    HasMargin, 
    HasPadding,
)
from excelbird._utils.util import (
    init_from_same_dimension_type,
)
from excelbird._utils.pass_attributes import (
    pass_attr_to_children,
    pass_dict_to_children,
)
from excelbird._utils.argument_parsing import (
    combine_args_and_children_to_list,
    convert_all_to_type,
    move_remaining_kwargs_to_dict,
)

from excelbird.core.cell import Cell
from excelbird.core.series import (
    _Series,
    Col,
)
from excelbird.core.gap import Gap
from excelbird.core.frame import _Frame, Frame, VFrame
from excelbird.core.expression import Expr
from excelbird.core.function import Func


class _Stack(ListIndexableById, HasId, HasMargin, HasPadding):
    _doc_primary_summary = """
    A general container that can hold any element, *including itself*. Offers unique spatial styling
    features, like margin and padding, described below.
    """
    _doc_params = """
    .. note:: Stacks *cannot* be used in a python expression, or included in a :class:`Func`. However, you can still call :meth:`self.ref()` to make an exact reference to its cells.

    Parameters
    ----------
    *args : Union[Stack, VStack, Frame, VFrame, Col, Row, Cell, list, tuple, str, int, float, pd.Series, pd.DataFrame, np.ndarray, Gap, Expr, Func, set]
        Can take any layout element (besides Book or Sheet), or any value that
        can be used to construct a layout element. Stack is the only layout element
        that can store other instances of itself as children
    children : list, optional
        Will be combined with args
    id : str, optional
        Unique identifier to store globally so that this element can be referenced
        elsewhere in the layout without being assigned to a variable
    sep : Gap or bool or int or dict, optional
        A sep in any excelbird layout element inserts a Gap between each of its children.
        If True, a default of Gap(1) is used. If int, Gap(sep) will be used. If a dict,
        ``Gap(1, **sep)`` will be used.
    background_color : str, optional
        Hex code for background_color. Will be applied to fill_color of padding, any Gap
        child who hasn't specified its own fill_color, and to any child Stack/VStack's margins.
        Will also be passed down to any child (Cell excluded) who hasn't specified its own
        background_color.
    schema : Schema, optional
        Applied to each child who takes schema
    cell_style : dict, optional
        Applied to each child who has cell_style
    header_style : dict, optional
        Applied to each child who has header_style
    table_style : dict or bool, optional
        Applied to each child who has table_style
    margin : int or list[int], optional
        Margin, like padding, will apply space around the element. Unlike padding, margin space
        will NOT inherit any of the element's styling. It will, however, be filled with the
        parent container's background_color, if present. Syntax inspired by CSS. An int,
        if passed, will be applied to all 4 sides. If list, length can be 2, 3, or 4 elements.
        Order is [top, right, bottom, left]. If length 2, apply the first element to top and
        bottom margin, and second to right and left.
    margin_top : int, optional
        Top margin, measured in number of cells
    margin_right : int, optional
        Right margin, measured in number of cells
    margin_bottom : int, optional
        Bottom marign, measured in number of cells
    margin_left : int, optional
        Left margin, measured in number of cells
    padding : int or list[int], optional
        Padding, like margin, will apply space around the element. Unlike margin, padding space
        WILL inherit the element's styling, like background_color. Syntax inspired by CSS. An int,
        if passed, will be applied to all 4 sides. If list, length can be 2, 3, or 4 elements.
        Order is [top, right, bottom, left]. If length 2, apply the first element to top and
        bottom margin, and second to right and left.
    padding_top : int, optional
        Top padding, measured in number of cells
    padding_right : int, optional
        Right padding, measured in number of cells
    padding_bottom : int, optional
        Bottom padding, measured in number of cells
    padding_left : int, optional
        Left padding, measured in number of cells
    **kwargs : Any
        Remaining kwargs will be applied to cell_style

    """

    sibling_type: type = None
    elem_type: type = None
    _dimensions = -1

    def __init__(
        self,
        *args: Any,
        children: list | None = None,
        id: str | int | None = None,
        sep: Any | None = None,
        background_color: str | None = None,
        margin: int | list[int] | None = None,
        margin_top: int | None = None,
        margin_right: int | None = None,
        margin_bottom: int | None = None,
        margin_left: int | None = None,
        padding: int | list[int] | None = None,
        padding_top: int | None = None,
        padding_right: int | None = None,
        padding_bottom: int | None = None,
        padding_left: int | None = None,
        schema: None = None,
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

        self._loc = None
        self.id = id
        self.background_color = background_color
        # Attrs that must be passed to children
        self.schema = schema
        # Dicts that must be passed to children
        self.cell_style = Style(**cell_style)
        self.header_style = Style(**header_style)
        self.table_style = Style(**table_style)

        self._init(children)

        self._init_margin(
            margin,
            margin_top,
            margin_right,
            margin_bottom,
            margin_left,
        )
        self._init_padding(
            padding,
            padding_top,
            padding_right,
            padding_bottom,
            padding_left,
        )

        if sep is not None:
            self._insert_separator(sep)


    def ref(self, inherit_style: bool = False, **kwargs):
        """
        Get a new object with cell references to those in the caller.
        This assumes that **both** the calling object
        and the returned object will be placed in the workbook.

        Parameters
        ----------
        inherit_style : bool, default False
            Copy the caller's style to the returned object.

        Returns
        -------
        :class:`Self`

        Notes
        -----

        .. note::

            Children's ``header`` attributes are stylistic attributes, and therefore will **not** be
            passed to the returned object's children unless ``inherit_style=True``. And, if style
            is inherited, headers will be copied over to the children, instead of cell references to them.

        """
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
                if key not in new_dict and key not in ["_id", "_loc"]:
                    new_dict[key] = val
        return type(self)(*new_elements, **new_dict)

    def transpose(self, **kwargs):
        """
        Convert to sibling type. Places current children into the returned object,
        without copying or making cell references to them.

        Parameters
        ----------
        **kwargs : Any
            Keyword arguments to apply as attributes to the new object.

        Returns
        -------
        :class:`Stack <excelbird.Stack>` or :class:`VStack <excelbird.VStack>`
            The opposite to self's type. Try ``type(my_obj).sibling_type``

        Notes
        -----
        **Assumes that the caller won't be placed in the layout**. Do not
        place both the calling object and returned object in the layout, since
        they both contain the same children.

        .. code-block::

            # 'current' must not be placed in the workbook.
            new = current.transpose()

        To include the caller and make cell references to it, get a reference
        first:

        .. code-block::

            new = current.ref().transpose()

        """
        elements = list(self)
        new = type(self).sibling_type(*elements)
        for key, val in self.__dict__.items():
            if key == "_id":
                key = "id"
            setattr(new, key, val)
        for key, val in kwargs.items():
            if hasattr(new, key):
                setattr(new, key, val)
            elif hasattr(new, 'cell_style'):
                new.cell_style[key] = val
        return new

    def _format_args(self, args: list) -> None:
        convert_all_to_type(args, (str, int, float), Cell, strict=True)
        convert_all_to_type(args, Series, Col)
        convert_all_to_type(args, DataFrame, Frame)
        convert_all_to_type(args, set, Expr)

    @property
    def _elem_widths(self) -> list:
        return [i.width for i in self if hasattr(i, "width")]

    @property
    def _elem_heights(self) -> list:
        return [i.height for i in self if hasattr(i, "height")]

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
                    if "fill_color" not in elem.kwargs and elem.is_margin is False:
                        elem.fill = True
                        elem.kwargs["fill_color"] = self.background_color

                # Child's margins should be filled with self's background color
                elif hasattr(elem, "margin"):
                    if elem.margin != HasMargin.empty:
                        for item in elem:
                            if isinstance(item, Gap):
                                if (
                                    "fill_color" not in item.kwargs
                                    and item.is_margin is True
                                ):
                                    item.fill = True
                                    item.kwargs["fill_color"] = self.background_color
                            elif hasattr(item, "margin"):
                                for x in item:
                                    if isinstance(x, Gap):
                                        if (
                                            "fill_color" not in x.kwargs
                                            and x.is_margin is True
                                        ):
                                            x.fill = True
                                            x.kwargs[
                                                "fill_color"
                                            ] = self.background_color

    def _resolve_padding(self) -> None:
        for elem in self:
            if hasattr(elem, "padding"):
                elem._resolve_padding()

        def get_gap(amount, elem) -> Gap:
            if getattr(elem, "background_color", None) not in [None, False]:
                return Gap(amount, fill_color=elem.background_color)
            return Gap(amount, fill_color=None)

        for i, elem in enumerate(self):
            if hasattr(elem, "padding"):
                if elem.padding != HasPadding.empty:
                    top, right, bottom, left = elem.padding
                    elem_type = type(elem)
                    new_elements = []
                    for i, item in reversed(list(enumerate(elem))):
                        new_elements.insert(0, elem.pop(i))

                    if issubclass(elem_type, Stack):
                        if left is not None:
                            elem.append(get_gap(left, elem))

                        elem.append(
                            elem_type.sibling_type(
                                get_gap(top, elem) if top is not None else None,
                                elem_type(*new_elements),
                                get_gap(bottom, elem) if bottom is not None else None,
                            )
                        )
                        if right is not None:
                            elem.append(get_gap(right, elem))

                    elif issubclass(elem_type, VStack):
                        if top is not None:
                            elem.append(get_gap(top, elem))

                        elem.append(
                            elem_type.sibling_type(
                                get_gap(left, elem) if left is not None else None,
                                elem_type(*new_elements),
                                get_gap(right, elem) if right is not None else None,
                            ),
                        )
                        if bottom is not None:
                            elem.append(get_gap(bottom, elem))

    def _resolve_margin(self) -> None:
        for elem in self:
            if hasattr(elem, "margin"):
                elem._resolve_margin()

        for i, elem in enumerate(self):
            if hasattr(elem, "margin"):
                if elem.margin != HasMargin.empty:
                    top, right, bottom, left = elem.margin
                    elem_type = type(elem)
                    new_elements = []
                    for i, item in reversed(list(enumerate(elem))):
                        new_elements.insert(0, elem.pop(i))

                    if issubclass(elem_type, Stack):
                        if left is not None:
                            elem.append(Gap(left, is_margin=True))

                        elem.append(
                            elem_type.sibling_type(
                                Gap(top, is_margin=True) if top is not None else None,
                                elem_type(*new_elements),
                                Gap(bottom, is_margin=True)
                                if bottom is not None
                                else None,
                            ),
                        )
                        if right is not None:
                            elem.append(Gap(right, is_margin=True))

                    elif issubclass(elem_type, VStack):
                        if top is not None:
                            elem.append(Gap(top, is_margin=True))

                        elem.append(
                            elem_type.sibling_type(
                                Gap(left, is_margin=True) if left is not None else None,
                                elem_type(*new_elements),
                                Gap(right, is_margin=True)
                                if right is not None
                                else None,
                            ),
                        )
                        if bottom is not None:
                            elem.append(Gap(bottom, is_margin=True))

    def _resolve_gaps(self) -> None:
        Gap._convert_all_to_frames(self, type(self).elem_type, self._gap_size)
        for elem in self:
            if hasattr(elem, "_resolve_gaps"):
                elem._resolve_gaps()

    def _set_loc(self, loc: Loc) -> None:
        self._loc = loc

        offset = self._starting_offset()
        for elem in self:
            elem._set_loc(
                Loc((self._loc.y + offset.y, self._loc.x + offset.x), self._loc.ws)
            )
            offset = self._inc_offset(offset, elem)

    def __getitem__(self, key):
        if not isinstance(key, list):
            # return super().__getitem__(key)
            return ListIndexableById.__getitem__(self, key)

        new_elements = [self[self._key_to_idx(k)] for k in key]
        new_dict = {k: v for k, v in self.__dict__.items() if k not in ["_id", "_loc"]}
        if "_header" in new_dict:
            new_dict["header"] = new_dict.pop("_header")

        return type(self)(*new_elements, **new_dict)

    def _validate_child_types(self) -> None:
        valid_types = (
            _Stack,
            _Frame,
            _Series,
            Cell,
            Gap,
        )
        for elem in self:
            if not isinstance(elem, valid_types):
                raise TypeError(
                    f"At write time, a {type(self).__name__} can only hold "
                    "the following types:\n{valid_types}"
                )
            if hasattr(elem, "_validate_child_types"):
                elem._validate_child_types()

    def _write(self) -> None:
        pass_attr_to_children(self, "schema")
        pass_dict_to_children(self, "cell_style")
        pass_dict_to_children(self, "header_style")
        pass_dict_to_children(self, "table_style")

        if len(self.cell_style) > 0:
            for elem in self:
                if isinstance(elem, Cell):
                    elem._inherit_style_without_override(self.cell_style)

        for elem in self:
            elem._write()

    def _starting_offset(self) -> Loc:
        return Loc((0, 0), self._loc.ws)


class Stack(_Stack):
    _doc_custom_summary = """
    * Direction: **horizontal**
    * Child Type: :class:`Stack`, :class:`VStack`, :class:`Frame`, :class:`VFrame`, :class:`Col`, :class:`Row`, :class:`Cell`
    """
    sibling_type: type = None  # these are set after class declaration
    elem_type: type = Frame

    def transpose(self, **kwargs) -> VStack:
        return super().transpose(**kwargs)

    def ref(self, inherit_style: bool = False, **kwargs) -> Stack:
        return super().ref(inherit_style, **kwargs)

    @property
    def width(self) -> int:
        return sum(self._elem_widths + [0])

    @property
    def height(self) -> int:
        heights = [i.height for i in self if hasattr(i, 'height') and not isinstance(i, Gap)]
        return max(heights + [0])

    @staticmethod
    def _inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.x += elem.width
        return offset

    @property
    def _gap_size(self) -> int:
        return self.height


class VStack(_Stack):
    _doc_custom_summary = """
    * Direction: **vertical**
    * Child Type: :class:`Stack`, :class:`VStack`, :class:`Frame`, :class:`VFrame`, :class:`Col`, :class:`Row`, :class:`Cell`
    """
    sibling_type: type = Stack  # these are set after class declaration
    elem_type: type = VFrame

    def transpose(self, **kwargs) -> Stack:
        return super().transpose(**kwargs)

    def ref(self, inherit_style: bool = False, **kwargs) -> VStack:
        return super().ref(inherit_style, **kwargs)

    @property
    def width(self) -> int:
        widths = [i.width for i in self if hasattr(i, 'width') and not isinstance(i, Gap)]
        return max(widths + [0])

    @property
    def height(self) -> int:
        return sum(self._elem_heights + [0])

    @staticmethod
    def _inc_offset(offset: Loc, elem: Any) -> Loc:
        offset.y += elem.height
        return offset

    @property
    def _gap_size(self) -> int:
        return self.width

Stack.sibling_type = VStack

Stack.__doc__ = f"""
    {_Stack._doc_primary_summary}

    {Stack._doc_custom_summary}

    {_Stack._doc_params}

    """

VStack.__doc__ = f"""
    {_Stack._doc_primary_summary}

    {VStack._doc_custom_summary}

    {_Stack._doc_params}

    """
