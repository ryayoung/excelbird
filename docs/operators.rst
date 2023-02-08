Python Operators
================

The table below shows what built-in Python operators correspond to
in Excel when excelbird objects are used in arithmetic python expressions,
i.e. ``product = my_row * my_col``. 

.. note:: 

    Excelbird tries to mimic Excel syntax wherever possible, but in a handful of cases
    this cannot be done.

    * ``a = b:c`` is invalid Python. Use ``a = b >> c`` instead
    * ``<>`` is invalid anywhere in Python. Use ``!=`` instead.
    * ``a_percent = a%`` is invalid. Instead use ``a_percent = a % a`` where both ``a`` are the same object


.. list-table:: Operators
   :widths: 25 25 25 25
   :header-rows: 1

   * - Python
     - Excel
   * - ``a >> b``
     - ``=a:b``
   * - ``a >> b``
     - ``=a:b``


``__rshift__(a, b)``
    * ``a >> b`` --> ``=a:b``

``__eq__(a, b)``
    * ``a == b`` --> ``=a = b``

``__ne__(a, b)``
    * ``a != b`` --> ``=a <> b``

``__lt__(a, b)`` / ``__gt__(a, b)``
    * ``a < b`` / ``a > b`` --> ``=a < b`` / ``=a > b``

``__le__(a, b)`` / ``__ge__(a, b)``
    * ``a <= b`` / ``a >= b` --> ``=a <= b`` / ``=a >= b``

``__add__(a, b)``
    * ``a + b`` --> ``=a ^ b``

``__and__(a, b)``
    * ``a & b`` --> ``=a & b``
    * note - Strings will be surrounded in double quotes

``__sub__(a, b)``
    * ``a - b`` --> ``=a - b``

``__mul__(a, b)``
    * ``a * b`` --> ``=a * b``

``__truediv__(a, b)``
    * ``a / b`` --> ``=a / b``

``__pow__(a, b)``
    * ``a ** b`` --> ``=a ^ b``

``__xor__(a, b)``
    * ``a ^ b`` --> ``=a ^ b``

``__or__(a, b)``
    * ``a | b`` --> ``=OR(a, b)``

``__mod__(a, b)``
    * ``a % b`` --> ``=MOD(a, b)``
    * ``a % a`` --> ``=a%``
    * NOTE: Passing the *same* object on both sides of the expression (i.e. ``my_var % my_var``)
      will call excel's shorthand percent conversion and return ``=my_var%``

``__round__(a, b)``
    * ``round(a, b)`` --> ``=ROUND(a, b)``

``__abs__(x)``
    * ``abs(x)`` --> ``=ABS(x)``

``__invert__(x)``
    * ``~ x`` -> ``=NOT(x)``

``__trunc__(x)``
    * ``math.trunc(x)`` -> ``=TRUNC(x)``

``__floor__(x)``
    * ``math.floor(x)`` -> ``=FLOOR(x, 1)``

``__ceil__(x)``
    * ``math.ceil(x)`` -> ``=CEILING(x, 1)``
