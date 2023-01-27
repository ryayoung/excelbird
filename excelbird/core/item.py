from typing import Any

class Item:
    """
    ====
    Item
    ====

    Let the parent container decide what type the element should be.

    Its abbreviated version, ``I``, can be used interchangeably.

    ``Item`` exists because most layout elements (``Stack``/``VStack`` and ``Sheet`` excluded)
    can only hold one child type. In many cases, your code can be simplified, and
    refactoring made easier, by using ``I``/``Item`` instead of the required child type.
    For instance, if you have a ``Frame`` full of ``Col`` and you want to refactor it
    to a ``VFrame``, you'd need to rename not only the container in question, but also
    each of its children, changing all the ``Col`` instances to ``Row``. If ``I``/``Item``
    were used instead of ``Col``, this code change wouldn't be necessary, as the ``I``
    elements would be interpreted as ``Row`` automatically by the new parent container type.

    Once created, an ``Item`` cannot be modified, used in expressions/functions,
    or have its elements/attributes referenced, until it is either passed as an element
    to a parent container or resolved by calling ``.astype()``.

    ----

    """

    def __init__(self, *args, **kwargs) -> None:
        self.__args = args
        self.__kwargs = kwargs

    def astype(self, dtype: type, **kwargs) -> Any:
        """
        Instantiate the desired type.
        """
        return dtype(*self.__args, **self.__kwargs, **kwargs)

    @classmethod
    def _resolve_all_in_container(cls, container: list, dtype: type):
        for i, elem in enumerate(container):
            if isinstance(elem, cls):
                container[i] = elem.astype(dtype)


class I(Item):
    """
    Shorthand for `Item`
    """

    pass
