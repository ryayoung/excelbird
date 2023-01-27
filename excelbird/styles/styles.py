from excelbird._base.dotdict import Style
from excelbird.styles.colors import conditional

"""
Styles
------
default_table_style:
    Used when setting ``table_style=True`` for a ``Frame``
conditional:
    Formats cells as 'good', 'bad', or 'neutral', by applying fill color and font
    color as seen in Excel's default conditional formatting styles.
"""

default_table_style = Style(
    name="TableStyleMedium2",
    showRowStripes=True,
)

conditional=Style(
    good=Style(
        fill_color=conditional.light_green,
        color=conditional.dark_green,
    ),
    bad=Style(
        fill_color=conditional.light_red,
        color=conditional.dark_red,
    ),
    neutral=Style(
        fill_color=conditional.light_yellow,
        color=conditional.dark_yellow,
    ),
),

