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
- HOW TO RESOLVE EXPRESSIONS WITHOUT POINTLESS ITERATION
    - Get rid of project-level global ids.
    - Ids should be regular attributes, meaningless until Book.write(). Don't attempt
      to ID anything or evaluate/resolve anything until then.
    - At Book.write():
        - DEPTH first, traverse the tree. Each container element should store
          its own dictionary mapping ids to objects for ALL children (not just immediate).
          Also, exprs/funcs with ids should be treated the same.
          If a child has an id, add it. If a child has a dictionary with ids, add all of them
          individually (they'll already be created since we drilled depth first). So at the end
          of our search, the last call should be for Book, and it should know the ids of all its elements.
        - If an element contains two or more IMMEDIATE children with matching id and/or header, throw an error
          immediately.
        - IMPORTANT: When duplicate ids are used across multiple containers in the SAME sheet,
          we must then treat them as LOCAL identifiers, whose scope ends at the first tree intersection.
          - The scope of an identifier can be logically identified by traversing upwards until a matching
            name is found. If it intersects DIRECTLY with the matching name, then the matching name will
            'override' it, and live on as a globally available identifier.
            If it intersects INDIRECTLY, then NEITHER identifier lives on past that point, since it can't
            be determined which to prioritize. Maybe we should keep track of when this happens, so we can throw
            a helpful error.
          - Direct vs. indirect intersections:
            - Direct: Container A has children X and Y. Child Y nests J
              somewhere beneath it. If X and J have matching IDs, then a direct intersection occurs inside A.
              In this case, J is accessible to ANY child of Y, but nobody else. Starting from A upwards, the id
              in question will reference X only.
            - Indirect: Container A has children X and Y. Child X nests J somewhere beneath it,
              and child Y nests K somewhere beneath it. If J and K have matching IDs, an indirect intersection
              is formed at A between J and K. The id in question will be locally valid from X downwards and
              Y downwards, respectively. However, from A upwards, the id is invalidated, i.e. forgotten entirely.
          - In practice, this is easy to implement. First, add all the ids of IMMEDIATE children.
            When looking at the childrens' pools, an id can be added if and only if: 1.) It does not match any
            of self's immediate children, and 2.) it's unique across the pool of secondary children.
            The result is that if an id is duplicated across secondary children, it will be ignored, and it will
            die from this point onwards. If an immediate child has it (we've already validated immediate child uniqueness)
            we'll include it, and it lives on.
        - Now, we can safely evaluate references.
          - This should also be done depth-first.
          - A reference may or may not be prefixed with a sheet identifier (figure out syntax for this).
          - If no sheet identifier is given, start searching for the element from the current location,
            traversing UP the tree, which will prioritize elements based on proximity. We're able to traverse
            upwards because each parent element already knows the ids of all its children. If we reach the
            Book's dictionary and nothing is found, we can throw an error.
          - If a sheet identifier is given, first make sure it's valid, then start the search from the TOP
            of the specified sheet, and search for it BREADTH first.
        - Now, once all references are resolved, we can start evaluating exprs/funcs.
          - I'm not sure which search pattern is best, but probably depth-first.
          - Evaluate recursively, so we don't have to iteratively try repeatedly. If a referenced element
            itself is not yet evaluated, evaluate it first. It will then make the same check, resulting
            in a depth-first call stack that traces straight down to the element that needs evaluation first, and then
            moves backward up the stack as dependencies get evaluated.

- Deprecate Expr and Func, in replace of just Formula
- Style objects should have `.with()` and `.without()` methods that update and return self
- A series has the option to hide its header. This way its header is kept so others can refer to it,
  but it won't be visible.
- IMPORTANT: For all containers, `children` can be a dictionary. If it is, treat each value like an arg
  (in order) and initialize it with its key as its id (or header, for _Series)
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

