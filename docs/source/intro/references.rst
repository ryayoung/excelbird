Expr: The Lazy Expression
============================

.. _references_main:

Code readability is central to excelbird's design. Therefore, we've given you the tools needed
to let you build an entire workbook (and some of its logic) in a single line of code, without creating
any variables other than your input data. This is great. It means your Book layout can be read the
way its output will look: in sequential order. The logic, references, and design features in an
element can be isolated to that element's location in your layout.

To accomplish this, we must be able to reference elements that either aren't assigned to variables,
or may not even exist yet. For instance, say you want to design a Sheet that has a table
at the bottom, and some summary statistics at the top that reference columns in the table. Normally,
you'd need to create the table first, and then declare the summary section which reference it. Then,
your code reads backwards. That's no fun.

Before any explanation, here's an example of how this is solved in excelbird.

Cell **A1** in **Sheet1** will read ``=A2 + B2 + Sheet2!A1``:

.. code-block::

    Book(
        Sheet(
            Cell(ex="[one] + [two] + [three]"),
            Row(
                Cell(1, id="one"),
                Cell(2, id="two"),
            )
        ),
        Sheet(
            Cell(3, id="three")
        ),
    ).write()


Global Identifiers and Lazy Evaluation
----------------------------------------
Every excelbird object has an :attr:`id` property (some have a :attr:`header` too) which, when set, 
saves a pointer to **itself** in memory, so it can be found from anywhere else in the Book.

As explained before, the whole Book layout is lazily evaluated - triggered only when ``.write()`` is called.
This means that *when* you set an element's identifier has no effect on *when* you can reference it.

This solves the problem identified earlier: You can arrange a summary card that sums/averages some columns
in a table that will be arranged later, without creating variables for the summary card or table.


The 'Expr' Element
-------------------------

Python has a builtin function :meth:`eval` which takes a string and executes it as code:
``eval("1 + my_variable")`` is the same as ``1 + my_variable``.

:class:`xb.Expr <excelbird.Expr>` works just like `eval`, but instead of real variable names, you'll reference the id or header
of an element in your layout, and it will wait until each reference is found before executing.

If you would normally say,

.. code-block::

    my_cell = Cell(1)
    other = my_cell + 5

You can instead write,

.. code-block::

    my_cell = Cell(1, id="my_cells_id")
    other = Expr("[my_cells_id] + 5")

The difference? **Order doesn't matter anymore**

.. code-block::

    other = Expr("[my_cells_id] + 5")
    my_cell = Cell(1, id="my_cells_id")

Another difference? **You no longer need to reference the** ``my_cell`` **variable**

.. code-block::

    Book(
        Sheet(
            Expr("[my_cells_id] + 5"),
            Cell(1, id="my_cells_id"),
        )
    ).write()

This code can still be improved: it's not clear to the reader which type
will be returned when the Expr executes. Instead...

.. code-block::

    Book(
        Sheet(
            Cell(ex="[my_cells_id] + 5"),
            Cell(1, id="my_cells_id"),
        )
    ).write()

The ``ex`` argument was intercepted before Cell's constructor could be called, and an Expr was returned instead

Not only is this more readable, but the returned Expr has been told that it's supposed to
return a Cell when it executes, and if it doesn't (perhaps ``my_cells_id`` is actually a column header),
a descriptive error will be raised to help you fix the problem

.. danger::

   Expr creation by use of the ``ex`` argument is only *recommended* when creating
   the element from *inside* your layout, as shown above, rather than by assigning to a variable.
   The ability to intercept arguments like ``ex`` and return an instance of a different class
   is an unusual strategy, and can cause serious confusion for a reader who sees a variable
   assigned to a certain type, only to find out it's a different type. It's justified in the
   use-case above because if no variable is declared, there's no way to interact with the
   element directly, and thus no chance of confusion.

