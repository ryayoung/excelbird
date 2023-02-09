

class UnsavedWorkbookError(Exception):
    pass

class SchemaError(Exception):
    pass

class AlreadyWrittenError(Exception):
    """
    An object can only be written once!
    """
    pass

class AutoOpenFileError(Exception):
    """
    For issues encountered when using `auto_open=True` in a Book.
    Common issues include:
        Not having Xlwings installed
        Trouble accessing file, usually caused by it being in OneDrive
    """
    pass

class InvalidSheetName(Exception):
    pass

class ExpressionResolutionError(Exception):
    default_msg = """
One or more expressions could not be resolved.
As a reminder, expression strings should reference elements inside
square brackets with no quotes, like: {"[some_col] + [other_col]"} or {"[1] + 99"}.

The value inside the brackets must contain one of the following:
    - A valid index of an element in the parent container
    - The `id` of any element defined globally
    - The `header` of any Col or Row defined globally

Another possible cause of this error is when setting `isolate=True` to a Sheet.
When True, the sheet will resolve its own references immediately after creation
and then clear the global memory of references, meaning any element created before,
or inside, an isolated sheet cannot be referenced in an Expr by id or header
after that sheet was created.
"""
    def __init__(self, message: str | None = None):
        if message is None:
            message = type(self).default_msg
        self.message = message
        super().__init__(self.message)


class ExpressionExecutionError(Exception):
    def __init__(self, original_exception: Exception, expr_string: str):
        super().__init__(
            f"An error was encountered when executing an Expr. This is usually a user syntax error. "
            "Excelbird tried to execute the following string as python code: '" + expr_string + "' "
            f"and encountered a '{type(original_exception).__name__}' with the description, '" + str(original_exception) + "'"
        )

class ExpressionTypeError(Exception):
    pass


class CellReferenceError(Exception):
    default_msg = """
One of the cells in your book is trying to reference a cell that isn't being
placed in the book. This would be fine if the missing cell contained references
to cells that eventually trace back to valid cells in the book, or if it had a value
of its own. In that case, the expression or value stored in the missing cell would be
inherited by those who were referencing it. The value of the missing cell is None.
Why was it referenced?
"""
    def __init__(self, message: str | None = None):
        if message is None:
            message = type(self).default_msg
        self.message = message
        super().__init__(self.message)
    
    @classmethod
    def issue_warning(cls, message: str | None = None):
        if message is None:
            message = cls.default_msg
        print(message)
