.. excelbird documentation master file, created by
   sphinx-quickstart on Fri Jan 27 16:03:43 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Excelbird Documentation
=======================

.. role:: html(raw)
    :format: html


A markup language, front-end framework, and dataframe library all in one. For Excel.

Excelbird is the tool for *rapid* development of complex, functional Excel workbooks with styling,
formulas, and cell references, all in **Python**.

Excelbird is **not** a scripting library. There is no such thing as cell ``A1``, and there
are no grid coordinates. Your layout is *fluid*, like an html page.


.. grid:: 2

    .. grid-item-card::
        :link: /intro/main
        :link-type: doc

        :doc:`Getting Started </intro/main>`
        ^^^

:html:`<h4>Layout Elements</h4>`

.. grid:: 3

    .. grid-item-card::
        :link: /cell/main
        :link-type: doc

        Value
        ^^^
        :class:`Cell <excelbird.Cell>`

    .. grid-item-card::
        :link: /series/main
        :link-type: doc

        Series
        ^^^
        :class:`Col <excelbird.Col>` | :class:`Row <excelbird.Row>`


    .. grid-item-card::
        :link: /frame/main
        :link-type: doc

        DataFrame
        ^^^
        :class:`Frame <excelbird.Frame>` | :class:`VFrame <excelbird.VFrame>`

.. grid:: 2

    .. grid-item-card::
        :link: /stack/main
        :link-type: doc

        Container
        ^^^
        :class:`Stack <excelbird.Stack>` | :class:`VStack <excelbird.VStack>`

    .. grid-item-card::
        :link: /workbook/main
        :link-type: doc

        Workbook
        ^^^
        :class:`Sheet <excelbird.Sheet>`, :class:`Book <excelbird.Book>`


:html:`<h4>Dynamic Elements</h4>`

.. grid:: 2

    .. grid-item-card::
        :link: /gap/main
        :link-type: doc

        :class:`Gap <excelbird.Gap>`
        ^^^

        Apply spacing

    .. grid-item-card::
        :link: /item/main
        :link-type: doc

        :class:`Item <excelbird.Item>`
        ^^^

        Let the parent container decide

    .. grid-item-card::
        :link: /expr/main
        :link-type: doc

        :class:`Expr <excelbird.Expr>`
        ^^^

        Execute code on elements not assigned to variables

    .. grid-item-card::
        :link: /func/main
        :link-type: doc

        :class:`Func <excelbird.Func>`
        ^^^

        Call Excel built-in functions



.. toctree::
   api
