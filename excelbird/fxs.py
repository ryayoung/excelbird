"""
Alternate version of fx. The goal of these functions
is simply to make writing complex nested Funcs easier,
so that you don't have to put your entire Func string inside
one long string.

Instead of...

'''
MAX(
  NETWORKDAYS(
    MAX({forecast_start_date}, {date_start}),
    {date_end},
    IF(
      OR({loc}="Offshore", {loc}="Nearshore"),
      0,
      {[holidays].range()}
    )
  ),
  0
)
'''

You can now use:

MAX(
    NETWORKDAYS(
        MAX("{forecast_start_date}, {date_start}"),
        "{date_end}",
        IF(
            OR("{loc}='Offshore', {loc}='Nearshore'"),
            0,
            "{[holidays].range()}"
        )
    ),
    0
)

"""
