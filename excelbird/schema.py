"""
xb.Schema
==========

Where traditional dataframe schema classes define what should go *inside*
a dataframe's columns, `Schema` defines what those columns should be, 'when'
they should be, and how they got there. It defines a dataframe's 'state' at
a given point in time. And it provides the tools/methods needed to help you get to
that state, change it, and move to new states seamlessly.

It's a simple class, designed for ease of use and exceptional readability.

It's a subclass of dictionary.

* Keys: python-friendly variable names
* Values: namedtuple: ("Input col name", "Output col name (optional)")

Consider the following:

.. code-block::

    sch_person = Schema(
        first_name=("FName", "First Name"),
        last_name=("LName", "Last Name"),
        favorite_food=("Fav Food", "Favorite Food"),
    )

    sch_company = Schema(
        comp_name=("Companyname", "Company Name"),
        market_cap="Market Capitalization",
        favorite_food="Preferred Employee Favorite Food",
    )

    sch_output = Schema(
        sch_person[[
            'last_name',
            'age',
        ]],
        sch_company[[
            'comp_name',
        ]],
        is_executive="Person is Executive"
    )


This should be readability-paradise. Given only the code above,
the reader should know exactly what's supposed to happen in the script:

* There are two input sources, person and company.
* The script will have to join person and company, and include fields from each.
* The script needs to add a new custom column, `is_executive`


Instance methods of this class try to provide as much utility as possible for
common operations. Here are just a few:

* ``select_inputs()``: Take raw input data, validate our required columns can be
  found, select them, rename them python-friendly, and order them
* ``select_outputs()``: Do the opposite, and again, validate that all the columns
  required by our output schema are present.
* ``apply()``: Mid-workflow, safely re-order our columns and remove undesired ones.
"""

from __future__ import annotations

from pandas import DataFrame
from collections import namedtuple, ChainMap
from copy import copy
from excelbird.exceptions import SchemaError
from typing import overload


# The values held by each key of a Schema.
# Tuple's immutability helps enforce consistency in user's code
Column = namedtuple("Column", "input, output")
Column.__doc__ = """
The values stored by a :class:`xb.Schema <excelbird.schema.Schema>`

A :class:`namedtuple` with two values, `input` and `output`, that
can be accessed by dot notation, and is immutable.
"""


