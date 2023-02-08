# 3.11
from __future__ import annotations
from typing import overload

class Func:
    def __init__(self, fn, id=None, res_type: type | None = None):
        print("fn init called")
        self.fn = fn
        self.id = id
        self.res_type = res_type

class Expr:
    def __init__(self, expr, id=None, res_type: type | None = None):
        print("expr init called")
        self.expr = expr
        self.id = id
        self.res_type = res_type

class A:
    @overload
    def __new__(cls, expr: str | set, **kwargs) -> Expr:
        ...

    @overload
    def __new__(cls, fn: str | set, **kwargs) -> Func:
        ...

    @overload
    def __new__(cls, *args, **kwargs) -> A:
        ...

    def __new__(cls, *args, mul=None, expr=None, fn=None, **kwargs):
        print("A new called")
        if mul is not None:
            new_fns = [cls.__new__(cls, expr=expr, fn=fn, **kwargs) for _ in range(mul)]
            for i, elem in enumerate(new_fns):
                if isinstance(elem, cls):
                    elem.__init__(*args, **kwargs)
            return new_fns

        if expr is not None:
            new_expr = super().__new__(Expr)
            new_expr.__init__(expr, res_type=A, **kwargs)
            return new_expr

        if fn is not None:
            new_fn = super().__new__(Func)
            new_fn.__init__(fn, res_type=A, **kwargs)
            return new_fn


        return super().__new__(cls)

    def __init__(self, arg1=None, arg2=None, arg3=None, expr=None, fn=None):
        del expr, fn
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

stuff = A(5, mul=5)

print([x.arg1 for x in stuff])
