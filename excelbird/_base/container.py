from __future__ import annotations
from typing import Any
from excelbird.core.gap import Gap
from dataclasses import dataclass

@dataclass(slots=True)
class Locable:
    elem: ListIndexableById

    def __getitem__(self, key: slice) -> Any:
        if not isinstance(key, slice):
            return self.elem.__getitem__(key)

        start, stop = key.start, key.stop
        if start is None:
            start = 0
        if stop is None:
            stop = -1

        elem_from = self.elem[self.elem._key_to_idx(start)]
        elem_to = self.elem[self.elem._key_to_idx(stop)]
        return elem_from >> elem_to


class ListIndexableById(list):
    """
    A simple child class of list that can accept an `id` string as a
    key to access elements.

    Each element MUST have an `id` property itself, before trying to
    access elements.
    """

    @property
    def loc(self) -> Locable:
        """
        When subscripted, provides an alternative to the default
        subscripting behavior. Instead of returning the elements
        found by the slice, a subscripted ``loc`` will return a *range*
        from the found elements.

        .. warning::

            Slices of ``loc`` will be **inclusive** of the 'stop'
            argument, unlike normal slices which exclude it.

        For instance, ``my_frame.loc[2:5]`` is equivalent to
        ``my_frame[2] >> my_frame[5]``.

        Returns
        -------
        :class:`Locable <excelbird.Locable>`
        """
        return Locable(self)

    def insert(self, index, new) -> None:
        index = self._key_to_idx(index)
        super().insert(index, new)

    def set(self, **kwargs) -> ListIndexableById:
        """
        Set attributes inline.

        Useful if defining a complex layout and setting attributes
        dynamically via either a list comprehension or inline conditionals.

        Parameters
        ----------
        **kwargs : Any
            All keyword arguments will be set as attributes on self, via ``setattr()``

        Returns
        -------
        :class:`Self`

        Examples
        --------

        Instead of having to set an attribute ahead of time, like

        .. code-block::

            if len(elem) > 5:
                elem.bold = True

            Book(
                elem,
            )

        Set the attribute inline!

        .. code-block::

            Book(
                elem if len(elem) < 5 else elem.set(bold=True)
            )
            
        """
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self

    def get(self, key, default=None) -> Any:
        """
        Safely get an element.

        Parameters
        ----------
        key : str or int
            The index, ``id`` or ``header`` (if series) of a child element.
        default : Any, default None
            Value to return if nothing is found

        Returns
        -------
        Any
            Note that some dynamic elements, such as :class:`Gap` or :class:`Expr` may not
            have been resolved to a valid child type yet.

        Notes
        -----

        .. note::

            Excelbird containers are all subclasses of :class:`python:list` so you
            can access elements using square brackets the same as you would with a list.

        """
        try:
            return self[key]
        except Exception:
            return default

    def _key_to_idx(self, key) -> int:
        if isinstance(key, int):
            return key

        ids = [i.id if hasattr(i, "_id") else None for i in self]
        if key in ids:
            return ids.index(key)

        headers = [
            i.header if hasattr(i, "_header") else 
            i.kwargs.get('header', None) if hasattr(i, 'kwargs')
            else None for i in self
        ]
        if key in headers:
            return headers.index(key)
        else:
            raise KeyError(f"Invalid key, {key}")


    def __setitem__(self, key, val) -> None:
        from excelbird.core.function import Func
        if isinstance(key, int):
            return super().__setitem__(key, val)
        if isinstance(val, Func):
            val.kwargs['id'] = key
        else:
            val.id = key
        try:
            index = self._key_to_idx(key)
            self[index] = val
        except Exception:
            self.append(val)

    def __getitem__(self, key) -> Any:
        if not isinstance(key, slice):
            return super().__getitem__(self._key_to_idx(key))

        start, stop = key.start, key.stop
        if start is not None:
            start = self._key_to_idx(start)
        if stop is not None:
            stop = self._key_to_idx(stop)

        elems = super().__getitem__(slice(start, stop, key.step))

        if not isinstance(elems, list):
            return elems

        new = type(self)(*elems)
        for key, val in self.__dict__.items():
            if key == "_header":
                key = "header"
            if key == "_id":
                key = "id"
            setattr(new, key, val)
        return new

    def __repr__(self):
        # This shouldnt be here but I'm lazy
        return f"{type(self).__name__}({super().__repr__()})"

    def _init(self, args: list, **kwargs):
        """
        A container should finish its initialization by
        calling this function
        """
        from excelbird.core.expression import Expr
        from excelbird.core.function import Func

        list.__init__(self, list(args))

        for key, val in kwargs.items():
            setattr(self, key, val)

        Expr._set_use_ref_for_container_recursive(self)
        Expr._resolve_container_recursive(self)
        Func._resolve_container_recursive(self)

    def _insert_separator(self, separator: Gap | int | bool | dict) -> None:
        if type(separator) in [int, bool, dict]:
            if separator is True:
                separator = 1
            if isinstance(separator, int):
                separator = Gap(separator)
            elif isinstance(separator, dict):
                separator = Gap(1, **separator)

        for i, _ in reversed(list(enumerate(self))):
            if i > 0:
                self.insert(i, separator)
