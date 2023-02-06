"""
    pygments.styles.pastie
    ~~~~~~~~~~~~~~~~~~~~~~

    Style similar to the `pastie`_ default style.

    .. _pastie: http://pastie.caboo.se/

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Other, Token, Literal, Punctuation

PURPLE = "#8250df"
RED = "#CF222E"
BROWN = "#953800"  # Class names, constants
BLUE = "#0550AE"  # arithmetic operators, numbers, builtin in/and, True/F, None
DARK_BLUE = "#0A3069"  # strings, quotes, docstrings
GRAY = "#6E7781"  # comments
GREEN = "#2DA443"
ORANGE = "#DA5B0B"
BLACK = "#24292F"  # paren, colon, dot, underscore, brackets
PINK = "#E83E8C"
AQUA = "#459DB9"

class LightStyle(Style):
    """
    Style similar to the pastie default style.
    """

    styles = {
        Token:                  BLACK,
        Whitespace:             '#bbbbbb',
        Comment:                f'italic {GRAY}',
        Number:                 BLUE,
        Other:                  ORANGE,
        Keyword:                RED,
        Keyword.Constant:       BLUE,
        Keyword.Declaration:    RED,
        Keyword.Namespace:      RED,
        Keyword.Pseudo:         RED,
        Keyword.Reserved:       RED,
        Keyword.Type:           BROWN,

        Operator:               BLUE,
        Operator.Word:          BLUE,

        Name:                   BLACK,
        Name.Attribute:         RED,
        Name.Builtin:           PURPLE,
        Name.Builtin.Pseudo:    RED,
        Name.Class:             BROWN,
        Name.Constant:          BROWN,
        Name.Decorator:         PURPLE,
        Name.Entity:            BROWN,
        Name.Class:             BROWN,
        # Name.Exception:         'ne',
        Name.Function:          PURPLE,
        Name.Function.Magic:    PURPLE,
        Name.Property:          ORANGE,
        Name.Label:             ORANGE,
        Name.Namespace:         BLACK,
        Name.Other:             GREEN,
        Name.Tag:               GREEN,
        Name.Variable:          GREEN,
        Name.Variable.Class:    GREEN,
        Name.Variable.Global:   GREEN,
        Name.Variable.Instance: GREEN,
        Name.Variable.Magic:    GREEN,

        String:                 DARK_BLUE,
        String.Affix:           BLUE,
        # String.Backtick:        GREEN,
        # String.Char:            GREEN,
        # String.Delimiter:       GREEN,
        # String.Doc:             GREEN,
        # String.Double:          GREEN,
        String.Escape:          BLUE,
        # String.Heredoc:         GREEN,
        String.Interpol:        BLUE,
        # String.Other:           GREEN,
        # String.Regex:           BLUE,
        # String.Single:          GREEN,
        # String.Symbol:          GREEN,

        # Punctuation:            GREEN,
        # Punctuation.Marker:     GREEN,

        Literal:                ORANGE,

        Generic:               '#2c2cff',
        Generic.Emph:          '#008800',
        Generic.Error:         '#d30202',
        Error:                 'bg:#e3d2d2 #a61717'
    }

    # styles = {
    #     Whitespace:             '#bbbbbb',
    #     Comment:                '#888888',
    #     Comment.Preproc:        'bold #cc0000',
    #     Comment.Special:        'bg:#fff0f0 bold #cc0000',
    #
    #     String:                 'bg:#fff0f0 #dd2200',
    #     String.Regex:           'bg:#fff0ff #008800',
    #     String.Other:           'bg:#f0fff0 #22bb22',
    #     String.Symbol:          '#aa6600',
    #     String.Interpol:        '#3333bb',
    #     String.Escape:          '#0044dd',
    #
    #     Operator.Word:          '#008800',
    #
    #     Keyword:                RED,
    #     Keyword.Pseudo:         'nobold',
    #     Keyword.Type:           '#888888',
    #
    #     Name.Class:             'bold #bb0066',
    #     Name.Exception:         'bold #bb0066',
    #     Name.Function:          'bold #0066bb',
    #     Name.Property:          'bold #336699',
    #     Name.Namespace:         'bold #bb0066',
    #     Name.Builtin:           PURPLE,
    #     Name.Variable:          '#336699',
    #     Name.Variable.Class:    '#336699',
    #     Name.Variable.Instance: '#3333bb',
    #     Name.Variable.Global:   '#dd7700',
    #     Name.Constant:          'bold #003366',
    #     Name.Tag:               'bold #bb0066',
    #     Name.Attribute:         '#336699',
    #     Name.Decorator:         '#555555',
    #     Name.Label:             'italic #336699',
    #
    #     Number:                 BLUE,
    #
    #     Generic.Heading:        '#333',
    #     Generic.Subheading:     '#666',
    #     Generic.Deleted:        'bg:#ffdddd #000000',
    #     Generic.Inserted:       'bg:#ddffdd #000000',
    #     Generic.Error:          '#aa0000',
    #     Generic.Emph:           'italic',
    #     Generic.Strong:         'bold',
    #     Generic.Prompt:         '#555555',
    #     Generic.Output:         '#888888',
    #     Generic.Traceback:      '#aa0000',
    #
    #     Error:                  'bg:#e3d2d2 #a61717'
    # }




# purple - function, decorator, kwarg, module




















