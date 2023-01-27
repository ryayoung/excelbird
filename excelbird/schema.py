from __future__ import annotations

from pandas import DataFrame
from collections import namedtuple, ChainMap
from copy import copy
from excelbird.exceptions import SchemaError
from typing import overload


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

    def __getattr__(self, key: str) -> Column:
        """Lets you access dict items with dot notation"""
        if key in self.keys():
            return self[key]
        raise KeyError(f"Unknown key, '{key}'")

    @overload
    def __getitem__(self, key: list) -> Schema:
        ...

    @overload
    def __getitem__(self, key: str) -> Column:
        ...

    def __getitem__(self, key) -> Column | Schema:
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

        reordered = {copy(k): copy(self[k]) for k in key}
        return type(self)(**reordered)

    def __setitem__(self, key: str, val: Column | tuple[str, ...] | str) -> None:

        if isinstance(val, Column):
            return super().__setitem__(key, val)

        if isinstance(val, (list, tuple)):
            new = Column(*val)
            return super().__setitem__(key, new)

        if isinstance(val, str):
            new = Column(val, val)
            return super().__setitem__(key, new)

        raise ValueError(f"Invalid value, {val}")

    def drop(self, columns: list[str] | str) -> Schema:
        """
        Drop the specified keys
        """
        if not isinstance(columns, (list, tuple)):
            columns = [columns]

        return type(self)(
            **{copy(k): copy(v) for k, v in self.items() if k not in columns}
        )

    def apply(self, df: DataFrame, strict: bool = False) -> DataFrame:
        """
        - Filter ``df`` to remove columns that aren't in self
        - Re-order columns according to self's order

        If ``strict=True``, raise an error if ``df`` doesn't at least contain
        all columns specified in self.
        """
        if strict is False:
            return df[[k for k in self.keys() if k in df.columns]].copy()
        try:
            return df[[k for k in self.keys()]].copy()
        except KeyError:
            missing = [k for k in self.keys() if k not in df.columns]
            raise KeyError(
                f"Schema apply strict: The following columns were not found "
                f"in the dataframe (did you forget to run .select_inputs() first?): {missing}"
            )

    def rename(
        self,
        keys: dict | None = None,
        inputs: dict | None = None,
        outputs: dict | None = None,
    ) -> Schema:
        """
        Rename any part of self's items (key, input, output), by passing a dict
        who's keys are a current key in self, and values are the updated element.
        """
        new = self.copy()
        if keys is not None:
            new = type(self)()
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
        Like ``dict.update()``, but if a regular ``dict`` or kwargs are passed,
        they're first used to create a new ``Schema`` before updating, so the
        correct format is maintained
        """
        if isinstance(new, type(self)):
            return super().update(new)
        if new is not None:
            return super().update(type(self)(**new))
        return super().update(type(self)(**kwargs))

    def rename_inputs_to_vars(self, df: DataFrame) -> DataFrame:
        """
        Take a dataframe in its input format and rename its columns to the
        python-friendly keys in self.
        """
        return df.rename(columns={val.input: key for key, val in self.items()})

    def rename_vars_to_outputs(self, df: DataFrame) -> DataFrame:
        """
        Rename columns to self's output names
        """
        return df.rename(columns={key: val.output for key, val in self.items()})

    def inputs(self) -> list[str]:
        return [val.input for val in self.values()]

    def outputs(self) -> list[str]:
        return [val.output for val in self.values()]

    def select_inputs(self, df: DataFrame) -> DataFrame:
        """
        Renames desired columns to var names, and selects them.
        If a column isn't found, an error is raised to force you to correct
        your schema.
        """
        missing = [col for col in self.inputs() if col not in df.columns]
        if len(missing) > 0:
            raise SchemaError(
                f"Schema requires input column(s), {missing}, not found in data."
            )
        df = self.rename_inputs_to_vars(df)
        return df[[k for k in self.keys()]]

    def select_outputs(self, df: DataFrame) -> DataFrame:
        """
        Renames var columns to their output names, and selects them.
        If any columns are missing, an error is raised to remind you to create them.
        """
        missing = [col for col in self.keys() if col not in df.columns]
        if len(missing) > 0:
            raise SchemaError(f"Please add columns, {missing} before outputting.")
        df = self.rename_vars_to_outputs(df)
        return df[[k for k in self.outputs()]]

    def reset_inputs(self) -> Schema:
        """
        Sets all inputs with output values. Use this if you're
        using a previous schema to read in data that was outputted from it
        """
        new = self.copy()
        for key in new.keys():
            new[key] = Column(new[key].output, new[key].output)
        return new

    def reset_outputs(self) -> Schema:
        """
        Fills all outputs with the current inputs
        """
        new = self.copy()
        for key in new.keys():
            new[key] = Column(new[key].input, new[key].input)
        return new

    def copy(self) -> Schema:
        return type(self)(**{copy(k): copy(v) for k, v in self.items()})

    def _repr_html_(self):

        return DataFrame(
            list(zip(self.inputs(), self.outputs())),
            columns=["Input", "Output"],
            index=list(self.keys()),
        )._repr_html_()
