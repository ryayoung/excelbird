# REFACTOR SO & ACTS NORMAL AGAIN
from typing import Any
from pandas import Series, DataFrame

from excelbird._utils.util import get_dimensions
from excelbird.core.gap import Gap
from excelbird._layout_references import Globals


expr_error = ValueError(
    "You've tried to do math with an Expr that contains unresolved references. This isn't possible "
    "because to evaluate this python expression, we need to establish cell references between "
    "the two elements. Since the Expr can't be evaluated yet, we have no cells to reference! "
    "\nHowever, you can always reference another Expr inside of an Expr (that's their purpose). "
    "To do this, assign this Expr an `id` or `header` (which will be applied to its returned element) "
    "and then create a new Expr which references that identifier."
)
func_error = ValueError(
    "You've tried to do math with a Func that contains unresolved references. This isn't possible "
    "because to evaluate this python expression we need to establish cell references between the "
    "two elements. Since the Func can't be evaluated yet, we have no cells to reference! "
    "\nFortunately, you can easily fix this by using an Expr, which allows evaluation to be delayed "
    "until all of its referenecs are resolved. Simply assign this func an `id` or `header` "
    "(which will be applied to its returned element) and then reference that future element in your Expr."
)


def elem_math(a: Any, b: Any, func, sign: str) -> Any:
    from excelbird.core.cell import Cell
    from excelbird.core.series import Col
    from excelbird.core.frame import Frame
    from excelbird.core.function import Func
    from excelbird.core.expression import Expr

    a_cls, b_cls = type(a), type(b)
    a_dim, b_dim = get_dimensions(a), get_dimensions(b)

    if a_cls in [int, str, float]:
        a_dim = 0
    if b_cls in [int, str, float]:
        b_dim = 0

    if type(a) in [list, tuple, Series]:
        a_cls = Col
        a_dim = 1
    elif type(a) in [DataFrame]:
        a_cls = Frame
        a_dim = 2

    if type(b) in [list, tuple, Series]:
        b_cls = Col
        b_dim = 1
    elif type(b) in [DataFrame]:
        b_cls = Frame
        b_dim = 2
    
    if isinstance(a, Expr):
        try:
            a = a._eval()
            a_cls = type(a)
            a_dim = get_dimensions(a)
        except Exception:
            raise expr_error

    elif isinstance(a, Func):
        try:
            a = a._get_function()
            a_cls = type(a)
            a_dim = get_dimensions(a)
        except Exception:
            raise func_error

    if isinstance(b, Expr):
        try:
            b = b._eval()
            b_cls = type(b)
            b_dim = get_dimensions(b)
        except Exception:
            raise expr_error

    elif isinstance(b, Func):
        try:
            b = b._get_function()
            b_cls = type(b)
            b_dim = get_dimensions(b)
        except Exception:
            raise func_error

    assert not isinstance(a, Gap) and not isinstance(b, Gap), (
        "Cannot do math against a Gap"
    )

    if a_dim == 0 and b_dim == 0:
        return Cell(_expr=[a, sign, b])

    if a_dim == b_dim:
        a = [a for a in a if not isinstance(a, Gap)]
        b = [b for b in b if not isinstance(b, Gap)]
        return a_cls(*[func(e1, e2) for e1,e2 in zip(a, b)])
    
    if a_dim > b_dim:
        a = [a for a in a if not isinstance(a, Gap)]
        return a_cls(*[func(elem, b) for elem in a])

    if a_dim < b_dim:
        b = [b for b in b if not isinstance(b, Gap)]
        if hasattr(b_cls, "sibling_type") and a_dim > 0:
            if getattr(b_cls.sibling_type, "elem_type", None) == a_cls:
                b_cls = b_cls.sibling_type

        return b_cls(*[func(a, elem) for elem in b])


