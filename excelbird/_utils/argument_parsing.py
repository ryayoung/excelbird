from typing import Any, Generator

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
    to_type: type,
    strict: bool = False,
) -> None:
    def check_elem(elem) -> bool:
        if strict is True:
            if isinstance(from_type, tuple):
                return type(elem) in from_type
            return type(elem) == from_type
        return isinstance(elem, from_type)

    for i, elem in enumerate(container):
        if check_elem(elem):
            container[i] = to_type(elem)


def convert_sibling_types(instance, container: list) -> None:
    elem_type = type(instance).elem_type
    sib_type = elem_type.sibling_type
    for i, elem in enumerate(container):
        if isinstance(elem, sib_type):
            container[i] = elem.transpose()


def move_remaining_kwargs_to_dict(kwargs: dict, to_dict: dict, safely: bool = False) -> None:
    """
    OVERRIDES values in to_dict
    """
    for key, val in kwargs.items():
        if safely is True and key in to_dict:
            continue
        to_dict[key] = val
