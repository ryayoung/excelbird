from excelbird.base_types import Style
from excelbird.colors import conditional

default_table_style = Style(
    name="TableStyleMedium2",
)



styles = Style(
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
)
