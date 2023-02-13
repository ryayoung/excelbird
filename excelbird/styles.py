"""
.. note::
    
    Source code for this module is displayed at the bottom of this page

The following styles contain dictionaries **to be unpacked** as keyword arguments
into an excelbird layout element, using the ``**`` operator. Here's an
example of how that's done

.. code-block::

    from excelbird.styles import conditional
    from excelbird import Cell

    bad_cell = Cell(10, id='bad_cell', **conditional.bad)

**default_table_style** : dict

* The style applied by default when setting ``table_style=True``. See the source code below
  for the exact attributes passed

**conditional** : dict

* Format cells as 'good', 'bad', or 'neutral', by applying fill color and font
  color as seen in Excel's default conditional formatting styles.
* Keys : ``good``, ``bad``, ``neutral``

Source code
--------------

.. literalinclude:: ../../../excelbird/styles.py

"""
from excelbird._base.dotdict import Style
from excelbird.colors import conditional as cond_color

default_table_style = Style(
    name="TableStyleMedium2",
    showRowStripes=True,
)

conditional=Style(
    good=Style(
        fill_color=cond_color.light_green,
        color=cond_color.dark_green,
    ),
    bad=Style(
        fill_color=cond_color.light_red,
        color=cond_color.dark_red,
    ),
    neutral=Style(
        fill_color=cond_color.light_yellow,
        color=cond_color.dark_yellow,
    ),
),

