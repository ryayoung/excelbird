

class HasHelp:
    @classmethod
    def help(cls, doc: bool = False):
        doc_str = cls.__doc__
        help_str = cls.__help__
        help_nb_str = cls.__help_notebook__

        if doc_str is None and help_str is None and help_nb_str is None:
            res = f"Sorry, **`{cls.__name__}`** doesn't have any documentation yet."
        elif doc is True or help_str is None:
            res = doc_str
        elif help_str is not None:
            res = help_str
        else:
            res = ""

        from excelbird._utils.util import is_notebook

        if is_notebook():
            from IPython.display import display, Markdown as md

            if help_nb_str is not None:
                display(md(help_nb_str))
            else:
                display(md(res))
        else:
            print(res)

    # Your class's help string
    __help__ = None
    # Custom help string for notebooks
    __help_notebook__ = None
