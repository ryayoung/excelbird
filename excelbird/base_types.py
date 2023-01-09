from typing import Any, overload, TypeVar, Iterable

from excelbird.globals import global_ids, global_headers
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.utils import get_column_letter
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string


class ImpliedType:
    """
    Short for 'Implied' type. Serves as a temporary container to store arguments
    to later resolve to a desired type

    Once created, an `I` cannot:
        be modified
        be used in expressions/functions
        have its elements/attributes referenced
    until it is either:
        passed as an element to a parent container
        resolved by passing a type to its `resolve_to()` function

    Main purpose (other than for conciseness) is to let you swap parent container types
    without having to refactor element types. For instance, if your code looks like:
        HFrame(Col(...), Col(...))
    and you want to change HFrame to VFrame, you would have to track down every Col element
    and refactor it to a Row. Instead:
        HFrame(I(...), I(...)) easily refactors to: VFrame(I(...), I(...))
    """

    def __init__(self, *args, **kwargs) -> None:
        self.__args = args
        self.__kwargs = kwargs

    def astype(self, dtype: type, **kwargs) -> Any:
        return dtype(*self.__args, **self.__kwargs, **kwargs)
    
    @classmethod
    def resolve_all_in_container(cls, container: list, dtype: type):
        for i, elem in enumerate(container):
            if isinstance(elem, cls):
                container[i] = elem.astype(dtype)


class I(ImpliedType):
    """
    Shorthand for `ImpliedType`
    """
    pass


class Gap(int):
    def __new__(cls, value=None, *args, **kwargs):
        if value is None:
            value = 1
        # Need this because Gap's __init__ takes extra args, which int's
        # __new__ doesn't accept. So just call int's __new__ with the `value`
        # arg and ignore the extras which will be handled by Gap __init__
        return super(Gap, cls).__new__(cls, value)

    def __init__(self, value: int | None = None, fill: bool = False, **kwargs):
        if value is None:
            value = 1
        if len(kwargs) > 0:
            fill = True
        self.fill = fill
        self.kwargs = kwargs
        int.__init__(value)

    def __len__(self):
        return self

    @property
    def width(self):
        return int(self)

    @property
    def height(self):
        return int(self)

    @property
    def fill_val(self):
        if self.fill is True:
            return ""
        return None

    def ref(self):
        return self
    
    @classmethod
    def explode_all_to_values(cls, container: list, val_type: type) -> None:
        """
        Given a container, explode each Gap to `val_type`
        with the gap's fill_val

        Mutates inplace: `container`
        """
        for i, elem in enumerate(container):
            if isinstance(elem, cls):
                gap = container.pop(i)
                for _ in range(gap):
                    container.insert(i, val_type(gap.fill_val, **gap.kwargs))
    
    @classmethod
    def explode_all_to_vecs(cls, container: list, vec_type: type, vec_length: int) -> None:
        """
        Given a container, explode each Gap to vectors of vec_type filled with
        `val_type` with the Gap's fill_val

        Mutates inplace: `container`
        """
        val_type = vec_type.elem_type
        for i, elem in enumerate(container):
            if isinstance(elem, cls):
                gap = container.pop(i)
                for _ in range(gap):
                    container.insert(i,
                        vec_type(*[val_type(gap.fill_val) for _ in range(vec_length)], **gap.kwargs)
                    )
    
    @classmethod
    def convert_all_to_frames(
        cls, container: list, frame_type: type, vec_length: int
    ) -> None:
        """
        Given a container, replace each Gap with a frame of vectors of cells.
        `vec_length` sets the length of each resulting vector.

        Mutates inplace: `container`
        """
        vec_type = frame_type.elem_type
        val_type = vec_type.elem_type
        for i, elem in enumerate(container):
            if isinstance(elem, cls):
                container[i] = frame_type(
                    *[
                        vec_type(*[
                            val_type(elem.fill_val) for _ in range(vec_length)
                        ])
                        for _ in range(elem)
                    ],
                    **elem.kwargs
                )



