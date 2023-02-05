"""
A :class:`Func <excelbird.Func>` is a template that dynamically returns an
element of the appropriate shape/dimensions while applying an Excel formula to its
cell(s). It should be used **only when calling builtin Excel functions** in your formula.

As standard across excelbird, a Func is designed for use without
specifying any cell coordinates.

Syntax
------
To build a :class:`Func <excelbird.Func>`, provide the *exact* formula string,
with Python objects placed wherever the cell references should appear.

For instance, here's how it should look if you were **not** referencing any cells.

.. code-block::

    from excelbird import Func, Cell

    simple_func = Func("SUM(5, 4, MIN(6, 7))")

To reference other layout elements in your formula, there are two options:

Referencing Elements - Option 1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Break the string, and insert variables directly**. Be warned, this option
can be clumsy, tedious, and cause mistakes.

Let's rewrite the above example, but instead of
hardcoding `5` and `4`, reference :class:`Cells <excelbird.Cell>` containing them.

.. code-block::

    five = Cell(5)
    four = Cell(4)
    another_func = Func("SUM(", five, ", ", four, ", MIN(6, 7))")

Notice the comma we had to insert manually between `five` and `four`

.. note::

    The above technique can be clumsy and prone to user-error. Its only
    benefit is improved speed, and that it doesn't require any knowledge
    of object `ids`, `headers`, and :class:`Expr <excelbird.Expr>`.

Referencing Elements - Option 2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Templated** :class:`Expr <excelbird.Expr>`. Please read the intro to `Expr` if
you aren't familiar with them yet.

.. code-block::

    better_func = Func("SUM({{cell_five}}, {{cell_four}}, MIN(6, 7))")
    five = Cell(5, id="cell_five")  # ^ Exprs can reference stuff that doesn't exist yet.
    four = Cell(4, id="cell_four")

`Why` did we use braces ``{{...}}`` instead of square bracktets ``[...]`` like we do with `Expr`?

Because we weren't referencing variables. We were inserting Exprs.

**In an Expr, square brackets enclose an id or header. In a Func, curly braces enclose an Expr**

To illustrate this, let's make our Expr execute some python code. We'll add cells five and four
together, instead of listing them. For reference, in **option 1** this would look like
``Func("SUM(", five + four, ", MIN(6, 7))")``

.. code-block::

    Func("SUM({{[cell_five] + [cell_four]}}, MIN(6, 7))")

Which is equivalent to

.. code-block::

    Func("SUM(", Expr("[cell_five] + [cell_four]"), ", MIN(6, 7))")

**Why are the braces necessary? Why can't I just use square brackets alone?**

Because in an Expr, the entire contents of the string is treated as *valid Python code* and **is executed**.
This allows for things like ``Expr("[row_header].range() + [col_header].loc[3:]")``. If you
placed that string inside a Func, we can't know whether the ``.range``, ``.loc``,
or ``+`` should be executed in Python or included as exact strings inside the Excel formula.

**Double braces are strongly recommended, but ANY number of curly braces are allowed**. i.e. ``{{{stuff}}}``, ``{{stuff}}``,
or ``{stuff}`` are each valid. This is a design feature to ensure your code reads and is interpreted the same regardless of whether
your string is `an f-string <https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/>`_ as long
as you've used **at least two** braces.

----

Here is an **impractical** example that demonstrates a variety of syntax used together.

.. code-block::

    my_cell = Cell(69)
    Func("SUM(", {"foo"}, ", ", my_cell, None, ", ", Expr("bar"), ", SUM({{[one] * [two]}}, {{some_elem}}) + ", 5, ")")

will build a formula that's arranged like:

.. code-block::

    =SUM(<Expr>, 99, <Cell>, SUM(<Expr>, <Expr>) + 5)

where the second `Expr` is the result of ``Expr("[one] * [two]")`` and the
third `Expr` is the result of ``Expr("some_elem")``. Notice the value of
``None`` was ignored, which is a feature shared by all excelbird layout elements
to allow for conditional placement of elements.

Additional Arguments - res_type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Keyword argument :attr:`res_type` can be used to specify the type of the object returned
by Func. This is **not** necessary inside structured parent containers like :class:`Frame <excelbird.Frame>`
or :class:`Row <excelbird.Row>` which will make this decision automatically. However, inside
unstructured containers like :class:`Stack <excelbird.Stack>` or :class:`Sheet <excelbird.Sheet>` it will
need to be specified.

For instance, in the following example, the parent Frame will decide that ``res_type`` must be
:class:`Col <excelbird.Col>` so no user input is needed.

.. code-block::

    Frame(
        Col(1, 2, 3, header="first"),
        Col(2, 7, 1, header="second"),
        Func("MAX({{first}}, {{second}})", header="third"),
    )

However, if we placed those elements inside a Stack, now we have
some flexibility and need to make a choice.
Should the returned element be a Col containing the max of each pair across the other vectors?
Or do we want the single largest value across the other two columns returned as a Cell? Try both:

.. code-block::

    Stack(
        Func("MAX({{first}}, {{second}})", res_type=Cell),
        Col(1, 2, 3, header="first"),
        Col(2, 7, 1, header="second"),
        Func("MAX({{first}}, {{second}})", header="third", res_type=Col),
    )

"""
from __future__ import annotations
import re
from typing import Any
from itertools import zip_longest
from itertools import chain

