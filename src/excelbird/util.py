from typing import Any, Iterable, Generator
from pandas import DataFrame, Series, to_datetime
from openpyxl.worksheet.worksheet import Worksheet
import openpyxl.worksheet.table as xl_tbl
import re

from excelbird.globals import global_ids
from excelbird.styles import default_table_style
from excelbird.base_types import Gap, Style, I

def get_dimensions(elem: Any) -> int:
    return getattr(elem.__class__, "dimensions", 0)


def autofit_algorithm(value: str) -> int:
    """
    Decides column width given string value of a cell
    """
    filtered_value = str(value).replace("_xlfn.", "")
    length_coef = len(filtered_value)
    with_lower_bound = max(length_coef, 10)
    with_upper_bound = min(with_lower_bound, 40)
    return with_upper_bound


def capture_kwargs_by_type(
    kwargs: dict, types: tuple[type, ...] | type
) -> Generator[tuple[Any, Any], None, None]:
    """
    Loop through a dictionary's items that match type(s)
    """
    for key, val in kwargs.items():
        if isinstance(val, types):
            yield (key, val)


def capture_args_by_type(
    args: list | tuple, types: tuple[type, ...] | type
) -> Generator[tuple[int, Any], None, None]:
    """
    Enumerate through an iterable's values that match type(s)
    """
    for i, arg in enumerate(args):
        if isinstance(arg, types):
            yield (i, arg)


def to_date(column: Series) -> Series:
    return to_datetime(column).dt.date


def datetime_cols_to_dates(df: DataFrame) -> DataFrame:
    """
    Applies `to_date()` to each column in `df` that has a datetime64[ns] type
    """
    df = df.copy()
    for col in df.columns:
        if df[col].dtype == "datetime64[ns]":
            df[col] = to_date(df[col])
    return df


def pass_attr_to_children(container: list, attr_name: str) -> None:
    """
    For each child element whose attribute, `attr_name` is not None,
    set that attribute to the value of the parent's `attr_name`

    Mutates inplace: `container`
    """
    container_attr = getattr(container, attr_name)
    if container_attr is None:
        return
    for elem in container:
        if hasattr(elem, attr_name):
            if getattr(elem, attr_name) is None:
                setattr(elem, attr_name, container_attr)


def pass_dict_to_children(container: list, dict_name: str) -> None:
    """
    Copy each element in a parent container's `dict_name` to each
    of its children's `dict_name` if that child hasn't already set it.
    ---
    Container MUST have an attribute called `dict_name`, and that
    attribute MUST be an instance of dictionary.

    Mutates inplace: `container`
    """
    container_dict = getattr(container, dict_name)
    if container_dict is None:
        return
    if len(container_dict) == 0:
        return
    for elem in container:
        if hasattr(elem, dict_name):
            for attr, value in container_dict.items():
                if attr not in getattr(elem, dict_name):
                    getattr(elem, dict_name)[attr] = value


def pass_attr_without_override(elem1: Any, elem2: Any, attr_name: str) -> None:
    """
    If elem1 and elem2 have attribute, `attr_name` and that attribute is not None
    for elem1 and IS None for elem2, set elem1's value for the attribute to elem2

    Mutates inplace:
        `elem1`
        `elem2`
    """
    assert hasattr(elem1, attr_name), (
        f"Element 1 must have attribute, '{attr_name}'"
    )
    if not hasattr(elem2, attr_name):
        return

    elem1_attr = getattr(elem1, attr_name)
    elem2_attr = getattr(elem2, attr_name)

    if elem1_attr is None:
        return
    if elem2_attr is not None:
        return
    
    setattr(elem2, attr_name, elem1_attr)


def pass_dict_without_override(elem1: Any, elem2: Any, dict_name: str) -> None:
    """
    If elem1 and elem2 have attribute, `dict_name` and that attribute is a dict,
    Safely pass each each element from `elem1`'s `dict_name` to `elem2`'s `dict_name`

    Mutates inplace:
        `elem1`
        `elem2`
    """
    assert hasattr(elem1, dict_name), (
        f"Element 1 must have attribute, {dict_name}"
    )
    if not hasattr(elem2, dict_name):
        return

    elem1_dict = getattr(elem1, dict_name)
    elem2_dict = getattr(elem2, dict_name)

    assert (
        elem1_dict is not None and elem2_dict is not None
    ), f"Both element's {dict_name} can't be None"

    for key, val in elem1_dict.items():
        if key not in elem2_dict:
            elem2_dict[key] = val