class HasId:
    """
    Has an id property which, when set, inserts a reference to
    self in `global_ids`.
    """

    @property
    def id(self):
        if not hasattr(self, "_id"):
            self._id = None
        return self._id

    @id.setter
    def id(self, new):
        self.set_id(new)

    def set_id(self, new):
        if new is not None:
            if not isinstance(new, str):
                raise ValueError(f"Invalid id, `{new}`. Ids must be strings.")
            global_ids[new] = self
        self._id = new
        return self


class HasHeader:
    """
    Has an header property which, when set, inserts a reference to
    self in `global_headers`.
    """

    @property
    def header(self):
        if not hasattr(self, "_header"):
            self._header = None
        return self._header

    @header.setter
    def header(self, new):
        self.set_header(new)

    def set_header(self, new):
        if new is not None:
            if not isinstance(new, str):
                raise ValueError(f"Invalid header, `{new}`. Headers must be strings.")
            global_headers[new] = self
        self._header = new
        return self


class HasBorder:
    """
    Child class is responsible for making sure each instance
    has variable, 'border_x' for each side.
    """
    default = [None, None, None, None]

    def init_border(self, border, top, right, bottom, left) -> None:
        """
        Processes the full border and individual sides, where
        individual sides take priority only if they are not None
        """
        self.border = border
        if top is not None:
            self.border_top = top
        if right is not None:
            self.border_right = right
        if bottom is not None:
            self.border_bottom = bottom
        if left is not None:
            self.border_left = left

    @property
    def border(self) -> tuple:
        if not hasattr(self, "_border"):
            self._border = self.__class__.default
        
        return self._border

    @border.setter
    def border(self, new: tuple) -> None:
        self._border = self.__class__.parse_arg(new)
    
    @property
    def border_top(self) -> bool | str | None:
        if not hasattr(self, "_border"):
            self._border = self.__class__.default
        return self._border[0]
    
    @border_top.setter
    def border_top(self, new):
        if not hasattr(self, "_border"):
            self._border = self.__class__.default
        self._border[0] = new

    @property
    def border_right(self) -> bool | str | None:
        if not hasattr(self, "_border"):
            self._border = self.__class__.default
        return self._border[1]
    
    @border_right.setter
    def border_right(self, new):
        if not hasattr(self, "_border"):
            self._border = self.__class__.default
        self._border[1] = new

    @property
    def border_bottom(self) -> bool | str | None:
        if not hasattr(self, "_border"):
            self._border = self.__class__.default
        return self._border[2]
    
    @border_bottom.setter
    def border_bottom(self, new):
        if not hasattr(self, "_border"):
            self._border = self.__class__.default
        self._border[2] = new

    @property
    def border_left(self) -> bool | str | None:
        if not hasattr(self, "_border"):
            self._border = self.__class__.default
        return self._border[3]
    
    @border_left.setter
    def border_left(self, new):
        if not hasattr(self, "_border"):
            self._border = self.__class__.default
        self._border[3] = new
    
    @classmethod
    def parse_arg(
        cls, border: bool | Iterable
    ) -> tuple[str | bool, str | bool, str | bool, str | bool]:
        """
        Designed to mimic CSS border logic. Returns a 4-element tuple
        describing the border of 4 sides, in the order: top, right, bottom,
        left. Elements can either be None, False, or a string representing weight.

        Arguments of True will default to 'thin' border

        Example arguments to outputs:
            True or 'thin':
                ('thin', 'thin', 'thin', 'thin')
            ('thin', False):
                ('thin', False, 'thin', False)
            ('thick', 'thick', 'thick'):
                ('thick', 'thick', 'thick', False)
        """
        if not isinstance(border, (tuple, list)):
            border = [border]

        if isinstance(border, tuple):
            border = list(border)

        border = ["thin" if i is True else i for i in border]

        if len(border) == 1:
            border = border * 4
        elif len(border) == 2:
            border += border
        elif len(border) == 3:
            border += [False]

        assert len(border) == 4, "Border must be 4 elements"
        return list(border)


class DotDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            return super().__getattr__(key)


class Style(DotDict):
    def help(self) -> None:
        print(*self.keys(), sep="\n")


