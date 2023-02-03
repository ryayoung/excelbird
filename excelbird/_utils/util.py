from typing import Any
from pandas import DataFrame, Series, to_datetime

from excelbird.core.gap import Gap

def get_dimensions(elem: Any) -> int:
    if isinstance(elem, type):
        return getattr(elem, "_dimensions", -1)
    return getattr(type(elem), "_dimensions", -1)


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


def get_idx(container: list, index: int, default: Any = None) -> Any:
    """
    Safely call list's __getitem__ for an index that might not be valid
    """
    try:
        return container[index]
    except (KeyError, IndexError):
        return default
    

def init_from_same_dimension_type(instance, args: list) -> list:
    """
    Mutates `instance` inplace, AND returns new args.
    """
    first_arg = get_idx(args, 0)
    arg_dimensions = get_dimensions(first_arg)
    instance_dimensions = get_dimensions(instance)
    if (
        len(args) == 1
        and arg_dimensions == instance_dimensions
        and arg_dimensions > 0 and instance_dimensions > 0
    ):
        args = list(first_arg)
        for key, val in first_arg.__dict__.items():
            if key == "_loc":
                continue
            if key == "_id":
                key = "id"
            if key == "_header":
                key = "header"
            setattr(instance, key, val)
    
    return args


def fill_frames(container: list) -> None:
    from excelbird.core.stack import _Stack
    from excelbird.core.frame import _Frame
    from excelbird.core.series import _Series
    from excelbird.core.cell import Cell

    def true_length(series) -> int:
        return len(series) + (0 if series.header is None else 1)

    for elem in container:
        if isinstance(elem, _Stack):
            fill_frames(elem)

        elif isinstance(elem, _Frame):
            if len(set(
                (true_lengths := [
                    true_length(i) for i in elem if isinstance(i, _Series)
                ])
            )) == 1:
                continue

            max_length = max(true_lengths)

            if elem.fill_empty is True:
                fill_value = lambda: Cell("")
            else:
                fill_value = lambda: Gap()

            for series in [e for e in elem if isinstance(e, _Series)]:
                if (true_len := true_length(series)) < max_length:
                    for _ in range(max_length - true_len):
                        series.append(fill_value())


def set_duplicate_objects_to_ref(
    container: list, memory_ids_history: list,
) -> None:
    """
    Duplicated elements need to have .ref() set.
    """
    from excelbird.core.stack import _Stack
    from excelbird.core.frame import _Frame
    from excelbird.core.series import _Series
    from excelbird.core.cell import Cell
    valid_types = (
        _Stack,
        _Frame,
        _Series,
        Cell,
    )
    for i, elem in enumerate(container):
        if isinstance(elem, valid_types):
            if id(elem) in memory_ids_history and hasattr(elem, "ref"):
                container[i] = elem.ref()
            else:
                memory_ids_history.append(id(elem))
                if not isinstance(elem, Cell):
                    set_duplicate_objects_to_ref(elem, memory_ids_history)


def is_notebook() -> bool:
    """
    Thank you very much Gustavo Bezerra on Stackoverflow
    """
    try:
        shell = type(get_ipython()).__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter




# def mark_all_cells_as_written_recursive(container: list) -> None:
#     from excelbird.core.cell import Cell
#     for elem in container:
#         if isinstance(elem, Cell):
#             elem._written = True
#         elif isinstance(elem, list):
#             mark_all_cells_as_written_recursive(elem)

