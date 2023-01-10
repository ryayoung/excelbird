from excelbird.base_types import Style
from excelbird.colors import conditional

default_table_style = Style(
    name="TableStyleMedium2",
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

from openpyxl.styles.numbers import (
    BUILTIN_FORMATS as xl_fmt,
)
formats = Style(
    general='General',
    int='0',
    float='0.00',
    comma_int='#,##0',
    comma_float='#,##0.00',
    percent_int=xl_fmt[9],
    percent_float=xl_fmt[10],
    usd_int=xl_fmt[5],
    usd_float=xl_fmt[7],
    accounting_int=xl_fmt[42],
    accounting_float=xl_fmt[44],
)

# Openpyxl formats
BUILTIN_FORMATS = {
    0: 'General',
    1: '0',
    2: '0.00',
    3: '#,##0',
    4: '#,##0.00',
    5: '"$"#,##0_);("$"#,##0)',
    6: '"$"#,##0_);[Red]("$"#,##0)',
    7: '"$"#,##0.00_);("$"#,##0.00)',
    8: '"$"#,##0.00_);[Red]("$"#,##0.00)',
    9: '0%',
    10: '0.00%',
    11: '0.00E+00',
    12: '# ?/?',
    13: '# ??/??',
    14: 'mm-dd-yy',
    15: 'd-mmm-yy',
    16: 'd-mmm',
    17: 'mmm-yy',
    18: 'h:mm AM/PM',
    19: 'h:mm:ss AM/PM',
    20: 'h:mm',
    21: 'h:mm:ss',
    22: 'm/d/yy h:mm',

    37: '#,##0_);(#,##0)',
    38: '#,##0_);[Red](#,##0)',
    39: '#,##0.00_);(#,##0.00)',
    40: '#,##0.00_);[Red](#,##0.00)',

    41: r'_(* #,##0_);_(* \(#,##0\);_(* "-"_);_(@_)',
    42: r'_("$"* #,##0_);_("$"* \(#,##0\);_("$"* "-"_);_(@_)',
    43: r'_(* #,##0.00_);_(* \(#,##0.00\);_(* "-"??_);_(@_)',

    44: r'_("$"* #,##0.00_)_("$"* \(#,##0.00\)_("$"* "-"??_)_(@_)',
    45: 'mm:ss',
    46: '[h]:mm:ss',
    47: 'mmss.0',
    48: '##0.0E+0',
    49: '@',
}