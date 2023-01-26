from typing import Any
from types import NoneType
from excelbird.expression import Expr
from excelbird.styles import default_table_style
from excelbird.base_types import Style
from excelbird.math import CanDoMath

from excelbird.util import (
    get_dimensions,
    convert_all_to_type,
)

class Func(CanDoMath):
    def __init__(
        self,
        *inner,
        res_type: type | None = None,
        **kwargs,
    ) -> None:
        """
        All that is needed is the res type and a list of elements.
        Define the function in its exact form, including all characters,
        including parentheses, except the beginnning equals sign. Separate
        out the dynamic elements into their own list elements, which can either
        be an Expression, set, Cell or vector.

        If res type is a cell, call .range()
        """
        inner = list(inner)

        inner = [i for i in inner if i is not None]

        if len(inner) == 0:
            raise ValueError("No elements provided to Func")

        if len(inner) == 1 and type(inner[0]) in [list, tuple]:
            inner = list(inner[0])

        convert_all_to_type(inner, set, Expr)

        if any(isinstance(i, Func) for i in inner):
            raise ValueError("Cannot nest Funcs inside one another, as there is no need to do so.")

        if not all(isinstance(i, (str, int, float, Expr)) or hasattr(i.__class__, "dimensions") for i in inner):
            raise ValueError(
                "Inner elements inside a Func must be any of:, str, int, float, Cell, _Vec, _Frame, Expr"
            )

        self.res_type = res_type
        self.inner = inner
        self.kwargs = kwargs

    def get_function(self, container_type: type | None = None):
        if self.res_type is None:
            if container_type is None:
                raise ValueError(
                    "Can't determine the result type of function. Please provide "
                    "`res_type` as a keyword argument to Func, with the desired return type."
                )
            else:
                from excelbird.core.frame import Frame, VFrame
                from excelbird.core.vec import Col, Row
                valid_containers = (Frame, VFrame, Col, Row)
                if not issubclass(container_type, valid_containers):
                    raise ValueError(
                        f"When a Func is placed inside of a general container type "
                        f"(in this case, {container_type.__name__}) we can't assume  "
                        "its result type cannot be implied/assumed (we don't know) if "
                    )
                self.res_type = container_type.elem_type

        assert self.res_type is not None, (
            "Internal developer error: a Func's res_type is still None. Why? Please raise an Issue on Github so this can be patched. "
            "In the meantime, you can avoid this error by passing `res_type` as a keyword argument to Func"
        )

        if self.all_resolved() is False:
            raise ValueError("All references must be resolved before calling .get_function()")

        dimensions = get_dimensions(self.res_type)
        assert dimensions >= 0, f"Invalid res_type, {self.res_type}"

        if dimensions == 0:
            for i, elem in enumerate(self.inner):
                if get_dimensions(elem) > 0:
                    self.inner[i] = elem.range()
            return self.res_type(func=self.inner, **self.kwargs)

        if dimensions == 1:
            res_length = min(len(x) for x in self.inner if get_dimensions(x) == 1)
            elem_type = self.res_type.elem_type
            for i, elem in enumerate(self.inner):
                if get_dimensions(elem) > 1:
                    frame = elem
                    self.inner[i] = self.res_type(
                        *[ frame[0][k] >> frame[-1][k] for k in range(res_length) ]
                    )
            return self.res_type(
                *[
                    elem_type(func=[item[i] if get_dimensions(item) == 1 else item for item in self.inner])
                    for i in range(res_length)
                ],
                **self.kwargs
            )

        if dimensions == 2:
            raise ValueError(
                "Returning a Frame from Func is not allowed yet. Please return a Cell, Row or Col."
            )

        raise Exception("get function returned nothing")


    def exprs(self) -> list:
        return [i for i in self.inner if isinstance(i, Expr)]

    def all_resolved(self) -> bool:
        if any(i.refs_resolved() is False for i in self.exprs()):
            return False
        return True
    
    def attempt_to_resolve(self, container: list) -> bool:
        """
        Given a parent container, try to resolve each expression
        in self's `inner`.
        """
        for i, elem in enumerate(self.inner):
            if isinstance(elem, Expr):
                if elem.attempt_to_resolve(container) is True:
                    self.inner[i] = elem.eval()

        return self.all_resolved()

    @classmethod
    def resolve_container_recursive(cls, container: list) -> bool:
        """
        For each _DelayedFunc in a container, attempt to resolve each of
        its expressions.

        Returns True if all were resolved

        Mutates inplace: `container`
        """
        all_dfuncs_resolved = True

        for i, elem in enumerate(container):
            if isinstance(elem, cls):

                if elem.attempt_to_resolve(container) is True:
                    container[i] = elem.get_function(container.__class__)
                else:
                    all_dfuncs_resolved = False

            elif isinstance(elem, list):
                if cls.resolve_container_recursive(elem) is False:
                    all_dfuncs_resolved = False

        return all_dfuncs_resolved

    def __repr__(self):
        if self.res_type is not None:
            return f"{self.__class__.__name__}({self.res_type.__name__}...)"
        return f"{self.__class__.__name__}(...)"

