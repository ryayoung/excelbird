Layout Tree Structure
=======================

.. _layout_main:

.. dropdown:: :octicon:`chevron-left` :octicon:`chevron-right`

    .. code-block::

        Book(
            Sheet(
                # Structured container: Frame, Col/Row, Cell
                Frame(
                    Col(
                        Cell(1),
                        Cell(2),
                        Cell(3),
                        Cell(4),
                    ),
                    Col(
                        Cell(1),
                        Cell(2),
                        Cell(3),
                        Cell(4),
                    ),
                ),
                # Unstructured container: Stack, Sheet
                Stack(
                    Cell(1),
                    Row(1, 2, 3),
                    Col(5, 6, 7),
                    Frame([[10,20], [30, 40]]),
                )
            )
        ).write(path)


1D Vector
-----------

A series :attr:`header <excelbird.Col.header>` attribute is special, and doesn't act like a normal cell.
:ref:`Read more about headers <header>`

.. .. dropdown:: :octicon:`chevron-left` :octicon:`chevron-right`
..
..     .. code-block::
..
..         from excelbird import Col, Row
..         my_col = Col(1, 2, 3, header="header")
..         my_row = Row(1, 2, 3, header="header")
..         # Or, just transpose `my_col` and get same result
..         my_row = my_col.transpose(inherit_style=True)
    

.. grid::
    :margin: 0

    .. grid-item::
        :columns: 3

        .. card:: :class:`Col <excelbird.Col>`
            :link: ../series/main
            :link-type: doc

            .. image:: ../assets/col.png
                :width: 50

    .. grid-item::
        :columns: 6

        .. card:: :class:`Row <excelbird.Row>`
            :link: ../series/main
            :link-type: doc

            .. image:: ../assets/row.png
                :width: 200

2D Vector
--------------

.. .. dropdown:: :octicon:`chevron-left` :octicon:`chevron-right`
..
..     This code assumes ``my_col`` and ``my_row`` are placed somewhere
..     in the same workbook. Although not shown in the images, each cell
..     (headers excluded) in the frames below will contain cell references to
..     the locations of ``my_col`` and ``my_row``
..
..     .. code-block::
..
..         from excelbird import Frame, VFrame
..         fr = Frame(
..             my_col,
..             my_col.ref(header='header'),
..             my_col.ref(),
..             my_col.ref(header='header'),
..         )
..         vfr = VFrame(
..             my_row,
..             my_row.ref(header='header'),
..             my_row.ref(),
..             my_row.ref(header='header'),
..         )
..         # Or, just transpose `fr` and get same result
..         vfr = fr.transpose(inherit_style=True)

.. grid::
    :margin: 0

    .. grid-item::
        :columns: 6

        .. card:: :class:`Frame <excelbird.Frame>`
            :link: ../frame/main
            :link-type: doc
            
            .. image:: ../assets/frame.png
                :width: 200

    .. grid-item::
        :columns: 6

        .. card:: :class:`VFrame <excelbird.VFrame>`
            :link: ../frame/main
            :link-type: doc
            
            .. image:: ../assets/vframe.png
                :width: 200


Unstructured Container
---------------------------

Stacks can hold anything, just like an html ``<div>``, but they can't be used in
expressions. They offer unique styling features not available to other elements, like
:attr:`margin <excelbird.Stack.margin>` and :attr:`padding <excelbird.Stack.padding>`

.. grid::
    :margin: 0

    .. grid-item::
        :columns: 12

        .. card:: :class:`Stack <excelbird.Stack>`
            :link: ../stack/main
            :link-type: doc
            
            .. image:: ../assets/stack.png
                :width: 450

.. grid::
    :margin: 0

    .. grid-item::
        :columns: 12

        .. card:: :class:`VStack <excelbird.VStack>`
            :link: ../stack/main
            :link-type: doc
            
            .. image:: ../assets/vstack.png
                :width: 200


Worksheet
---------------

Sheets handle children just like :class:`VStack <excelbird.VStack>`.

.. grid::
    :margin: 0

    .. grid-item::
        :columns: 12

        .. card:: :class:`Sheet <excelbird.Sheet>`
            :link: ../workbook/main
            :link-type: doc
            
            .. image:: ../assets/vstack.png
                :width: 200















