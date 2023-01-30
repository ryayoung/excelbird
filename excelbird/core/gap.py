"""
Detailed documentation and code examples coming soon. For now, please use the class
reference page below:
"""
from __future__ import annotations
from copy import deepcopy

class Gap(int):
    """
    A spacer inside a container. The parent container will decide what to do with the Gap,
    and convert it into the appropriate type.

    Parameters
    ----------
    value : int, default 1
        The gap distance, measured in cells
    **kwargs :
        Additional keyword arguments are passed to the resulting type when the parent container creates it.    
        This lets you apply styling to the gap

    """

    def __new__(cls, value=None, *args, **kwargs):
        if value is None:
            value = 1
        # Need this because Gap's __init__ takes extra args, which int's
        # __new__ doesn't accept. So just call int's __new__ with the `value`
        # arg and ignore the extras which will be handled by Gap __init__
        return super(Gap, cls).__new__(cls, value)

    def __init__(self, value: int | None = None, fill: bool = False, is_margin: bool = False, **kwargs):
        if value is None:
            value = 1
        if len(kwargs) > 0:
            fill = True
        self.fill = fill
        self.is_margin = is_margin
        self.kwargs = kwargs
        int.__init__(value)

    def __len__(self):
        return self

    @property
    def fill_val(self):
        if self.fill is True:
            return ""
        return None

    def ref(self, inherit_style: bool = False, **kwargs) -> Gap:
        """
        Get a copy.

        `Gap` has this method because parent containers
        will call ``.ref()`` on each of their children, passing the
        same set of arguments. It's unlikely you'll ever want to call
        this method on a `Gap` directly.

        Parameters
        ----------
        inherit_style : bool, default False
            Copy the caller's style to the returned object.
        **kwargs : Any
            Extra keyword arguments are set as attributes on the returned
            object.

        Returns
        -------
        :class:`Gap <excelbird.Gap>`

        """
        if inherit_style is False:
            new = Gap(deepcopy(int(self)))
        else:
            new = deepcopy(self)

        for key, val in kwargs.items():
            new.kwargs[key] = val

        return new

    @property
    def width(self) -> int:
        return int(self)

    @property
    def height(self) -> int:
        return int(self)

    @classmethod
    def _explode_all_to_values(cls, container: list, val_type: type) -> None:
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
    def _explode_all_to_series(
        cls, container: list, series_type: type, series_length: int
    ) -> None:
        """
        Given a container, explode each Gap to seriess of series_type filled with
        `val_type` with the Gap's fill_val

        Mutates inplace: `container`
        """
        val_type = series_type.elem_type
        for i, elem in enumerate(container):
            if isinstance(elem, cls):
                gap = container.pop(i)
                for _ in range(gap):
                    container.insert(
                        i,
                        series_type(
                            *[val_type(gap.fill_val) for _ in range(series_length)],
                            **gap.kwargs,
                        ),
                    )

    @classmethod
    def _convert_all_to_frames(
        cls, container: list, frame_type: type, series_length: int
    ) -> None:
        """
        Given a container, replace each Gap with a frame of series of cells.
        `series_length` sets the length of each resulting series.

        Mutates inplace: `container`
        """
        series_type = frame_type.elem_type
        val_type = series_type.elem_type
        for i, elem in enumerate(container):
            if isinstance(elem, cls):
                container[i] = frame_type(
                    *[
                        series_type(*[val_type(elem.fill_val) for _ in range(series_length)])
                        for _ in range(elem)
                    ],
                    **elem.kwargs,
                )

    def __repr__(self):
        return f"{type(self).__name__}({int(self)})"