class CanDoMath:

    def _space_sign(self, sign: str) -> str:
        space = Globals.expression_sign_spacing
        return (space * " ") + sign + (space * " ")

    def _to_func(self, name: str, extra_param: Any = None):
        from excelbird.core.function import Func
        start = name.upper() + "("
        if extra_param is None:
            return Func(start, self, ")")
        return Func(start, self, ", ", extra_param, ")")

    def __neg__(self):
        from excelbird.core.cell import Cell
        from excelbird.core.function import Func
        from excelbird.core.expression import Expr
        res = self
        cls = type(res)
        dim = get_dimensions(res)

        if isinstance(res, Expr):
            try:
                res = res._eval()
                dim = get_dimensions(res)
            except Exception:
                raise expr_error

        if isinstance(res, Func):
            try:
                res = res._get_function()
                dim = get_dimensions(res)
            except Exception:
                raise func_error

        if dim == 0:
            return Cell(_expr=["-", res])
        
        if dim > 0:
            return cls(*[-elem for elem in res])

        assert False, (
            "Internal developer error. Can't find dimensions of CanDoMath object"
        )

    def __mod__(self, other):
        if self is not other:
            return self._to_func("MOD", other)

        from excelbird.core.cell import Cell
        from excelbird.core.function import Func
        from excelbird.core.expression import Expr
        res = self
        cls = type(res)
        dim = get_dimensions(res)

        if isinstance(res, Expr):
            try:
                res = res._eval()
                dim = get_dimensions(res)
            except Exception:
                raise expr_error

        if isinstance(res, Func):
            try:
                res = res._get_function()
                dim = get_dimensions(res)
            except Exception:
                raise func_error

        if dim == 0:
            return Cell(_expr=[res, "%"])
        
        if dim > 0:
            return cls(*[elem % elem for elem in res])

        assert False, (
            "Internal developer error. Can't find dimensions of CanDoMath object"
        )

    def __round__(self, amount):
        return self._to_func("ROUND", amount)

    def __abs__(self):
        return self._to_func("ABS")

    def __invert__(self):
        return self._to_func("NOT")

    def __floor__(self):
        return self._to_func("FLOOR", 1)

    def __ceil__(self):
        return self._to_func("CEILING", 1)

    def __trunc__(self):
        return self._to_func("TRUNC")

    def __or__(self, other):
        return self._to_func("OR", other)

    def __ror__(self, other):
        from excelbird.core.function import Func
        return Func("OR(", other, ", ", self, ")")

    # def __and__(self, other):
    #     return self._to_func("AND", other)
    #
    # def __rand__(self, other):
    #     from excelbird.core.function import Func
    #     return Func("AND(", other, ", ", self, ")")

    def __eq__(self, other):
        return elem_math(self, other, lambda a,b: a == b, self._space_sign("="))

    def __ne__(self, other):
        return elem_math(self, other, lambda a,b: a != b, self._space_sign("<>"))

    def __lt__(self, other):
        return elem_math(self, other, lambda a,b: a < b, self._space_sign("<"))

    def __gt__(self, other):
        return elem_math(self, other, lambda a,b: a > b, self._space_sign(">"))

    def __le__(self, other):
        return elem_math(self, other, lambda a,b: a <= b, self._space_sign("<="))

    def __ge__(self, other):
        return elem_math(self, other, lambda a,b: a >= b, self._space_sign(">="))

    def __add__(self, other):
        from excelbird.core.function import Func
        if isinstance(self, Func) and self._is_python_sum is True:
            self.inner.insert(-1, ", ")
            self.inner.insert(-1, other)
            return self

        if isinstance(other, str):
            if not other.startswith('"') and not other.endswith('"'):
                other = f'"{other}"'
            return elem_math(self, other, lambda a,b: a + b, self._space_sign("&"))
        return elem_math(self, other, lambda a,b: a + b, self._space_sign("+"))

    def __radd__(self, other):
        from excelbird.core.function import Func
        if other == 0:  # Adding to zero signals the beginning of python sum() evaluation
            return Func("SUM(", self, ")", _is_python_sum = True)

        if isinstance(other, Func) and other._is_python_sum is True:
            other.inner.insert(-1, ", ")
            other.inner.insert(-1, self)
            return other

        if isinstance(other, str):
            if not other.startswith('"') and not other.endswith('"'):
                other = f'"{other}"'
            return elem_math(other, self, lambda a,b: a + b, self._space_sign("&"))
        return elem_math(other, self, lambda a,b: a + b, self._space_sign("+"))

    def __sub__(self, other):
        return elem_math(self, other, lambda a,b: a - b, self._space_sign("-"))

    def __rsub__(self, other):
        return elem_math(other, self, lambda a,b: a - b, self._space_sign("-"))


    def __mul__(self, other):
        return elem_math(self, other, lambda a,b: a * b, self._space_sign("*"))

    def __rmul__(self, other):
        return elem_math(other, self, lambda a,b: a * b, self._space_sign("*"))


    def __truediv__(self, other):
        return elem_math(self, other, lambda a,b: a / b, self._space_sign("/"))

    def __rtruediv__(self, other):
        return elem_math(other, self, lambda a,b: a / b, self._space_sign("/"))


    def __xor__(self, other):
        return elem_math(self, other, lambda a,b: a ^ b, self._space_sign("^"))

    def __rxor__(self, other):
        return elem_math(other, self, lambda a,b: a ^ b, self._space_sign("^"))


    def __pow__(self, other):
        return elem_math(self, other, lambda a,b: a ^ b, self._space_sign("^"))

    def __rpow__(self, other):
        return elem_math(other, self, lambda a,b: a ^ b, self._space_sign("^"))


    def __rshift__(self, other):
        return elem_math(self, other, lambda a,b: a >> b, ":")

    def __rrshift__(self, other):
        return elem_math(self, other, lambda a,b: a >> b, ":")


    def __and__(self, other):
        if isinstance(other, str):
            if not other.endswith('"') and not other.startswith('"'):
                other = f'"{other}"'
        return elem_math(self, other, lambda a,b: a & b, self._space_sign("&"))

    def __rand__(self, other):
        if isinstance(other, str):
            if not other.endswith('"') and not other.startswith('"'):
                other = f'"{other}"'
        return elem_math(self, other, lambda a,b: a & b, self._space_sign("&"))
