from typing import Any, Iterable


class HasMargin:
    empty = [None, None, None, None]

    def _init_margin(self, margin, top, right, bottom, left) -> None:

        if (margin, top, right, bottom, left) == (None, None, None, None, None):
            self.margin_top = None
            self.margin_right = None
            self.margin_bottom = None
            self.margin_left = None
            return

        if not isinstance(margin, list):
            margin = [margin]
        if len(margin) == 1:
            margin *= 4
        elif len(margin) == 2:
            margin *= 2
        elif len(margin) == 3:
            margin += [None]

        self.margin_top = margin[0]
        self.margin_right = margin[1]
        self.margin_bottom = margin[2]
        self.margin_left = margin[3]

        if top is not None:
            self.margin_top = top
        if right is not None:
            self.margin_right = right
        if bottom is not None:
            self.margin_bottom = bottom
        if left is not None:
            self.margin_left = left

    @property
    def margin(self) -> list[int | None]:
        return [
            self.margin_top,
            self.margin_right,
            self.margin_bottom,
            self.margin_left,
        ]


class HasPadding:
    empty = [None, None, None, None]

    def _init_padding(self, padding, top, right, bottom, left) -> None:

        if (padding, top, right, bottom, left) == (None, None, None, None, None):
            self.padding_top = None
            self.padding_right = None
            self.padding_bottom = None
            self.padding_left = None
            return

        if not isinstance(padding, list):
            padding = [padding]
        if len(padding) == 1:
            padding *= 4
        elif len(padding) == 2:
            padding *= 2
        elif len(padding) == 3:
            padding += [None]

        self.padding_top = padding[0]
        self.padding_right = padding[1]
        self.padding_bottom = padding[2]
        self.padding_left = padding[3]

        if top is not None:
            self.padding_top = top
        if right is not None:
            self.padding_right = right
        if bottom is not None:
            self.padding_bottom = bottom
        if left is not None:
            self.padding_left = left

    @property
    def padding(self) -> list[int | None]:
        return [
            self.padding_top,
            self.padding_right,
            self.padding_bottom,
            self.padding_left,
        ]

