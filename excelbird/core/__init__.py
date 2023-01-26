from excelbird.core.cell import *
from excelbird.core.vec import *
from excelbird.core.frame import *
from excelbird.core.stack import *
from excelbird.core.sheet import *
from excelbird.core.book import *

"""
TODO:
- In range references from separate sheets, remove redundant repeated sheet name
- Change expression to @[] instead of [].
- Allow Func to be a single string, parsing out all @[] just like we do with Expr
- Conditional formatting!
- Offer syntax in cell expression to specify which $s to use
- Somehow, figure out how to use column name references.

Make cell references smarter, using $ signs where appropriate.
    First change cell expression tree to hold 5 elements instead of 3.
    Second and last element hold a tuple designating how to lock the cell reference.
    (False,False) -> A5, (True,False) -> $A5, (False,True) -> A$5, (True,True) -> $A$5
    Then, in the math module, determine what these locks should be.
        - Create an express_with_lock function, because we can't express
          locks in a "a + b" expression (3 elements only), so instead, intermediate
          math will be done through a function that can take locks. 
        - LOGIC:
            - The lock is only set once. So if elem_math recieves a lock for an element,
              keep it. 
            - If referencing a Cell -> (True, True)
            - Col -> (True, False)
            - Row -> (False, True)
    For Func, we need a way to choose to specify lock. I think we can do this by allowing
    a 'lock' param inside .range(). Make sure Cell has a .range() as well now. This will
    be a boolean to full-lock or not. It should default to True, for all versions of .range()
"""

class Merged:
    """
    Take a Cell, and distance across/down to merge.
    Parent container will figure out how to interpret this.

    If inside a Col or Row, there is no need to differentiate between across/down.
    Just pass a single integer to `amount` as a positional.

    If inside a Col, for instance, and amount is 2, the parent will explode this value into
    three Cells: *[Cell(..., merge=(2,0)), Cell(), Cell()] where the first element is the initial
    Cell that was passed, but with the merge attribute set to merge 2 below, plus two empty cells
    to soak up the merge.

    If inside a Frame, and across is 2, down is 3, the parent will explode this value into 3 Cols:
        *[
            Col(Cell(..., merge=(3,2)), Cell(), Cell(), Cell()),
            Col(Cell(), Cell(), Cell(), Cell()),
            Col(Cell(), Cell(), Cell(), Cell())
        ]

    If inside a Stack, there is no need to explode. Insert a Frame instead:
        Frame(
            Col(Cell(..., merge=(3,2)), Cell(), Cell(), Cell()),
            Col(Cell(), Cell(), Cell(), Cell()),
            Col(Cell(), Cell(), Cell(), Cell())
        )

    """
def __init__(self, cell: Cell, amount: int = None, across: int = None, down: int = None):
    ...
