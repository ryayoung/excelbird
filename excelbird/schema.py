from collections import namedtuple, ChainMap
from copy import copy
from typing import TypeVar

TDataFrame = TypeVar("TDataFrame")

class SchemaError(Exception):
    pass


# namedtuple is like a tuple, but you can access elements by name. So
# `Column` is the data structure to be held as dict values by a `Schema`
Column = namedtuple("Column", "input, output")


class Schema(dict):
    """
    A subclass of dictionary, designed to hold the schema for imported data.
        Keys: python-friendly variable names
        Values: tuple: ("Input col name", "Output col name")

    Its purpose is to decouple column naming from the user's workflow.
    For each variable we want to use in our code, we'll store the following:

    "Input Col Name"   ->   var_name   ->   "Output Col Name"
                               ^
                        this never changes

    If we define this info ahead of time, our program only ever needs to reference
    the `var_name`. Input data and output format can change freely without breaking our code.

    This class has all the tools needed to convert between naming formats.
    Use `select_inputs()` and/or `read_excel()` when reading input data to `var_name`s.
    `vars_to_outputs()` returns a dict you can use to refactor columns to their output format.
    """

    def __init__(
        self, *schemas, **kwargs: tuple[str, str] | tuple[str] | list[str] | str
    ) -> None:
        """Accepts keyword args only to enforce that var names are valid python"""
        if not all(isinstance(s, Schema) for s in schemas):
            raise TypeError("Positional args can only be existing Schemas")
        # Convert all passed values to tuples
        kwargs = {
            k: v if isinstance(v, tuple) else tuple(v) if isinstance(v, list) else (v,)
            for k, v in kwargs.items()
        }
        # For values of length 1 (input column only), infer the output column by duplicating it
        kwargs = {k: v if len(v) > 1 else v + v for k, v in kwargs.items()}

        if any(len(val) > 2 for val in kwargs.values()):
            raise ValueError(
                "Values must be a max of length 2. One input col name, and one output col name"
            )
        # Convert to Column
        kwargs = {k: Column(*v) for k, v in kwargs.items()}
        # If other schemas were passed in, create those as well
        # ChainMap combines dictionaries. We reverse the input first,
        # since for some reason ChainMap returns the values in opposite order
        super().__init__(**ChainMap(*tuple(reversed(schemas))), **kwargs)

    def __getattr__(self, key) -> tuple[str, str]:
        """Lets you access dict items with dot notation"""
        if key in self.keys():
            return self[key]

    def __getitem__(self, key) -> Column | dict:
        """
        Acts normal, unless you past a list.
        If a list is passed, filter and re-order the schema just like a
        dataframe. Returns new object
        """
        if not isinstance(key, list):
            return super().__getitem__(key)

        missing = [k for k in key if k not in self.keys()]
        if len(missing) > 0:
            raise SchemaError(f"Keys {missing} not present in schema")

        filtered = {k: v for k, v in self.items() if k in key}
        reordered = {k: self[k] for k in key}
        return self.__class__(**reordered)

    def apply(self, df: TDataFrame) -> TDataFrame:
        """
        Filter dataframe to contain only columns that are in schema
        keys, re-orders the columns. Dataframe doesn't need to have all keys.
        """
        return df[[k for k in self.keys() if k in df.columns]].copy()

    def rename(self, keys: dict | None = None, inputs: dict | None = None, outputs: dict | None = None) -> None:
        """
        Identify with key
        """
        new = self.copy()
        if keys is not None:
            new = self.__class__()
            for key, val in self.items():
                if key not in keys:
                    new[key] = val
                else:
                    new[keys[key]] = val

        if inputs is not None:
            for key, new_name in inputs.items():
                new[key] = Column(new_name, new[key].output)

        if outputs is not None:
            for key, new_name in outputs.items():
                new[key] = Column(new[key].input, new_name)
        return new

    def update(self, new: dict | None = None, **kwargs) -> None:
        """
        If passing regular dict or kwargs, create a new Self object
        with the arguments before updating, so the same format is maintained
        """
        if isinstance(new, self.__class__):
            return super().update(new)
        if new is not None:
            return super().update(self.__class__(**new))
        return super().update(self.__class__(**kwargs))

    def rename_inputs_to_vars(self, df: TDataFrame) -> TDataFrame:
        return df.rename(columns={val.input: key for key, val in self.items()})

    def rename_vars_to_outputs(self, df: TDataFrame) -> TDataFrame:
        return df.rename(columns={key: val.output for key, val in self.items()})

    def inputs(self) -> list[str]:
        return [val.input for val in self.values()]

    def outputs(self) -> list[str]:
        return [val.output for val in self.values()]

    def select_inputs(self, df: TDataFrame) -> TDataFrame:
        """
        Renames desired columns to var names, and selects them.
        If a column isn't found, an error is raised to help you correct
        your schema.
        """
        missing = [col for col in self.inputs() if col not in df.columns]
        if len(missing) > 0:
            raise SchemaError(
                f"Schema requires input column(s), {missing}, not found in data."
            )
        df = self.rename_inputs_to_vars(df)
        return df[[k for k in self.keys()]]

    def select_outputs(self, df: TDataFrame) -> TDataFrame:
        """
        Renames var columns to their output names, and selects them.
        If any columns are missing, an error is raised to remind you to create them.
        """
        missing = [col for col in self.keys() if col not in df.columns]
        if len(missing) > 0:
            raise SchemaError(f"Please add columns, {missing} before outputting.")
        df = self.rename_vars_to_outputs(df)
        return df[[k for k in self.outputs()]]

    def reset_inputs(self):
        """
        Sets all inputs with output values. Use this if you're
        using a previous schema to read in data that was outputted from it
        """
        new = self.copy()
        for key in new.keys():
            new[key] = Column(new[key].output, new[key].output)
        return new

    def reset_outputs(self):
        new = self.copy()
        for key in new.keys():
            new[key] = Column(new[key].output, new[key].output)
        return new

    def copy(self) -> dict:
        return self.__class__(**{copy(k): copy(v) for k, v in self.items()})
    
    def _repr_html_(self):
        import pandas as pd
        return pd.DataFrame(
            list(zip(self.inputs(), self.outputs())),
            columns=["Input", "Output"],
            index=self.keys(),
        )._repr_html_()