def ensure_value_is_not_number(value: Any, message: str | None = None) -> bool:
    if message is None:
        message = (
            f"Value, '{value}' looks like a number. You've tried to place it in a cell "
            "that must be text to avoid breaking Excel. Please change it to text. "
            "A common example of this is Table headers. "
        )
    try:
        float(value)
        raise TypeError(message)
    except ValueError:
        return True


def ensure_value_is_number(value: Any, message: str | None = None) -> int | float:
    if isinstance(value, (int, float)):
        return value

    if message is None:
        message = (
            f"Value, '{value}' Can't be converted to a number. You've tried to place "
            "it in a cell that must contain a number to avoid breaking Excel. "
            "Please change it to a number."
        )
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            raise ValueError(message)


def get_idx(container: list, index: int, default: Any = None) -> Any:
    """
    Safely call list's __getitem__ for an index that might not be valid
    """
    try:
        return container[index]
    except (KeyError, IndexError):
        return default


def combine_args_and_children_to_list(args: tuple, children: list | None) -> list:
    """
    Combines elements passed as positionals with elements passed
    inside `children` into one list.
    """
    args = list(args)
    if children is not None:
        args += children
    return args


def move_dict_args_to_other_dict(container: list, other_dict: dict) -> None:
    """
    If any dictionaries are in `container` (likely because they were passed
    as positional arguments), they will be popped from container and their
    key/val pairs safely set to other_dict.

    Mutates inplace:
        `container`
        `other_dict`
    """
    for i, elem in enumerate(container):
        if isinstance(elem, dict):
            new = container.pop(i)
            for key, val in new.items():
                if other_dict.get(key) is None:
                    other_dict[key] = val


def convert_all_to_type(
    container: list,
    from_type: type | tuple[type, ...],
    to_type: type
) -> None:
    for i, elem in enumerate(container):
        if isinstance(elem, from_type):
            container[i] = to_type(elem)


def convert_sibling_types(instance, container: list) -> None:
    elem_type = instance.__class__.elem_type
    sib_type = elem_type.sibling_type
    for i, elem in enumerate(container):
        if isinstance(elem, sib_type):
            container[i] = elem.astype(elem_type)


def init_container(instance, args: list, **kwargs):
    """
    A container should finish its initialization by
    calling this function
    """
    from excelbird.expression import Expr
    from excelbird.function import _DelayedFunc

    list.__init__(instance, list(args))

    for key, val in kwargs.items():
        setattr(instance, key, val)

    Expr.set_use_ref_for_container_recursive(instance)
    Expr.resolve_container_recursive(instance)
    _DelayedFunc.resolve_container_recursive(instance)


def move_remaining_kwargs_to_dict(kwargs: dict, to_dict: dict, safely: bool = False) -> None:
    """
    OVERRIDES values in to_dict
    """
    for key, val in kwargs.items():
        if safely is True and key in to_dict:
            continue
        to_dict[key] = val
    

def init_from_same_dimension_type(instance, args: list) -> list:
    """
    Mutates `instance` inplace, AND returns new args.
    """
    first_arg = get_idx(args, 0)
    if (
        len(args) == 1
        and get_dimensions(first_arg) == instance.__class__.dimensions
    ):
        args = list(first_arg)
        for key, val in first_arg.__dict__.items():
            if key == "loc":
                continue
            if key == "_id":
                key = "id"
            setattr(instance, key, val)
    
    return args


def is_notebook() -> bool:
    """
    Thank you very much Gustavo Bezerra on Stackoverflow
    """
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter


def require_each_element_to_be_cls_type(container: list) -> None:
    cls_name = container.__class__.__name__
    elem_type = container.__class__.elem_type
    elem_type_name = elem_type.__name__
    for i, elem in enumerate(container):
        if not isinstance(elem, elem_type):
            raise TypeError(
                f"Each element inside {cls_name} must be a {elem_type_name}. "
                f"Elem at index {i} is a '{elem.__class__.__name__}'. Its value is: {elem}"
            )


def mark_all_cells_as_written_recursive(container: list) -> None:
    from excelbird.core.cell import Cell
    for elem in container:
        if isinstance(elem, Cell):
            elem.written = True
        elif isinstance(elem, list):
            mark_all_cells_as_written_recursive(elem)