from excelbird.core.expression import Expr
from excelbird._base.math import CanDoMath

from excelbird._utils.util import (
    get_dimensions,
)
from excelbird._utils.argument_parsing import (
    convert_all_to_type
)

class Func(CanDoMath):
    """
    Create a formula that uses builtin Excel functions. One `Func` does *not* correspond
    to a single call to an Excel function, but rather to the entire formula. Therefore, you
    cannot nest ``Func`` inside one another, nor would there be any reason to.

    .. note::

        `Func` should *only* be used if calling **builtin Excel functions**. If just
        arithmetic is needed to build your formula (i.e. adding/subtracting things), you
        can execute the expression **directly in Python** on layout elements, and optionally
        do so by referencing elements by id/header using an :class:`Expr`.

    Parameters
    ----------
    *inner : Any
        Pass each section of the formula as positional arguments
    res_type : type, optional
        Desired return type. This is rarely needed, since often you'll be placing ``Func``
        inside a container that can only hold one type, so ``res_type`` is inferred.
        In some cases though, such as when inside a ``Stack``, or when being used in a
        math expression prior to being placed in a layout, this will need to be specified.
    **kwargs : Any
        Any additional keyword arguments will be passed to the constructor of the resulting
        object.

    """

    def __init__(
        self,
        *inner,
        res_type: type | None = None,
        _is_python_sum: bool = False,
        **kwargs,
    ) -> None:
        """
        All that is needed is the res type and a list of elements.
        Define the function in its exact form, including all characters,
        including parentheses, except the beginnning equals sign. Separate
        out the dynamic elements into their own list elements, which can either
        be an Expression, set, Cell or series.

        If res type is a cell, call .range()
        """
        if len(inner) == 1:
            if type(inner[0]) in (list, tuple):
                inner = inner[0]

        inner = list(inner)

        inner = self._parse_args(inner)

        if len(inner) == 0:
            raise ValueError("No elements provided to Func")

        if any(isinstance(i, Func) for i in inner):
            raise ValueError("Cannot nest Funcs inside one another, as there is no need to do so.")

        self.res_type = res_type
        self.inner = inner
        self._is_python_sum = _is_python_sum
        self.kwargs = kwargs

    def set(self, **kwargs) -> Func:
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
            else:
                self.kwargs[k] = v
        return self

    def _parse_args(self, args) -> list:
        def extract_exprs_from_string(s: str):
            matches = [Expr(s) for s in re.findall(r"\{+(.*?)\}+", s)]
            splits = re.split(r"\{+.*?\}+", s)
            sub_args = [x for x in chain.from_iterable(zip_longest(splits, matches)) if x]
            return sub_args

        def is_str_containing_expr(s: Any) -> bool:
            if isinstance(s, str):
                if "{" in s:
                    return True
            return False

        return list(
            chain.from_iterable(
                [
                    [Expr(elem.pop())] if isinstance(elem, set)
                    else [elem] if not is_str_containing_expr(elem)
                    else extract_exprs_from_string(elem)
                    for elem in args if elem is not None
                ]
            )
        )


    def _get_function(self, container_type: type | None = None):
        if self.res_type is None:
            if container_type is None:
                raise ValueError(
                    "Can't determine the result type of function. Please provide "
                    "`res_type` as a keyword argument to Func, with the desired return type."
                )
            else:
                from excelbird.core.frame import Frame, VFrame
                from excelbird.core.series import Col, Row
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

        if self._all_resolved() is False:
            raise ValueError("All references must be resolved before calling .get_function()")

        dimensions = get_dimensions(self.res_type)
        assert dimensions >= 0, f"Invalid res_type, {self.res_type}"

        if dimensions == 0:
            # Since we're only returning one cell, we need to take each element
            # which is larger than a cell, and only refer to its range
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


    def _exprs(self) -> list:
        return [i for i in self.inner if isinstance(i, Expr)]

    def _all_resolved(self) -> bool:
        if any(i._refs_resolved() is False for i in self._exprs()):
            return False
        return True
    
    def _attempt_to_resolve(self, container: list) -> bool:
        """
        Given a parent container, try to resolve each expression
        in self's `inner`.
        """
        for i, elem in enumerate(self.inner):
            if isinstance(elem, Expr):
                if elem._attempt_to_resolve(container) is True:
                    self.inner[i] = elem._eval()

        return self._all_resolved()

    @classmethod
    def _resolve_container_recursive(cls, container: list) -> bool:
        """
        For each _DelayedFunc in a container, attempt to resolve each of
        its expressions.

        Returns True if all were resolved

        Mutates inplace: `container`
        """
        all_dfuncs_resolved = True

        for i, elem in enumerate(container):
            if isinstance(elem, cls):

                if elem._attempt_to_resolve(container) is True:
                    container[i] = elem._get_function(type(container))
                else:
                    all_dfuncs_resolved = False

            elif isinstance(elem, list):
                if cls._resolve_container_recursive(elem) is False:
                    all_dfuncs_resolved = False

        return all_dfuncs_resolved

    def __repr__(self):
        if self.res_type is not None:
            return f"{type(self).__name__}({self.res_type.__name__}...)"
        return f"{type(self).__name__}(...)"

