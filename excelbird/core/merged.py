from excelbird.core.cell import Cell

class _Merged:
    """
    Take a Cell, and distance across/down to merge.
    Parent container will figure out how to interpret this.

    If inside a Col or Row, there is no need to differentiate between across/down.
    Just pass a single integer to `amount` as a positional.

    If inside a Col, for instance, and amount is 2, the parent will explode this value into
    three Cells: `*`[Cell(..., merge=(2,0)), Cell(), Cell()] where the first element is the initial
    Cell that was passed, but with the merge attribute set to merge 2 below, plus two empty cells
    to soak up the merge.

    If inside a Frame, and across is 2, down is 3, the parent will explode this value into 3 Cols:
        `*`[
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
def __init__(self, cell: Cell, across: int = None, down: int = None):
    pass
