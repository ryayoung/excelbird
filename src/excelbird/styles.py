from excelbird.base_types import Style
from excelbird.colors import colors

default_table_style = Style(
    name="TableStyleMedium2",
)



styles = Style(
    conditional=Style(
        good=Style(
            fill_color=colors.conditional.light_green,
            color=colors.conditional.dark_green,
        ),
        bad=Style(
            fill_color=colors.conditional.light_red,
            color=colors.conditional.dark_red,
        ),
        neutral=Style(
            fill_color=colors.conditional.light_yellow,
            color=colors.conditional.dark_yellow,
        ),
    ),
)