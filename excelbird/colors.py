"""
.. note::
    
    Source code for this module is displayed at the bottom of this page

**mono**

* Keys : ``white``, ``black``, and 10 colors in between: ``gray0`` (95% white) - ``gray9`` (10% white)

**theme**

* The default colors found in "Theme Colors" section of the color selection panel in Excel.
* Contains **6 shades** of each of the following

  * light
  * dark
  * tan
  * dark_blue
  * light_blue
  * red
  * green
  * purple
  * aqua
  * orange

* For each of the colors above, the keys for each shade follow the pattern

  * ``<color>`` (primary)
  * ``<color>1`` (lightest)
  * ``<color>2``
  * ``<color>3``
  * ``<color>4``
  * ``<color>5`` (darkest)

* Example: ``excelbird.colors.theme.red3``

**theme_groups**

* Stores all 6 shades of each color in ``theme`` as a list, so they can be accessed dynamically.
* For instance, ``theme.red3`` is the same as ``theme_groups.red[3]``

**standard**

* Default colors found in the "Standard Colors" section of the color selection panel in Excel
* Colors

  * dark_red
  * red
  * orange
  * yellow
  * light_green
  * green
  * light_blue
  * blue
  * dark_blue
  * purple

**conditional**

* Default colors used by Excel's conditional formatting feature. Consists of a fill-color/font-color combo
  for 'good' (green), 'bad' (red) and 'neutral' (yellow).
* Keys : ``light_green`` & ``dark_green``, etc. (same pattern for 'red' and 'yellow')

Source code
-------------

.. literalinclude:: ../../../excelbird/colors.py

"""
from excelbird._base.dotdict import Style

conditional = Style(
    light_green="C6EFCE",
    dark_green="006100",
    light_yellow="FFEB9C",
    dark_yellow="9C6500",
    light_red="FFC7CE",
    dark_red="9C0006",
)
mono = Style(
    white="FFFFFF",
    gray9="1A1A1A",  # 10%
    gray8="333333",  # 20%
    gray7="4D4D4D",  # 30%
    gray6="666666",  # 40%
    gray5="808080",  # 50%
    gray4="999999",  # 60%
    gray3="B3B3B3",  # 70%
    gray2="CCCCCC",  # 80%
    gray1="E6E6E6",  # 90%
    gray0="F3F3F3",  # 95%
    black="000000",
)
standard = Style(
    dark_red="C00000",
    red="FF0000",
    orange="FFC000",
    yellow="FFFF00",
    light_green="92D050",
    green="00B050",
    light_blue="00B0F0",
    blue="0070C0",
    dark_blue="002060",
    purple="7030A0",
)
theme = Style(
    light="FFFFFF",
    light1="F2F2F2",
    light2="D9D9D9",
    light3="BFBFBF",
    light4="A6A6A6",
    light5="808080",
    dark="000000",
    dark1="808080",
    dark2="595959",
    dark3="404040",
    dark4="262626",
    dark5="0D0D0D",
    tan="EEECE1",
    tan1="DDD9C4",
    tan2="C4BD97",
    tan3="948A54",
    tan4="494529",
    tan5="1D1B10",
    dark_blue="1F497D",
    dark_blue1="C5D9F1",
    dark_blue2="8DB4E2",
    dark_blue3="538DD5",
    dark_blue4="16365C",
    dark_blue5="0F243E",
    light_blue="4F81BD",
    light_blue1="DCE6F1",
    light_blue2="B8CCE4",
    light_blue3="95B3D7",
    light_blue4="366092",
    light_blue5="244062",
    red="C0504D",
    red1="F2DCDB",
    red2="E6B8B7",
    red3="DA9694",
    red4="963634",
    red5="632523",
    green="9BBB59",
    green1="EBF1DE",
    green2="D8E4BC",
    green3="C4D79B",
    green4="76933C",
    green5="4F6228",
    purple="8064A2",
    purple1="E4DFEC",
    purple2="CCC0DA",
    purple3="B1A0C7",
    purple4="60497A",
    purple5="403151",
    aqua="4BACC6",
    aqua1="DAEEF3",
    aqua2="B7DEE8",
    aqua3="92CDDC",
    aqua4="31869B",
    aqua5="215967",
    orange="F79646",
    orange1="FDE9D9",
    orange2="FCD5B4",
    orange3="FABF8F",
    orange4="E26B0A",
    orange5="974706",
)

theme_groups = Style(
    light=[
        theme.light,
        theme.light1,
        theme.light2,
        theme.light3,
        theme.light4,
        theme.light5,
    ],
    dark=[
        theme.dark,
        theme.dark1,
        theme.dark2,
        theme.dark3,
        theme.dark4,
        theme.dark5,
    ],
    tan=[
        theme.tan,
        theme.tan1,
        theme.tan2,
        theme.tan3,
        theme.tan4,
        theme.tan5,
    ],
    dark_blue=[
        theme.dark_blue,
        theme.dark_blue1,
        theme.dark_blue2,
        theme.dark_blue3,
        theme.dark_blue4,
        theme.dark_blue5,
    ],
    light_blue=[
        theme.light_blue,
        theme.light_blue1,
        theme.light_blue2,
        theme.light_blue3,
        theme.light_blue4,
        theme.light_blue5,
    ],
    red=[
        theme.red,
        theme.red1,
        theme.red2,
        theme.red3,
        theme.red4,
        theme.red5,
    ],
    green=[
        theme.green,
        theme.green1,
        theme.green2,
        theme.green3,
        theme.green4,
        theme.green5,
    ],
    purple=[
        theme.purple,
        theme.purple1,
        theme.purple2,
        theme.purple3,
        theme.purple4,
        theme.purple5,
    ],
    aqua=[
        theme.aqua,
        theme.aqua1,
        theme.aqua2,
        theme.aqua3,
        theme.aqua4,
        theme.aqua5,
    ],
    orange=[
        theme.orange,
        theme.orange1,
        theme.orange2,
        theme.orange3,
        theme.orange4,
        theme.orange5,
    ],
)