class Schema(dict):
    """
    Defines the state of a dataframe.

    Parameters
    ----------
    *schemas : Schema
        Existing schemas to use, to build a composite Schema that shows the reader
        where the columns are coming from.
    **kwargs : tuple[str, str] | tuple[str] | str
        A mapping of python-friendly variable names to their corresponding input column
        names and output column names. If value is a string, or 1-element tuple, it will
        be applied as both the input and output name.

    Examples
    --------

    Define a new schema

    .. code-block::

        sch_person = Schema(
            first_name=("FName", "First Name"),
            last_name=("LName", "Last Name"),
            age="Age",
        )

    Define a composite schema that uses columns from a previous one

    .. code-block::

        sch_employee = Schema(
            sch_person[[
                'last_name',
                'age',
            ]],
            rank="Rank"
        )

    """
    def __init__(
        self, *schemas, **kwargs: tuple[str, str] | tuple[str] | list[str] | str
    ) -> None:
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

    # def __getattr__(self, key: str) -> Column:
    #     """Lets you access dict items with dot notation"""
    #     if key in self.keys():
    #         return self[key]
    #     raise KeyError(f"Unknown key, '{key}'")

    @overload
    def __getitem__(self, key: list) -> Schema:
        ...

    @overload
    def __getitem__(self, key: str) -> Column:
        ...

    def __getitem__(self, key) -> Column | Schema:
        """
        Called when accessing items with ``sch[<key>]`` syntax.

        Acts exactly like :class:`dict`'s ``__getitem__``, unless a
        :class:`list` is passed. Pass a list of keys to return a *new*
        object with the selected elements, in the desired order, similar
        to how a :class:`pd.DataFrame <pandas.DataFrame>` works.

        Parameters
        ----------
        key : str or int or list[str] or slice
            Used to access items

        Returns
        -------
        :class:`xb.Column <excelbird.schema.Column>`
            If a non-list key is used

        :class:`xb.Schema <excelbird.schema.Schema>`
            If a list key is used
            
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
        Returns a copy of Self with the specified keys dropped

        Parameters
        ----------
        columns : list[str] or str
            The items to drop

        Returns
        -------
        :class:`Self`
        """
        if not isinstance(columns, (list, tuple)):
            columns = [columns]

        return type(self)(
            **{copy(k): copy(v) for k, v in self.items() if k not in columns}
        )

    def apply(self, df: DataFrame, strict: bool = False) -> DataFrame:
        """
        Removes columns from a dataframe that aren't in the schema,
        and re-orders columns according to schema's order. If ``strict=True``,
        An error will be raised if ``df`` doesn't contain at least all the
        desired columns

        Parameters
        ----------
        df : pd.DataFrame
            Dataframe to apply the changes
        strict : bool, default False
            Whether to enforce that ``df`` must contain all columns needed by the schema

        Returns
        -------
        :class:`pd.DataFrame <pandas.DataFrame>`
            The updated dataframe

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
        keys: dict[str, str] | None = None,
        inputs: dict[str, str] | None = None,
        outputs: dict[str, str] | None = None,
    ) -> Schema:
        """
        Rename any part of the schema's data (keys, inputs, outputs) using a dictionary.
        Pick *one* of ``keys``, ``inputs``, ``outputs``.

        Regardless of which option is chosen, the **keys** in the provided dictionary
        must represent **current** keys in the schema.

        Parameters
        ----------
        keys : dict[str, str], optional
            Mapping to rename the keys in the current schema
        inputs : dict[str, str], optional
            Mapping to rename the inputs in the current schema
        outputs : dict[str, str], optional
            Mapping to rename the outputs in the current schema

        Returns
        -------
        :class:`Self`
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

    def update(self, other: Schema | dict | None = None, **kwargs) -> None:
        """
        Just like the normal :meth:`dict.update`, but if a regular :class:`dict`,
        or keyword arguments are passed, the arguments are first converted to
        a :class:`Schema <excelbird.schema.Schema>` before updating.

        Parameters
        ----------
        other : Schema or dict, optional
            Mapping to update the current schema with
        **kwargs : str
            Used to create a Schema first, then update the current one with it.
            
        Returns
        -------
        :class:`Self`
        """
        if isinstance(other, type(self)):
            return super().update(other)
        if other is not None:
            return super().update(type(self)(**other))
        return super().update(type(self)(**kwargs))

    def rename_inputs_to_vars(self, df: DataFrame) -> DataFrame:
        """
        Calls :meth:`df.rename <pandas.DataFrame.rename>` on the given
        dataframe and provides a mapping from the inputs in the current
        schema to the keys in the current schema

        Parameters
        ----------
        df : pd.DataFrame
            Dataframe to update

        Returns
        -------
        pd.DataFrame
            The updated dataframe
        """
        return df.rename(columns={val.input: key for key, val in self.items()})

    def rename_vars_to_outputs(self, df: DataFrame) -> DataFrame:
        """
        Calls :meth:`df.rename <pandas.DataFrame.rename>` on the given
        dataframe and provides a mapping from the keys in the current
        schema to the outputs in the current schema

        Parameters
        ----------
        df : pd.DataFrame
            Dataframe to update

        Returns
        -------
        pd.DataFrame
            The updated dataframe
        """
        return df.rename(columns={key: val.output for key, val in self.items()})

    def inputs(self) -> list[str]:
        """
        The input values for each key in the schema

        Returns
        -------
        list[str]
        """
        return [val.input for val in self.values()]

    def outputs(self) -> list[str]:
        """
        The output values for each key in the schema

        Returns
        -------
        list[str]
        """
        return [val.output for val in self.values()]

    def select_inputs(self, df: DataFrame) -> DataFrame:
        """
        Renames desired columns to var names, and selects them in the
        order of the schema.
        If a column isn't found, an error is raised to force you to correct
        your schema.

        Parameters
        ----------
        df : pd.DataFrame
            Target dataframe

        Returns
        -------
        pd.DataFrame
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
        Renames the current columns to output names, and selects them in
        the order of the schema.
        If a column isn't found, an error is raised to force you to correct
        your schema.

        Parameters
        ----------
        df : pd.DataFrame
            Target dataframe

        Returns
        -------
        pd.DataFrame
        """
        missing = [col for col in self.keys() if col not in df.columns]
        if len(missing) > 0:
            raise SchemaError(f"Please add columns, {missing} before outputting.")
        df = self.rename_vars_to_outputs(df)
        return df[[k for k in self.outputs()]]

    def reset_inputs(self) -> Schema:
        """
        Replaces all input values with the current output values.
        Use this if you're using a previous schema to read in data that was outputted from it

        Returns
        -------
        :class:`Self`
        """
        new = self.copy()
        for key in new.keys():
            new[key] = Column(new[key].output, new[key].output)
        return new

    def reset_outputs(self) -> Schema:
        """
        Replaces all output values with current input values.

        Returns
        -------
        :class:`Self`
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
