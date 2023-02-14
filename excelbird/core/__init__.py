from excelbird.core.cell import *
from excelbird.core.series import *
from excelbird.core.frame import *
from excelbird.core.stack import *
from excelbird.core.sheet import *
from excelbird.core.book import *
from excelbird.core.expression import *
from excelbird.core.function import *
from excelbird.core.gap import *
from excelbird.core.item import *
from excelbird.core.merged import *

"""
TODO:
- Allow the "not" operator to work, magically! Only for STRUCTURED containers (i.e. ONE elem_type)
  - Each container type holds a '_nots: list' class attribute.
  - Each container type overrides __bool__ to:
    - Always return True
    - Insert self to position 0 of type(self)._nots IF self is not already in the list.
  - Each container type, upon initialization, looks through its children to see if any
    child arguments are equal to False. If any are, loop through children and for each
    False, pop the object from the _nots stack of elem_type's class attribute, turn it
    into a proper "NOT()" excel function, and replace the boolean child with the updated
    Func object.
- A 'repeat' function which takes three arguments:
    1. a layout element
    2. number of times to repeat
    3. whether to reference
    4. Whether to inherit styling, if referencing.
    - Returns a ElementVector object, which the parent container must unpack
- allow a docstring in functions with triple backtick
- Func needs to have id and header
- DUDE!!!! Make Func use a unique syntax to declare an Expr inside.
  The enclosure, @[], represents an Expr. So @[<stuff>] will be interpreted
  EXACTLY as Expr("<stuff>"). AND since Expr can take a single reference without
  brackets, this gives us the ULTIMATE syntax combo. Inside a Func, reference an element
  like `@[some_elem]`. OR reference an Expr like `@[[foo]+[bar].range()]`
  the bracket references must be prefixed with an @[]
  - A reference is made like @[some_elem]. To insert an Expr, 
- Fix .ref() so that it can handle child elements who are item, expr, func
- ALL elements should be subclass of XBElement, to make type checking easier.
  ALL dynamic elements (gap, func, expr, item) should be subclass of Dynamic
- Ids and headers declared in Expr, Func, and Item should all be placed into global
  memory right away. This way, when Book's .write() is called, we can immediately determine
  if there are any invalid references, without trying to go through the whole process.
- Refactor `astype` to `to_sibling`
- Doc examples and doctests!!
- Store styles in dict instead of Style
- In range references from separate sheets, remove redundant repeated sheet name
- Change expression to @[] instead of [].
- Allow Func to be a single string, parsing out all @[] just like we do with Expr
- Conditional formatting!
- Offer syntax in cell expression to specify which $s to use
- Somehow, figure out how to use column name references.
- Fix table formatting with cross-sheet references
- Make diagrams for documentation

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

