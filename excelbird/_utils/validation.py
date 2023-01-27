from typing import Any

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


def require_each_element_to_be_cls_type(container: list) -> None:
    cls_name = type(container).__name__
    elem_type = type(container).elem_type
    elem_type_name = elem_type.__name__
    for i, elem in enumerate(container):
        if not isinstance(elem, elem_type):
            raise TypeError(
                f"Each element inside {cls_name} must be a {elem_type_name}. "
                f"Elem at index {i} is a '{type(elem).__name__}'. Its value is: {elem}"
            )
