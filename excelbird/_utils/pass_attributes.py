from typing import Any

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