class HasBorder:
    """
    Child class is responsible for making sure each instance
    has variable, 'border_x' for each side.
    """

    empty = [None, None, None, None]
    negated = [False, False, False, False]
    default_weight = "thin"
    default_color = "000000"
    default = ("thin", "000000")
    valid_weights = (
        "dashDot",
        "dashDotDot",
        "dashed",
        "dotted",
        "double",
        "hair",
        "medium",
        "thick",
        "thin",
        "mediumDashDot",
        "mediumDashDotDot",
        "mediumDashed",
        "slantDashDot",
    )

    def _init_border(self, border, top, right, bottom, left) -> None:
        """
        Processes the full border and individual sides, where
        individual sides take priority only if they are not None
        """
        cls = type(self)
        self.border = border
        if top is not None:
            self.border_top = cls._interpret_single_value(top)
        if right is not None:
            self.border_right = cls._interpret_single_value(right)
        if bottom is not None:
            self.border_bottom = cls._interpret_single_value(bottom)
        if left is not None:
            self.border_left = cls._interpret_single_value(left)

        _ = self.border

    @property
    def border(self) -> list:
        """
        A great border
        """
        for side in ["border_top", "border_right", "border_bottom", "border_left"]:
            if not hasattr(self, side):
                setattr(self, side, None)

        cls = type(self)

        self.border_top = cls._interpret_single_value(self.border_top)
        self.border_right = cls._interpret_single_value(self.border_right)
        self.border_bottom = cls._interpret_single_value(self.border_bottom)
        self.border_left = cls._interpret_single_value(self.border_left)

        return [
            self.border_top,
            self.border_right,
            self.border_bottom,
            self.border_left,
        ]

    @border.setter
    def border(self, new: list) -> None:
        top, right, bottom, left = type(self)._parse_arg(new)
        self.border_top = top
        self.border_right = right
        self.border_bottom = bottom
        self.border_left = left

    @classmethod
    def _is_valid(cls, value: Any) -> bool:
        if value is None or value is False:
            return True
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], str) and isinstance(value[1], str):
                    if not value[1].startswith("#"):
                        return True
        return False

    @classmethod
    def _interpret_single_value(cls, value: Any) -> tuple[Any, Any]:
        """
        Given a value intended to represent a single border side, interpret
        it to one of the following valid formats:
        * None - unset, can be overriden
        * False - override parent and remove border
        * ('<weight>' | None | False, '<hex color>' | None | False)

        Valid inputs for ``value``:
        * None
        * True - converts to ``cls.default``
        * False
        * '<weight>' - we can tell if the string is in list of valid weights
        * '<hex color>'
        * ('<weight>' | None | True | False,)
        * ('<weight>' | None | True | False, '<hex color>' | None | True | False)
        """
        if cls._is_valid(value):
            return value

        # Treat 1-element tuple as single value
        if isinstance(value, tuple):
            if len(value) == 1:
                value = value[0]

        if value is True:
            return cls.default

        # If string, we can definitively conclude whether they were
        # referring to the weight or to the color.
        if isinstance(value, str):
            if value in cls.valid_weights:
                return (value, cls.default_color)
            else:
                return (cls.default_weight, value)

        # Now it must be a 2-element tuple
        if not isinstance(value, tuple):
            raise ValueError(f"Invalid border value, {value}")
        if not len(value) == 2:
            raise ValueError(f"Invalid border value, {value}")

        if value[0] is True:
            value = (cls.default_weight, value[1])

        if value[1] is True:
            value = (value[0], cls.default_color)

        for val in value:
            if not isinstance(val, str) and not val is None and not val is False:
                raise ValueError(f"Border weight/color values must be strings. {value} is invalid")

        if not value[0] in cls.valid_weights and not value[0] is None and not value[0] is False:
            raise ValueError(f"'{value[0]}' is not a valid weight")
        if not isinstance(value[1], str) and not value[1] is None and not value[1] is False:
            raise ValueError(f"'{value[1]}' is not a valid hex color")

        if isinstance(value[1], str):
            value = (value[0], value[1].lstrip("#"))
            if not len(value[1]) == 6:
                raise ValueError(f"Color value must be 6-character hex code. {value[1]} is invalid")

        return value

    @classmethod
    def _parse_arg(
        cls, border: bool | Iterable | None
    ) -> list:
        """
        Designed to mimic CSS border logic. Returns a 4-element list
        describing the border of 4 sides, in the order: top, right, bottom,
        left. Elements can either be None, False, or a string representing weight.

        Arguments of True will default to 'thin' border

        Example arguments to outputs:
            True or 'thin':
                [ 'thin', 'thin', 'thin', 'thin' ]
            [ 'thin', False ]:
                [ 'thin', False, 'thin', False ]
            [ 'thick', 'thick', 'thick' ]:
                [ 'thick', 'thick', 'thick', False ]
        """
        if border is None or border == cls.empty:
            return cls.empty
        if border == cls.negated:
            return cls.negated

        if isinstance(border, tuple):
            if len(border) > 2:
                print(border)
                raise TypeError("Border must be a list")

        if not isinstance(border, list):
            border = [border]

        for i, elem in enumerate(border):
            border[i] = cls._interpret_single_value(elem)

        if len(border) == 1:
            border = border * 4
        elif len(border) == 2:
            border += border
        elif len(border) == 3:
            border += [border[1]]

        assert len(border) == 4, "Border must be 4 elements. If you're reading this, an excelbird developer made a mistake"
        return list(border)

    def _apply_border(self) -> None:
        if not hasattr(self, "__len__"):
            return
        if len(self) == 0 or self.border == [None, None, None, None]:
            return

        first = self[0]

        if len(self) == 1:
            if getattr(first, "is_empty", None) is True and hasattr(first, 'value'):
                first.value = ""
            first.border = self.border

        elif len(self) >= 2:
            mask = self._border_mask(*self.border)
            last = self[-1]
            middle_elements = self[1:-1]

            if getattr(first, "is_empty", None) is True and hasattr(first, 'value'):
                first.value = ""
            if getattr(last, "is_empty", None) is True and hasattr(last, 'value'):
                last.value = ""

            first.border = mask.first
            last.border = mask.last
            if len(self) > 2:
                for elem in middle_elements:
                    if getattr(elem, 'is_empty', None) is True and hasattr(elem, 'value'):
                        elem.value = ""
                    elem.border = mask.middle

