from typing import Any

from excelbird.util import get_dimensions

def elem_math(a: Any, b: Any, func, sign: str) -> Any:
    from excelbird.core.cell import Cell
    from excelbird.core.vec import Col
    from excelbird.core.frame import HFrame
    a_cls, b_cls = a.__class__, b.__class__
    a_dim, b_dim = get_dimensions(a), get_dimensions(b)

    if a_cls == list:
        a_cls = Col
    if b_cls == list:
        print("B is list")

    if a_dim == 0 and b_dim == 0:
        return Cell(expr=[a, sign, b])

    if a_dim == b_dim:
        return a_cls(*[func(e1, e2) for e1,e2 in zip(a, b)])
    
    if a_dim > b_dim:
        return a_cls(*[func(elem, b) for elem in a])

    if a_dim < b_dim:
        return b_cls(*[func(a, elem) for elem in b])


class CanDoMath:

    def __neg__(self, other):
        # Need to change elem_math before implementation to support
        # 2-element expressions like [" - ", self]
        ...

    def __eq__(self, other):
        return elem_math(self, other, lambda a,b: a == b, " = ")

    def __ne__(self, other):
        return elem_math(self, other, lambda a,b: a != b, " <> ")

    def __lt__(self, other):
        return elem_math(self, other, lambda a,b: a < b, " < ")

    def __gt__(self, other):
        return elem_math(self, other, lambda a,b: a > b, " > ")

    def __le__(self, other):
        return elem_math(self, other, lambda a,b: a <= b, " <= ")

    def __ge__(self, other):
        return elem_math(self, other, lambda a,b: a >= b, " >= ")


    def __add__(self, other):
        return elem_math(self, other, lambda a,b: a + b, " + ")

    def __radd__(self, other):
        return elem_math(other, self, lambda a,b: a + b, " + ")


    def __sub__(self, other):
        return elem_math(self, other, lambda a,b: a - b, " - ")

    def __rsub__(self, other):
        return elem_math(other, self, lambda a,b: a - b, " - ")


    def __mul__(self, other):
        return elem_math(self, other, lambda a,b: a * b, " * ")

    def __rmul__(self, other):
        return elem_math(other, self, lambda a,b: a * b, " * ")


    def __truediv__(self, other):
        return elem_math(self, other, lambda a,b: a / b, " / ")

    def __rtruediv__(self, other):
        return elem_math(other, self, lambda a,b: a / b, " / ")


    def __xor__(self, other):
        return elem_math(self, other, lambda a,b: a ^ b, " ^ ")

    def __rxor__(self, other):
        return elem_math(other, self, lambda a,b: a ^ b, " ^ ")


    def __pow__(self, other):
        return elem_math(self, other, lambda a,b: a ^ b, " ^ ")

    def __rpow__(self, other):
        return elem_math(other, self, lambda a,b: a ^ b, " ^ ")


    def __rshift__(self, other):
        return elem_math(self, other, lambda a,b: a >> b, ":")

    def __rrshift__(self, other):
        return elem_math(self, other, lambda a,b: a >> b, ":")


    def __and__(self, other):
        if isinstance(other, str):
            if not other.endswith('"') and not other.startswith('"'):
                other = f'"{other}"'
        return elem_math(self, other, lambda a,b: a & b, " & ")

    def __rand__(self, other):
        if isinstance(other, str):
            if not other.endswith('"') and not other.startswith('"'):
                other = f'"{other}"'
        return elem_math(self, other, lambda a,b: a & b, " & ")