"""
`Item` exists because most layout elements
(with the exception of :class:`Stack <excelbird.Stack>` / :class:`VStack <excelbird.VStack>` and :class:`Sheet <excelbird.Sheet>`)
can only hold **one** child type. In many cases, your code can be simplified, and
refactoring made easier, by using `Item` instead of the child type.

For instance, if you have a :class:`Frame <excelbird.Frame>` and want to refactor it
to a :class:`VFrame <excelbird.VFrame>`, you'd need to rename not only the container in question, but also
each of its children, changing all the :class:`Cols <excelbird.Col>` to :class:`Rows <excelbird.Row>`.
If `Item` were used instead of `Col`, this code change wouldn't be necessary, as each `Item`
would be interpreted as `Row` automatically by the new parent container type.

"""
from typing import Any

class Item:
    """
    Let the parent container decide what type the element should be.

    .. note::

        Once created, an `Item` cannot be modified, used in expressions/functions,
        or have its elements/attributes referenced, until it is either passed as an element
        to a parent container or resolved by calling :meth:`self.construct() <excelbird.Item.construct>`.

    Parameters
    ----------
    *args : Any
        All arguments are stored until the parent container decides which type should be
        instantiated, and will be passed to the corresponding type.
    **kwargs : Any
        All keyword arguments are stored until the parent container decides which type should be
        instantiated, and will be passed to the corresponding type.

    """

    def __init__(self, *args, **kwargs) -> None:
        self.__args = args
        self.__kwargs = kwargs

    def construct(self, dtype: type, **kwargs) -> Any:
        """
        Construct the desired type with the stored data.

        Parameters
        ----------
        dtype : type
            The desired type
        **kwargs : Any
            Additional keyword arguments will be passed to the constructor
            of the desired type

        Returns
        -------
        Any
            Type passed in argument ``dtype``
        """
        return dtype(*self.__args, **self.__kwargs, **kwargs)

    @classmethod
    def _resolve_all_in_container(cls, container: list, dtype: type):
        for i, elem in enumerate(container):
            if isinstance(elem, cls):
                container[i] = elem.construct(dtype)


class I(Item):
    """
    Shorthand for :class:`Item <excelbird.Item>`
    """

    pass
