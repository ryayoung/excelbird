from typing import Any
from excelbird.core.gap import Gap

class ListIndexableById(list):
    """
    A simple child class of list that can accept an `id` string as a
    key to access elements.

    Each element MUST have an `id` property itself, before trying to
    access elements.
    """

    def insert(self, index, new) -> None:
        index = self._key_to_idx(index)
        super().insert(index, new)

    def get(self, key, default=None) -> Any:
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
        else:
            headers = [i.header if hasattr(i, "_header") else None for i in self]
            if key in headers:
                return headers.index(key)
            else:
                raise KeyError(f"Invalid key, {key}")


    def __setitem__(self, key, val) -> None:
        index = self._key_to_idx(key)
        super().__setitem__(index, val)

    def __getitem__(self, key) -> Any:
        if not isinstance(key, slice):
            key = self._key_to_idx(key)
        return super().__getitem__(key)


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