class ListIndexableById(list):
    """
    A simple child class of list that can accept an `id` string as a
    key to access elements.

    Each element MUST have an `id` property itself, before trying to
    access elements.
    """

    def key_to_idx(self, key) -> int:
        if isinstance(key, int):
            return key

        ids = [i.id if hasattr(i, "id") else None for i in self]
        if key in ids:
            return ids.index(key)

        raise KeyError(f"Invalid key, {key}")

    def insert(self, index, new) -> None:
        index = self.key_to_idx(index)
        super().insert(index, new)

    def __setitem__(self, key, val) -> None:
        index = self.key_to_idx(key)
        super().__setitem__(index, val)

    def __getitem__(self, key) -> Any:
        if not isinstance(key, slice):
            key = self.key_to_idx(key)
        return super().__getitem__(key)

    def __repr__(self):
        # This shouldnt be here but I'm lazy
        return f"{self.__class__.__name__}({super().__repr__()})"


TLoc = TypeVar("TLoc", bound="Loc")


class Loc:
    """
    Stores y-x coordinates (ZERO-BASED) of a cell in Excel.
    Takes arguments in the order, `y`, `x`.
    ---
    Can be constructed from:
        String name of a cell in Excel: "B5"
        Another Loc
        2-element iterable of ints (y, x)
        Keywords, 'y' and 'x'
        2 positionals (y and x)

    Conversion to string (`str(my_loc)`) will return an Excel cell location "C7"
    """

    @overload
    def __init__(self, loc: TLoc, ws: None = None) -> None:
        ...

    @overload
    def __init__(self, loc: str | tuple[int, int] | list[int], ws: Worksheet) -> None:
        ...

    def __init__(
        self, loc: TLoc | str | tuple[int, int] | list[int], ws: Worksheet | None = None
    ) -> None:
        if isinstance(loc, Loc):
            self.y = loc.y
            self.x = loc.x
            self.ws = loc.ws

        elif isinstance(loc, (tuple, list)):
            self.y = loc[0]
            self.x = loc[1]
            self.ws = ws

        elif isinstance(loc, str):
            col_str, row_num = coordinate_from_string(loc)
            col_num = column_index_from_string(col_str)
            self.y = row_num - 1
            self.x = col_num - 1
            self.ws = ws
        else:
            raise ValueError(f"Invalid argument, {loc}")

        if self.ws is None:
            raise ValueError("A Loc must have a worksheet")

    @property
    def cell(self) -> str:
        return self.ws[self.cell_str]

    @property
    def col_letter(self) -> str:
        return get_column_letter(self.x + 1)

    @property
    def cell_str(self) -> str:
        return f"{get_column_letter(self.x+1)}{self.y+1}"

    @property
    def title_str(self) -> str:
        chars_to_trigger_quotes = [" ", "-"]
        if any(c in self.ws.title for c in chars_to_trigger_quotes):
            return "'" + self.ws.title + "'" + "!"
        return self.ws.title + "!"

    @property
    def full_str(self) -> str:
        return self.title_str + self.cell_str

    @property
    def column_dimensions(self):
        return self.ws.column_dimensions[self.col_letter]

    @property
    def row_dimensions(self):
        return self.ws.row_dimensions[self.y + 1]


class HasHelp:

    @classmethod
    def help(cls, doc: bool = False):
        doc_str = cls.__doc__
        help_str = cls.__help__
        help_nb_str = cls.__help_notebook__

        if doc_str is None and help_str is None and help_nb_str is None:
            res = f"Sorry, **`{cls.__name__}`** doesn't have any documentation yet."
        elif doc is True or help_str is None:
            res = doc_str
        elif help_str is not None:
            res = help_str

        from excelbird.util import is_notebook
        if is_notebook():
            from IPython.display import display, Markdown as md 
            if help_nb_str is not None:
                display(md(help_nb_str))
            else:
                display(md(res))
        else:
            print(res)
    
    # Your class's help string
    __help__ = None
    # Custom help string for notebooks
    __help_notebook__ = None
