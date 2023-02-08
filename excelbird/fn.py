"""

.. role:: html(raw)
   :format: html

All ~500 Excel functions can be accessed in Python, from the :mod:`excelbird.fn` module.

Each is documented with the same short summary as provided by `Microsoft's documentation <https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188>`_.

Allows for autocomplete and documentation preview in your IDE.

**Syntax Example:** Excel's ``T.DIST.2T()`` is :meth:`T_DIST_2T` in `excelbird`.

.. note::

    Each function is short for an :class:`excelbird.Func`

    .. code-block::

        fn.ABS(some_cell)

    is the same as

    .. code-block::

        Func("ABS(", some_cell, ")")
"""
from excelbird.core.function import Func
from typing import Any


def ABS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the absolute value of a number

	In Excel: ``ABS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ABS(", *inner, ")", res_type=res_type, **kwargs)

def ACCRINT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the accrued interest for a security that pays periodic interest

	In Excel: ``ACCRINT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACCRINT(", *inner, ")", res_type=res_type, **kwargs)

def ACCRINTM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the accrued interest for a security that pays interest at maturity

	In Excel: ``ACCRINTM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACCRINTM(", *inner, ")", res_type=res_type, **kwargs)

def ACOS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the arccosine of a number

	In Excel: ``ACOS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACOS(", *inner, ")", res_type=res_type, **kwargs)

def ACOSH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the inverse hyperbolic cosine of a number

	In Excel: ``ACOSH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACOSH(", *inner, ")", res_type=res_type, **kwargs)

def ACOT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the arccotangent of a number

	In Excel: ``ACOT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACOT(", *inner, ")", res_type=res_type, **kwargs)

def ACOTH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic arccotangent of a number

	In Excel: ``ACOTH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACOTH(", *inner, ")", res_type=res_type, **kwargs)

def AGGREGATE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns an aggregate in a list or database

	In Excel: ``AGGREGATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AGGREGATE(", *inner, ")", res_type=res_type, **kwargs)

def ADDRESS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns a reference as text to a single cell in a worksheet

	In Excel: ``ADDRESS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ADDRESS(", *inner, ")", res_type=res_type, **kwargs)

def AMORDEGRC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the depreciation for each accounting period by using a depreciation coefficient

	In Excel: ``AMORDEGRC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AMORDEGRC(", *inner, ")", res_type=res_type, **kwargs)

def AMORLINC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the depreciation for each accounting period

	In Excel: ``AMORLINC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AMORLINC(", *inner, ")", res_type=res_type, **kwargs)

def AND(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns TRUE if all of its arguments are TRUE

	In Excel: ``AND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AND(", *inner, ")", res_type=res_type, **kwargs)

def ARABIC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts a Roman number to Arabic, as a number

	In Excel: ``ARABIC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ARABIC(", *inner, ")", res_type=res_type, **kwargs)

def AREAS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the number of areas in a reference

	In Excel: ``AREAS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AREAS(", *inner, ")", res_type=res_type, **kwargs)

def ARRAYTOTEXT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns an array of text values from any specified range

	In Excel: ``ARRAYTOTEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ARRAYTOTEXT(", *inner, ")", res_type=res_type, **kwargs)

def ASC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Changes full-width (double-byte) English letters or katakana within a character string to half-width (single-byte) characters

	In Excel: ``ASC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ASC(", *inner, ")", res_type=res_type, **kwargs)

def ASIN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the arcsine of a number

	In Excel: ``ASIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ASIN(", *inner, ")", res_type=res_type, **kwargs)

def ASINH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the inverse hyperbolic sine of a number

	In Excel: ``ASINH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ASINH(", *inner, ")", res_type=res_type, **kwargs)

def ATAN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the arctangent of a number

	In Excel: ``ATAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ATAN(", *inner, ")", res_type=res_type, **kwargs)

def ATAN2(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the arctangent from x- and y-coordinates

	In Excel: ``ATAN2()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ATAN2(", *inner, ")", res_type=res_type, **kwargs)

def ATANH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the inverse hyperbolic tangent of a number

	In Excel: ``ATANH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ATANH(", *inner, ")", res_type=res_type, **kwargs)

def AVEDEV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the average of the absolute deviations of data points from their mean

	In Excel: ``AVEDEV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AVEDEV(", *inner, ")", res_type=res_type, **kwargs)

def AVERAGE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the average of its arguments

	In Excel: ``AVERAGE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AVERAGE(", *inner, ")", res_type=res_type, **kwargs)

def AVERAGEA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the average of its arguments, including numbers, text, and logical values

	In Excel: ``AVERAGEA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AVERAGEA(", *inner, ")", res_type=res_type, **kwargs)

def AVERAGEIF(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the average (arithmetic mean) of all the cells in a range that meet a given criteria

	In Excel: ``AVERAGEIF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AVERAGEIF(", *inner, ")", res_type=res_type, **kwargs)

def AVERAGEIFS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the average (arithmetic mean) of all cells that meet multiple criteria.

	In Excel: ``AVERAGEIFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AVERAGEIFS(", *inner, ")", res_type=res_type, **kwargs)

def BAHTTEXT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Converts a number to text, using the ß (baht) currency format

	In Excel: ``BAHTTEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BAHTTEXT(", *inner, ")", res_type=res_type, **kwargs)

def BASE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts a number into a text representation with the given radix (base)

	In Excel: ``BASE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BASE(", *inner, ")", res_type=res_type, **kwargs)

def BESSELI(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the modified Bessel function In(x)

	In Excel: ``BESSELI()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BESSELI(", *inner, ")", res_type=res_type, **kwargs)

def BESSELJ(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the Bessel function Jn(x)

	In Excel: ``BESSELJ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BESSELJ(", *inner, ")", res_type=res_type, **kwargs)

def BESSELK(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the modified Bessel function Kn(x)

	In Excel: ``BESSELK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BESSELK(", *inner, ")", res_type=res_type, **kwargs)

def BESSELY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the Bessel function Yn(x)

	In Excel: ``BESSELY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BESSELY(", *inner, ")", res_type=res_type, **kwargs)

def BETADIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the beta cumulative distribution function

	In Excel: ``BETADIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BETADIST(", *inner, ")", res_type=res_type, **kwargs)

def BETA_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the beta cumulative distribution function

	In Excel: ``BETA.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BETA.DIST(", *inner, ")", res_type=res_type, **kwargs)

def BETAINV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the cumulative distribution function for a specified beta distribution

	In Excel: ``BETAINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BETAINV(", *inner, ")", res_type=res_type, **kwargs)

def BETA_INV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the cumulative distribution function for a specified beta distribution

	In Excel: ``BETA.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BETA.INV(", *inner, ")", res_type=res_type, **kwargs)

def BIN2DEC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a binary number to decimal

	In Excel: ``BIN2DEC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BIN2DEC(", *inner, ")", res_type=res_type, **kwargs)

def BIN2HEX(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a binary number to hexadecimal

	In Excel: ``BIN2HEX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BIN2HEX(", *inner, ")", res_type=res_type, **kwargs)

def BIN2OCT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a binary number to octal

	In Excel: ``BIN2OCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BIN2OCT(", *inner, ")", res_type=res_type, **kwargs)

def BINOMDIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the individual term binomial distribution probability

	In Excel: ``BINOMDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BINOMDIST(", *inner, ")", res_type=res_type, **kwargs)

def BINOM_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the individual term binomial distribution probability

	In Excel: ``BINOM.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BINOM.DIST(", *inner, ")", res_type=res_type, **kwargs)

def BINOM_DIST_RANGE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the probability of a trial result using a binomial distribution

	In Excel: ``BINOM.DIST.RANGE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BINOM.DIST.RANGE(", *inner, ")", res_type=res_type, **kwargs)

def BINOM_INV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the smallest value for which the cumulative binomial distribution is less than or equal to a criterion value

	In Excel: ``BINOM.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BINOM.INV(", *inner, ")", res_type=res_type, **kwargs)

def BITAND(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a 'Bitwise And' of two numbers

	In Excel: ``BITAND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BITAND(", *inner, ")", res_type=res_type, **kwargs)

def BITLSHIFT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a value number shifted left by shift_amount bits

	In Excel: ``BITLSHIFT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BITLSHIFT(", *inner, ")", res_type=res_type, **kwargs)

def BITOR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a bitwise OR of 2 numbers

	In Excel: ``BITOR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BITOR(", *inner, ")", res_type=res_type, **kwargs)

def BITRSHIFT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a value number shifted right by shift_amount bits

	In Excel: ``BITRSHIFT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BITRSHIFT(", *inner, ")", res_type=res_type, **kwargs)

def BITXOR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a bitwise 'Exclusive Or' of two numbers

	In Excel: ``BITXOR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BITXOR(", *inner, ")", res_type=res_type, **kwargs)

def BYCOL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Applies a LAMBDA to each column and returns an array of the results

	In Excel: ``BYCOL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BYCOL(", *inner, ")", res_type=res_type, **kwargs)

def BYROW(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Applies a LAMBDA to each row and returns an array of the results

	In Excel: ``BYROW()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BYROW(", *inner, ")", res_type=res_type, **kwargs)

def CALL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Add-in and Automation:** Calls a procedure in a dynamic link library or code resource

	In Excel: ``CALL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CALL(", *inner, ")", res_type=res_type, **kwargs)

def CEILING(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Rounds a number to the nearest integer or to the nearest multiple of significance

	In Excel: ``CEILING()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CEILING(", *inner, ")", res_type=res_type, **kwargs)

def CEILING_MATH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number up, to the nearest integer or to the nearest multiple of significance

	In Excel: ``CEILING.MATH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CEILING.MATH(", *inner, ")", res_type=res_type, **kwargs)

def CEILING_PRECISE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number the nearest integer or to the nearest multiple of significance. Regardless of the sign of the number, the number is rounded up.

	In Excel: ``CEILING.PRECISE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CEILING.PRECISE(", *inner, ")", res_type=res_type, **kwargs)

def CELL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns information about the formatting, location, or contents of a cell

	In Excel: ``CELL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CELL(", *inner, ")", res_type=res_type, **kwargs)

def CHAR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the character specified by the code number

	In Excel: ``CHAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHAR(", *inner, ")", res_type=res_type, **kwargs)

def CHIDIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the one-tailed probability of the chi-squared distribution

	In Excel: ``CHIDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHIDIST(", *inner, ")", res_type=res_type, **kwargs)

def CHIINV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the one-tailed probability of the chi-squared distribution

	In Excel: ``CHIINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHIINV(", *inner, ")", res_type=res_type, **kwargs)

def CHITEST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the test for independence

	In Excel: ``CHITEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHITEST(", *inner, ")", res_type=res_type, **kwargs)

def CHISQ_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the cumulative beta probability density function

	In Excel: ``CHISQ.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHISQ.DIST(", *inner, ")", res_type=res_type, **kwargs)

def CHISQ_DIST_RT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the one-tailed probability of the chi-squared distribution

	In Excel: ``CHISQ.DIST.RT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHISQ.DIST.RT(", *inner, ")", res_type=res_type, **kwargs)

def CHISQ_INV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the cumulative beta probability density function

	In Excel: ``CHISQ.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHISQ.INV(", *inner, ")", res_type=res_type, **kwargs)

def CHISQ_INV_RT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the one-tailed probability of the chi-squared distribution

	In Excel: ``CHISQ.INV.RT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHISQ.INV.RT(", *inner, ")", res_type=res_type, **kwargs)

def CHISQ_TEST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the test for independence

	In Excel: ``CHISQ.TEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHISQ.TEST(", *inner, ")", res_type=res_type, **kwargs)

def CHOOSE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Chooses a value from a list of values

	In Excel: ``CHOOSE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHOOSE(", *inner, ")", res_type=res_type, **kwargs)

def CHOOSECOLS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the specified columns from an array

	In Excel: ``CHOOSECOLS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHOOSECOLS(", *inner, ")", res_type=res_type, **kwargs)

def CHOOSEROWS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the specified rows from an array

	In Excel: ``CHOOSEROWS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHOOSEROWS(", *inner, ")", res_type=res_type, **kwargs)

def CLEAN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Removes all nonprintable characters from text

	In Excel: ``CLEAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CLEAN(", *inner, ")", res_type=res_type, **kwargs)

def CODE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns a numeric code for the first character in a text string

	In Excel: ``CODE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CODE(", *inner, ")", res_type=res_type, **kwargs)

def COLUMN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the column number of a reference

	In Excel: ``COLUMN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COLUMN(", *inner, ")", res_type=res_type, **kwargs)

def COLUMNS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the number of columns in a reference

	In Excel: ``COLUMNS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COLUMNS(", *inner, ")", res_type=res_type, **kwargs)

def COMBIN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the number of combinations for a given number of objects

	In Excel: ``COMBIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COMBIN(", *inner, ")", res_type=res_type, **kwargs)

def COMBINA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts real and imaginary coefficients into a complex number

	In Excel: ``COMBINA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COMBINA(", *inner, ")", res_type=res_type, **kwargs)

def CONCAT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Combines the text from multiple ranges and/or strings, but it doesn't provide the delimiter or IgnoreEmpty arguments.

	In Excel: ``CONCAT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONCAT(", *inner, ")", res_type=res_type, **kwargs)

def CONCATENATE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Joins several text items into one text item

	In Excel: ``CONCATENATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONCATENATE(", *inner, ")", res_type=res_type, **kwargs)

def CONFIDENCE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the confidence interval for a population mean

	In Excel: ``CONFIDENCE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONFIDENCE(", *inner, ")", res_type=res_type, **kwargs)

def CONFIDENCE_NORM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the confidence interval for a population mean

	In Excel: ``CONFIDENCE.NORM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONFIDENCE.NORM(", *inner, ")", res_type=res_type, **kwargs)

def CONFIDENCE_T(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the confidence interval for a population mean, using a Student's t distribution

	In Excel: ``CONFIDENCE.T()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONFIDENCE.T(", *inner, ")", res_type=res_type, **kwargs)

def CONVERT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a number from one measurement system to another

	In Excel: ``CONVERT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONVERT(", *inner, ")", res_type=res_type, **kwargs)

def CORREL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the correlation coefficient between two data sets

	In Excel: ``CORREL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CORREL(", *inner, ")", res_type=res_type, **kwargs)

def COS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the cosine of a number

	In Excel: ``COS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COS(", *inner, ")", res_type=res_type, **kwargs)

def COSH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic cosine of a number

	In Excel: ``COSH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COSH(", *inner, ")", res_type=res_type, **kwargs)

def COT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic cosine of a number

	In Excel: ``COT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COT(", *inner, ")", res_type=res_type, **kwargs)

def COTH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the cotangent of an angle

	In Excel: ``COTH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COTH(", *inner, ")", res_type=res_type, **kwargs)

def COUNT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Counts how many numbers are in the list of arguments

	In Excel: ``COUNT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUNT(", *inner, ")", res_type=res_type, **kwargs)

def COUNTA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Counts how many values are in the list of arguments

	In Excel: ``COUNTA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUNTA(", *inner, ")", res_type=res_type, **kwargs)

def COUNTBLANK(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Counts the number of blank cells within a range

	In Excel: ``COUNTBLANK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUNTBLANK(", *inner, ")", res_type=res_type, **kwargs)

def COUNTIF(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Counts the number of cells within a range that meet the given criteria

	In Excel: ``COUNTIF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUNTIF(", *inner, ")", res_type=res_type, **kwargs)

def COUNTIFS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Counts the number of cells within a range that meet multiple criteria

	In Excel: ``COUNTIFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUNTIFS(", *inner, ")", res_type=res_type, **kwargs)

def COUPDAYBS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of days from the beginning of the coupon period to the settlement date

	In Excel: ``COUPDAYBS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPDAYBS(", *inner, ")", res_type=res_type, **kwargs)

def COUPDAYS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of days in the coupon period that contains the settlement date

	In Excel: ``COUPDAYS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPDAYS(", *inner, ")", res_type=res_type, **kwargs)

def COUPDAYSNC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of days from the settlement date to the next coupon date

	In Excel: ``COUPDAYSNC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPDAYSNC(", *inner, ")", res_type=res_type, **kwargs)

def COUPNCD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the next coupon date after the settlement date

	In Excel: ``COUPNCD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPNCD(", *inner, ")", res_type=res_type, **kwargs)

def COUPNUM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of coupons payable between the settlement date and maturity date

	In Excel: ``COUPNUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPNUM(", *inner, ")", res_type=res_type, **kwargs)

def COUPPCD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the previous coupon date before the settlement date

	In Excel: ``COUPPCD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPPCD(", *inner, ")", res_type=res_type, **kwargs)

def COVAR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns covariance, the average of the products of paired deviations

	In Excel: ``COVAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COVAR(", *inner, ")", res_type=res_type, **kwargs)

def COVARIANCE_P(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns covariance, the average of the products of paired deviations

	In Excel: ``COVARIANCE.P()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COVARIANCE.P(", *inner, ")", res_type=res_type, **kwargs)

def COVARIANCE_S(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the sample covariance, the average of the products deviations for each data point pair in two data sets

	In Excel: ``COVARIANCE.S()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COVARIANCE.S(", *inner, ")", res_type=res_type, **kwargs)

def CRITBINOM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the smallest value for which the cumulative binomial distribution is less than or equal to a criterion value

	In Excel: ``CRITBINOM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CRITBINOM(", *inner, ")", res_type=res_type, **kwargs)

def CSC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the cosecant of an angle

	In Excel: ``CSC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CSC(", *inner, ")", res_type=res_type, **kwargs)

def CSCH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic cosecant of an angle

	In Excel: ``CSCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CSCH(", *inner, ")", res_type=res_type, **kwargs)

def CUBEKPIMEMBER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns a key performance indicator (KPI) name, property, and measure, and displays the name and property in the cell. A KPI is a quantifiable measurement, such as monthly gross profit or quarterly employee turnover, used to monitor an organization's performance.

	In Excel: ``CUBEKPIMEMBER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBEKPIMEMBER(", *inner, ")", res_type=res_type, **kwargs)

def CUBEMEMBER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns a member or tuple in a cube hierarchy. Use to validate that the member or tuple exists in the cube.

	In Excel: ``CUBEMEMBER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBEMEMBER(", *inner, ")", res_type=res_type, **kwargs)

def CUBEMEMBERPROPERTY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns the value of a member property in the cube. Use to validate that a member name exists within the cube and to return the specified property for this member.

	In Excel: ``CUBEMEMBERPROPERTY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBEMEMBERPROPERTY(", *inner, ")", res_type=res_type, **kwargs)

def CUBERANKEDMEMBER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns the nth, or ranked, member in a set. Use to return one or more elements in a set, such as the top sales performer or top 10 students.

	In Excel: ``CUBERANKEDMEMBER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBERANKEDMEMBER(", *inner, ")", res_type=res_type, **kwargs)

def CUBESET(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Cube:** Defines a calculated set of members or tuples by sending a set expression to the cube on the server, which creates the set, and then returns that set to Microsoft Office Excel.

	In Excel: ``CUBESET()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBESET(", *inner, ")", res_type=res_type, **kwargs)

def CUBESETCOUNT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns the number of items in a set.

	In Excel: ``CUBESETCOUNT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBESETCOUNT(", *inner, ")", res_type=res_type, **kwargs)

def CUBEVALUE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns an aggregated value from a cube.

	In Excel: ``CUBEVALUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBEVALUE(", *inner, ")", res_type=res_type, **kwargs)

def CUMIPMT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the cumulative interest paid between two periods

	In Excel: ``CUMIPMT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUMIPMT(", *inner, ")", res_type=res_type, **kwargs)

def CUMPRINC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the cumulative principal paid on a loan between two periods

	In Excel: ``CUMPRINC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUMPRINC(", *inner, ")", res_type=res_type, **kwargs)

def DATE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of a particular date

	In Excel: ``DATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DATE(", *inner, ")", res_type=res_type, **kwargs)

def DATEDIF(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Calculates the number of days, months, or years between two dates. This function is useful in formulas where you need to calculate an age.

	In Excel: ``DATEDIF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DATEDIF(", *inner, ")", res_type=res_type, **kwargs)

def DATEVALUE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a date in the form of text to a serial number

	In Excel: ``DATEVALUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DATEVALUE(", *inner, ")", res_type=res_type, **kwargs)

def DAVERAGE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Returns the average of selected database entries

	In Excel: ``DAVERAGE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DAVERAGE(", *inner, ")", res_type=res_type, **kwargs)

def DAY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a day of the month

	In Excel: ``DAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DAY(", *inner, ")", res_type=res_type, **kwargs)

def DAYS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the number of days between two dates

	In Excel: ``DAYS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DAYS(", *inner, ")", res_type=res_type, **kwargs)

def DAYS360(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Calculates the number of days between two dates based on a 360-day year

	In Excel: ``DAYS360()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DAYS360(", *inner, ")", res_type=res_type, **kwargs)

def DB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the depreciation of an asset for a specified period by using the fixed-declining balance method

	In Excel: ``DB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DB(", *inner, ")", res_type=res_type, **kwargs)

def DBCS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Changes half-width (single-byte) English letters or katakana within a character string to full-width (double-byte) characters

	In Excel: ``DBCS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DBCS(", *inner, ")", res_type=res_type, **kwargs)

def DCOUNT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Counts the cells that contain numbers in a database

	In Excel: ``DCOUNT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DCOUNT(", *inner, ")", res_type=res_type, **kwargs)

def DCOUNTA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Counts nonblank cells in a database

	In Excel: ``DCOUNTA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DCOUNTA(", *inner, ")", res_type=res_type, **kwargs)

def DDB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the depreciation of an asset for a specified period by using the double-declining balance method or some other method that you specify

	In Excel: ``DDB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DDB(", *inner, ")", res_type=res_type, **kwargs)

def DEC2BIN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a decimal number to binary

	In Excel: ``DEC2BIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DEC2BIN(", *inner, ")", res_type=res_type, **kwargs)

def DEC2HEX(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a decimal number to hexadecimal

	In Excel: ``DEC2HEX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DEC2HEX(", *inner, ")", res_type=res_type, **kwargs)

def DEC2OCT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a decimal number to octal

	In Excel: ``DEC2OCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DEC2OCT(", *inner, ")", res_type=res_type, **kwargs)

def DECIMAL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts a text representation of a number in a given base into a decimal number

	In Excel: ``DECIMAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DECIMAL(", *inner, ")", res_type=res_type, **kwargs)

def DEGREES(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts radians to degrees

	In Excel: ``DEGREES()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DEGREES(", *inner, ")", res_type=res_type, **kwargs)

def DELTA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Tests whether two values are equal

	In Excel: ``DELTA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DELTA(", *inner, ")", res_type=res_type, **kwargs)

def DEVSQ(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the sum of squares of deviations

	In Excel: ``DEVSQ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DEVSQ(", *inner, ")", res_type=res_type, **kwargs)

def DGET(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Extracts from a database a single record that matches the specified criteria

	In Excel: ``DGET()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DGET(", *inner, ")", res_type=res_type, **kwargs)

def DISC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the discount rate for a security

	In Excel: ``DISC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DISC(", *inner, ")", res_type=res_type, **kwargs)

def DMAX(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Returns the maximum value from selected database entries

	In Excel: ``DMAX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DMAX(", *inner, ")", res_type=res_type, **kwargs)

def DMIN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Returns the minimum value from selected database entries

	In Excel: ``DMIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DMIN(", *inner, ")", res_type=res_type, **kwargs)

def DOLLAR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Converts a number to text, using the $ (dollar) currency format

	In Excel: ``DOLLAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DOLLAR(", *inner, ")", res_type=res_type, **kwargs)

def DOLLARDE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Converts a dollar price, expressed as a fraction, into a dollar price, expressed as a decimal number

	In Excel: ``DOLLARDE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DOLLARDE(", *inner, ")", res_type=res_type, **kwargs)

def DOLLARFR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Converts a dollar price, expressed as a decimal number, into a dollar price, expressed as a fraction

	In Excel: ``DOLLARFR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DOLLARFR(", *inner, ")", res_type=res_type, **kwargs)

def DPRODUCT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Multiplies the values in a particular field of records that match the criteria in a database

	In Excel: ``DPRODUCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DPRODUCT(", *inner, ")", res_type=res_type, **kwargs)

def DROP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Excludes a specified number of rows or columns from the start or end of an array

	In Excel: ``DROP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DROP(", *inner, ")", res_type=res_type, **kwargs)

def DSTDEV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Estimates the standard deviation based on a sample of selected database entries

	In Excel: ``DSTDEV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DSTDEV(", *inner, ")", res_type=res_type, **kwargs)

def DSTDEVP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Calculates the standard deviation based on the entire population of selected database entries

	In Excel: ``DSTDEVP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DSTDEVP(", *inner, ")", res_type=res_type, **kwargs)

def DSUM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Adds the numbers in the field column of records in the database that match the criteria

	In Excel: ``DSUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DSUM(", *inner, ")", res_type=res_type, **kwargs)

def DURATION(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the annual duration of a security with periodic interest payments

	In Excel: ``DURATION()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DURATION(", *inner, ")", res_type=res_type, **kwargs)

def DVAR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Estimates variance based on a sample from selected database entries

	In Excel: ``DVAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DVAR(", *inner, ")", res_type=res_type, **kwargs)

def DVARP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Database:** Calculates variance based on the entire population of selected database entries

	In Excel: ``DVARP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DVARP(", *inner, ")", res_type=res_type, **kwargs)

def EDATE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of the date that is the indicated number of months before or after the start date

	In Excel: ``EDATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EDATE(", *inner, ")", res_type=res_type, **kwargs)

def EFFECT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the effective annual interest rate

	In Excel: ``EFFECT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EFFECT(", *inner, ")", res_type=res_type, **kwargs)

def ENCODEURL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Web:** Returns a URL-encoded string

	In Excel: ``ENCODEURL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ENCODEURL(", *inner, ")", res_type=res_type, **kwargs)

def EOMONTH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of the last day of the month before or after a specified number of months

	In Excel: ``EOMONTH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EOMONTH(", *inner, ")", res_type=res_type, **kwargs)

def ERF(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the error function

	In Excel: ``ERF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ERF(", *inner, ")", res_type=res_type, **kwargs)

def ERF_PRECISE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the error function

	In Excel: ``ERF.PRECISE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ERF.PRECISE(", *inner, ")", res_type=res_type, **kwargs)

def ERFC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the complementary error function

	In Excel: ``ERFC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ERFC(", *inner, ")", res_type=res_type, **kwargs)

def ERFC_PRECISE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the complementary ERF function integrated between x and infinity

	In Excel: ``ERFC.PRECISE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ERFC.PRECISE(", *inner, ")", res_type=res_type, **kwargs)

def ERROR_TYPE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns a number corresponding to an error type

	In Excel: ``ERROR.TYPE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ERROR.TYPE(", *inner, ")", res_type=res_type, **kwargs)

def EUROCONVERT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Add-in and Automation:** Converts a number to euros, converts a number from euros to a euro member currency, or converts a number from one euro member currency to another by using the euro as an intermediary (triangulation).

	In Excel: ``EUROCONVERT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EUROCONVERT(", *inner, ")", res_type=res_type, **kwargs)

def EVEN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number up to the nearest even integer

	In Excel: ``EVEN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EVEN(", *inner, ")", res_type=res_type, **kwargs)

def EXACT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Checks to see if two text values are identical

	In Excel: ``EXACT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EXACT(", *inner, ")", res_type=res_type, **kwargs)

def EXP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns <i class="ocpItalic">e</i> raised to the power of a given number

	In Excel: ``EXP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EXP(", *inner, ")", res_type=res_type, **kwargs)

def EXPAND(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Expands or pads an array to specified row and column dimensions

	In Excel: ``EXPAND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EXPAND(", *inner, ")", res_type=res_type, **kwargs)

def EXPON_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the exponential distribution

	In Excel: ``EXPON.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EXPON.DIST(", *inner, ")", res_type=res_type, **kwargs)

def EXPONDIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the exponential distribution

	In Excel: ``EXPONDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EXPONDIST(", *inner, ")", res_type=res_type, **kwargs)

def FACT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the factorial of a number

	In Excel: ``FACT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FACT(", *inner, ")", res_type=res_type, **kwargs)

def FACTDOUBLE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the double factorial of a number

	In Excel: ``FACTDOUBLE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FACTDOUBLE(", *inner, ")", res_type=res_type, **kwargs)

def FALSE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns the logical value FALSE

	In Excel: ``FALSE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FALSE(", *inner, ")", res_type=res_type, **kwargs)

def F_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the F probability distribution

	In Excel: ``F.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("F.DIST(", *inner, ")", res_type=res_type, **kwargs)

def FDIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the F probability distribution

	In Excel: ``FDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FDIST(", *inner, ")", res_type=res_type, **kwargs)

def F_DIST_RT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the F probability distribution

	In Excel: ``F.DIST.RT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("F.DIST.RT(", *inner, ")", res_type=res_type, **kwargs)

def FILTER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Filters a range of data based on criteria you define

	In Excel: ``FILTER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FILTER(", *inner, ")", res_type=res_type, **kwargs)

def FILTERXML(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Web:** Returns specific data from the XML content by using the specified XPath

	In Excel: ``FILTERXML()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FILTERXML(", *inner, ")", res_type=res_type, **kwargs)

def FIND(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Finds one text value within another (case-sensitive)

	In Excel: ``FIND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FIND(", *inner, ")", res_type=res_type, **kwargs)

def FINDB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Finds one text value within another (case-sensitive)

	In Excel: ``FINDB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FINDB(", *inner, ")", res_type=res_type, **kwargs)

def F_INV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the F probability distribution

	In Excel: ``F.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("F.INV(", *inner, ")", res_type=res_type, **kwargs)

def F_INV_RT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the F probability distribution

	In Excel: ``F.INV.RT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("F.INV.RT(", *inner, ")", res_type=res_type, **kwargs)

def FINV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the F probability distribution

	In Excel: ``FINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FINV(", *inner, ")", res_type=res_type, **kwargs)

def FISHER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Fisher transformation

	In Excel: ``FISHER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FISHER(", *inner, ")", res_type=res_type, **kwargs)

def FISHERINV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the Fisher transformation

	In Excel: ``FISHERINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FISHERINV(", *inner, ")", res_type=res_type, **kwargs)

def FIXED(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Formats a number as text with a fixed number of decimals

	In Excel: ``FIXED()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FIXED(", *inner, ")", res_type=res_type, **kwargs)

def FLOOR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Rounds a number down, toward zero

	In Excel: ``FLOOR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FLOOR(", *inner, ")", res_type=res_type, **kwargs)

def FLOOR_MATH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number down, to the nearest integer or to the nearest multiple of significance

	In Excel: ``FLOOR.MATH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FLOOR.MATH(", *inner, ")", res_type=res_type, **kwargs)

def FLOOR_PRECISE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number the nearest integer or to the nearest multiple of significance. Regardless of the sign of the number, the number is rounded up.

	In Excel: ``FLOOR.PRECISE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FLOOR.PRECISE(", *inner, ")", res_type=res_type, **kwargs)

def FORECAST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns a value along a linear trend

	In Excel: ``FORECAST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FORECAST(", *inner, ")", res_type=res_type, **kwargs)

def FORMULATEXT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the formula at the given reference as text

	In Excel: ``FORMULATEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FORMULATEXT(", *inner, ")", res_type=res_type, **kwargs)

def FREQUENCY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns a frequency distribution as a vertical array

	In Excel: ``FREQUENCY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FREQUENCY(", *inner, ")", res_type=res_type, **kwargs)

def F_TEST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the result of an F-test

	In Excel: ``F.TEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("F.TEST(", *inner, ")", res_type=res_type, **kwargs)

def FTEST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the result of an F-test

	In Excel: ``FTEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FTEST(", *inner, ")", res_type=res_type, **kwargs)

def FV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the future value of an investment

	In Excel: ``FV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FV(", *inner, ")", res_type=res_type, **kwargs)

def FVSCHEDULE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the future value of an initial principal after applying a series of compound interest rates

	In Excel: ``FVSCHEDULE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FVSCHEDULE(", *inner, ")", res_type=res_type, **kwargs)

def GAMMA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Gamma function value

	In Excel: ``GAMMA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMA(", *inner, ")", res_type=res_type, **kwargs)

def GAMMA_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the gamma distribution

	In Excel: ``GAMMA.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMA.DIST(", *inner, ")", res_type=res_type, **kwargs)

def GAMMADIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the gamma distribution

	In Excel: ``GAMMADIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMADIST(", *inner, ")", res_type=res_type, **kwargs)

def GAMMA_INV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the gamma cumulative distribution

	In Excel: ``GAMMA.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMA.INV(", *inner, ")", res_type=res_type, **kwargs)

def GAMMAINV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the gamma cumulative distribution

	In Excel: ``GAMMAINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMAINV(", *inner, ")", res_type=res_type, **kwargs)

def GAMMALN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the natural logarithm of the gamma function, Γ(x)

	In Excel: ``GAMMALN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMALN(", *inner, ")", res_type=res_type, **kwargs)

def GAMMALN_PRECISE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the natural logarithm of the gamma function, Γ(x)

	In Excel: ``GAMMALN.PRECISE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMALN.PRECISE(", *inner, ")", res_type=res_type, **kwargs)

def GAUSS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns 0.5 less than the standard normal cumulative distribution

	In Excel: ``GAUSS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAUSS(", *inner, ")", res_type=res_type, **kwargs)

def GCD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the greatest common divisor

	In Excel: ``GCD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GCD(", *inner, ")", res_type=res_type, **kwargs)

def GEOMEAN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the geometric mean

	In Excel: ``GEOMEAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GEOMEAN(", *inner, ")", res_type=res_type, **kwargs)

def GESTEP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Tests whether a number is greater than a threshold value

	In Excel: ``GESTEP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GESTEP(", *inner, ")", res_type=res_type, **kwargs)

def GETPIVOTDATA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns data stored in a PivotTable report

	In Excel: ``GETPIVOTDATA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GETPIVOTDATA(", *inner, ")", res_type=res_type, **kwargs)

def GROWTH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns values along an exponential trend

	In Excel: ``GROWTH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GROWTH(", *inner, ")", res_type=res_type, **kwargs)

def HARMEAN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the harmonic mean

	In Excel: ``HARMEAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HARMEAN(", *inner, ")", res_type=res_type, **kwargs)

def HEX2BIN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a hexadecimal number to binary

	In Excel: ``HEX2BIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HEX2BIN(", *inner, ")", res_type=res_type, **kwargs)

def HEX2DEC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a hexadecimal number to decimal

	In Excel: ``HEX2DEC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HEX2DEC(", *inner, ")", res_type=res_type, **kwargs)

def HEX2OCT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a hexadecimal number to octal

	In Excel: ``HEX2OCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HEX2OCT(", *inner, ")", res_type=res_type, **kwargs)

def HLOOKUP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Looks in the top row of an array and returns the value of the indicated cell

	In Excel: ``HLOOKUP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HLOOKUP(", *inner, ")", res_type=res_type, **kwargs)

def HOUR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to an hour

	In Excel: ``HOUR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HOUR(", *inner, ")", res_type=res_type, **kwargs)

def HSTACK(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Appends arrays horizontally and in sequence to return a larger array

	In Excel: ``HSTACK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HSTACK(", *inner, ")", res_type=res_type, **kwargs)

def HYPERLINK(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Creates a shortcut or jump that opens a document stored on a network server, an intranet, or the Internet

	In Excel: ``HYPERLINK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HYPERLINK(", *inner, ")", res_type=res_type, **kwargs)

def HYPGEOM_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the hypergeometric distribution

	In Excel: ``HYPGEOM.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HYPGEOM.DIST(", *inner, ")", res_type=res_type, **kwargs)

def HYPGEOMDIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the hypergeometric distribution

	In Excel: ``HYPGEOMDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HYPGEOMDIST(", *inner, ")", res_type=res_type, **kwargs)

def IF(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Specifies a logical test to perform

	In Excel: ``IF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IF(", *inner, ")", res_type=res_type, **kwargs)

def IFERROR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns a value you specify if a formula evaluates to an error; otherwise, returns the result of the formula

	In Excel: ``IFERROR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IFERROR(", *inner, ")", res_type=res_type, **kwargs)

def IFNA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns the value you specify if the expression resolves to #N/A, otherwise returns the result of the expression

	In Excel: ``IFNA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IFNA(", *inner, ")", res_type=res_type, **kwargs)

def IFS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Checks whether one or more conditions are met and returns a value that corresponds to the first TRUE condition.

	In Excel: ``IFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IFS(", *inner, ")", res_type=res_type, **kwargs)

def IMABS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the absolute value (modulus) of a complex number

	In Excel: ``IMABS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMABS(", *inner, ")", res_type=res_type, **kwargs)

def IMAGINARY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the imaginary coefficient of a complex number

	In Excel: ``IMAGINARY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMAGINARY(", *inner, ")", res_type=res_type, **kwargs)

def IMARGUMENT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the argument theta, an angle expressed in radians

	In Excel: ``IMARGUMENT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMARGUMENT(", *inner, ")", res_type=res_type, **kwargs)

def IMCONJUGATE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the complex conjugate of a complex number

	In Excel: ``IMCONJUGATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCONJUGATE(", *inner, ")", res_type=res_type, **kwargs)

def IMCOS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the cosine of a complex number

	In Excel: ``IMCOS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCOS(", *inner, ")", res_type=res_type, **kwargs)

def IMCOSH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the hyperbolic cosine of a complex number

	In Excel: ``IMCOSH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCOSH(", *inner, ")", res_type=res_type, **kwargs)

def IMCOT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the cotangent of a complex number

	In Excel: ``IMCOT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCOT(", *inner, ")", res_type=res_type, **kwargs)

def IMCSC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the cosecant of a complex number

	In Excel: ``IMCSC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCSC(", *inner, ")", res_type=res_type, **kwargs)

def IMCSCH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the hyperbolic cosecant of a complex number

	In Excel: ``IMCSCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCSCH(", *inner, ")", res_type=res_type, **kwargs)

def IMDIV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the quotient of two complex numbers

	In Excel: ``IMDIV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMDIV(", *inner, ")", res_type=res_type, **kwargs)

def IMEXP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the exponential of a complex number

	In Excel: ``IMEXP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMEXP(", *inner, ")", res_type=res_type, **kwargs)

def IMLN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the natural logarithm of a complex number

	In Excel: ``IMLN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMLN(", *inner, ")", res_type=res_type, **kwargs)

def IMLOG10(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the base-10 logarithm of a complex number

	In Excel: ``IMLOG10()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMLOG10(", *inner, ")", res_type=res_type, **kwargs)

def IMLOG2(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the base-2 logarithm of a complex number

	In Excel: ``IMLOG2()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMLOG2(", *inner, ")", res_type=res_type, **kwargs)

def IMPOWER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a complex number raised to an integer power

	In Excel: ``IMPOWER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMPOWER(", *inner, ")", res_type=res_type, **kwargs)

def IMPRODUCT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the product of complex numbers

	In Excel: ``IMPRODUCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMPRODUCT(", *inner, ")", res_type=res_type, **kwargs)

def IMREAL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the real coefficient of a complex number

	In Excel: ``IMREAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMREAL(", *inner, ")", res_type=res_type, **kwargs)

def IMSEC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the secant of a complex number

	In Excel: ``IMSEC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSEC(", *inner, ")", res_type=res_type, **kwargs)

def IMSECH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the hyperbolic secant of a complex number

	In Excel: ``IMSECH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSECH(", *inner, ")", res_type=res_type, **kwargs)

def IMSIN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the sine of a complex number

	In Excel: ``IMSIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSIN(", *inner, ")", res_type=res_type, **kwargs)

def IMSINH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the hyperbolic sine of a complex number

	In Excel: ``IMSINH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSINH(", *inner, ")", res_type=res_type, **kwargs)

def IMSQRT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the square root of a complex number

	In Excel: ``IMSQRT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSQRT(", *inner, ")", res_type=res_type, **kwargs)

def IMSUB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the difference between two complex numbers

	In Excel: ``IMSUB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSUB(", *inner, ")", res_type=res_type, **kwargs)

def IMSUM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the sum of complex numbers

	In Excel: ``IMSUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSUM(", *inner, ")", res_type=res_type, **kwargs)

def IMTAN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the tangent of a complex number

	In Excel: ``IMTAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMTAN(", *inner, ")", res_type=res_type, **kwargs)

def INDEX(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Uses an index to choose a value from a reference or array

	In Excel: ``INDEX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INDEX(", *inner, ")", res_type=res_type, **kwargs)

def INDIRECT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns a reference indicated by a text value

	In Excel: ``INDIRECT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INDIRECT(", *inner, ")", res_type=res_type, **kwargs)

def INFO(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns information about the current operating environment

	In Excel: ``INFO()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INFO(", *inner, ")", res_type=res_type, **kwargs)

def INT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number down to the nearest integer

	In Excel: ``INT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INT(", *inner, ")", res_type=res_type, **kwargs)

def INTERCEPT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the intercept of the linear regression line

	In Excel: ``INTERCEPT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INTERCEPT(", *inner, ")", res_type=res_type, **kwargs)

def INTRATE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the interest rate for a fully invested security

	In Excel: ``INTRATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INTRATE(", *inner, ")", res_type=res_type, **kwargs)

def IPMT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the interest payment for an investment for a given period

	In Excel: ``IPMT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IPMT(", *inner, ")", res_type=res_type, **kwargs)

def IRR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the internal rate of return for a series of cash flows

	In Excel: ``IRR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IRR(", *inner, ")", res_type=res_type, **kwargs)

def ISBLANK(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is blank

	In Excel: ``ISBLANK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISBLANK(", *inner, ")", res_type=res_type, **kwargs)

def ISERR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is any error value except #N/A

	In Excel: ``ISERR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISERR(", *inner, ")", res_type=res_type, **kwargs)

def ISERROR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is any error value

	In Excel: ``ISERROR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISERROR(", *inner, ")", res_type=res_type, **kwargs)

def ISEVEN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the number is even

	In Excel: ``ISEVEN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISEVEN(", *inner, ")", res_type=res_type, **kwargs)

def ISFORMULA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if there is a reference to a cell that contains a formula

	In Excel: ``ISFORMULA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISFORMULA(", *inner, ")", res_type=res_type, **kwargs)

def ISLOGICAL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is a logical value

	In Excel: ``ISLOGICAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISLOGICAL(", *inner, ")", res_type=res_type, **kwargs)

def ISNA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is the #N/A error value

	In Excel: ``ISNA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISNA(", *inner, ")", res_type=res_type, **kwargs)

def ISNONTEXT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is not text

	In Excel: ``ISNONTEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISNONTEXT(", *inner, ")", res_type=res_type, **kwargs)

def ISNUMBER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is a number

	In Excel: ``ISNUMBER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISNUMBER(", *inner, ")", res_type=res_type, **kwargs)

def ISODD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the number is odd

	In Excel: ``ISODD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISODD(", *inner, ")", res_type=res_type, **kwargs)

def ISOMITTED(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Checks whether the value in a LAMBDA is missing and returns TRUE or FALSE

	In Excel: ``ISOMITTED()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISOMITTED(", *inner, ")", res_type=res_type, **kwargs)

def ISREF(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is a reference

	In Excel: ``ISREF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISREF(", *inner, ")", res_type=res_type, **kwargs)

def ISTEXT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is text

	In Excel: ``ISTEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISTEXT(", *inner, ")", res_type=res_type, **kwargs)

def ISO_CEILING(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a number that is rounded up to the nearest integer or to the nearest multiple of significance

	In Excel: ``ISO.CEILING()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISO.CEILING(", *inner, ")", res_type=res_type, **kwargs)

def ISOWEEKNUM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the number of the ISO week number of the year for a given date

	In Excel: ``ISOWEEKNUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISOWEEKNUM(", *inner, ")", res_type=res_type, **kwargs)

def ISPMT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Calculates the interest paid during a specific period of an investment

	In Excel: ``ISPMT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISPMT(", *inner, ")", res_type=res_type, **kwargs)

def JIS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Changes half-width (single-byte) characters within a string to full-width (double-byte) characters

	In Excel: ``JIS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("JIS(", *inner, ")", res_type=res_type, **kwargs)

def KURT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the kurtosis of a data set

	In Excel: ``KURT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("KURT(", *inner, ")", res_type=res_type, **kwargs)

def LAMBDA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Create custom, reusable functions and call them by a friendly name

	In Excel: ``LAMBDA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LAMBDA(", *inner, ")", res_type=res_type, **kwargs)

def LARGE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the k-th largest value in a data set

	In Excel: ``LARGE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LARGE(", *inner, ")", res_type=res_type, **kwargs)

def LCM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the least common multiple

	In Excel: ``LCM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LCM(", *inner, ")", res_type=res_type, **kwargs)

def LEFT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the leftmost characters from a text value

	In Excel: ``LEFT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LEFT(", *inner, ")", res_type=res_type, **kwargs)

def LEFTB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the leftmost characters from a text value

	In Excel: ``LEFTB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LEFTB(", *inner, ")", res_type=res_type, **kwargs)

def LEN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the number of characters in a text string

	In Excel: ``LEN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LEN(", *inner, ")", res_type=res_type, **kwargs)

def LENB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the number of characters in a text string

	In Excel: ``LENB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LENB(", *inner, ")", res_type=res_type, **kwargs)

def LET(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Assigns names to calculation results

	In Excel: ``LET()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LET(", *inner, ")", res_type=res_type, **kwargs)

def LINEST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the parameters of a linear trend

	In Excel: ``LINEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LINEST(", *inner, ")", res_type=res_type, **kwargs)

def LN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the natural logarithm of a number

	In Excel: ``LN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LN(", *inner, ")", res_type=res_type, **kwargs)

def LOG(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the logarithm of a number to a specified base

	In Excel: ``LOG()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOG(", *inner, ")", res_type=res_type, **kwargs)

def LOG10(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the base-10 logarithm of a number

	In Excel: ``LOG10()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOG10(", *inner, ")", res_type=res_type, **kwargs)

def LOGEST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the parameters of an exponential trend

	In Excel: ``LOGEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOGEST(", *inner, ")", res_type=res_type, **kwargs)

def LOGINV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the lognormal cumulative distribution

	In Excel: ``LOGINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOGINV(", *inner, ")", res_type=res_type, **kwargs)

def LOGNORM_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the cumulative lognormal distribution

	In Excel: ``LOGNORM.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOGNORM.DIST(", *inner, ")", res_type=res_type, **kwargs)

def LOGNORMDIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the cumulative lognormal distribution

	In Excel: ``LOGNORMDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOGNORMDIST(", *inner, ")", res_type=res_type, **kwargs)

def LOGNORM_INV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the lognormal cumulative distribution

	In Excel: ``LOGNORM.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOGNORM.INV(", *inner, ")", res_type=res_type, **kwargs)

def LOOKUP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Looks up values in a vector or array

	In Excel: ``LOOKUP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOOKUP(", *inner, ")", res_type=res_type, **kwargs)

def LOWER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Converts text to lowercase

	In Excel: ``LOWER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOWER(", *inner, ")", res_type=res_type, **kwargs)

def MAKEARRAY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns a calculated array of a specified row and column size, by applying a LAMBDA

	In Excel: ``MAKEARRAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MAKEARRAY(", *inner, ")", res_type=res_type, **kwargs)

def MAP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns an array formed by mapping each value in the array(s) to a new value by applying a LAMBDA to create a new value

	In Excel: ``MAP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MAP(", *inner, ")", res_type=res_type, **kwargs)

def MATCH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Looks up values in a reference or array

	In Excel: ``MATCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MATCH(", *inner, ")", res_type=res_type, **kwargs)

def MAX(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the maximum value in a list of arguments

	In Excel: ``MAX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MAX(", *inner, ")", res_type=res_type, **kwargs)

def MAXA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the maximum value in a list of arguments, including numbers, text, and logical values

	In Excel: ``MAXA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MAXA(", *inner, ")", res_type=res_type, **kwargs)

def MAXIFS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the maximum value among cells specified by a given set of conditions or criteria

	In Excel: ``MAXIFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MAXIFS(", *inner, ")", res_type=res_type, **kwargs)

def MDETERM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the matrix determinant of an array

	In Excel: ``MDETERM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MDETERM(", *inner, ")", res_type=res_type, **kwargs)

def MDURATION(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the Macauley modified duration for a security with an assumed par value of $100

	In Excel: ``MDURATION()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MDURATION(", *inner, ")", res_type=res_type, **kwargs)

def MEDIAN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the median of the given numbers

	In Excel: ``MEDIAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MEDIAN(", *inner, ")", res_type=res_type, **kwargs)

def MID(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns a specific number of characters from a text string starting at the position you specify

	In Excel: ``MID()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MID(", *inner, ")", res_type=res_type, **kwargs)

def MIDB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns a specific number of characters from a text string starting at the position you specify

	In Excel: ``MIDB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MIDB(", *inner, ")", res_type=res_type, **kwargs)

def MIN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the minimum value in a list of arguments

	In Excel: ``MIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MIN(", *inner, ")", res_type=res_type, **kwargs)

def MINIFS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the minimum value among cells specified by a given set of conditions or criteria.

	In Excel: ``MINIFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MINIFS(", *inner, ")", res_type=res_type, **kwargs)

def MINA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the smallest value in a list of arguments, including numbers, text, and logical values

	In Excel: ``MINA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MINA(", *inner, ")", res_type=res_type, **kwargs)

def MINUTE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a minute

	In Excel: ``MINUTE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MINUTE(", *inner, ")", res_type=res_type, **kwargs)

def MINVERSE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the matrix inverse of an array

	In Excel: ``MINVERSE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MINVERSE(", *inner, ")", res_type=res_type, **kwargs)

def MIRR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the internal rate of return where positive and negative cash flows are financed at different rates

	In Excel: ``MIRR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MIRR(", *inner, ")", res_type=res_type, **kwargs)

def MMULT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the matrix product of two arrays

	In Excel: ``MMULT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MMULT(", *inner, ")", res_type=res_type, **kwargs)

def MOD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the remainder from division

	In Excel: ``MOD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MOD(", *inner, ")", res_type=res_type, **kwargs)

def MODE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the most common value in a data set

	In Excel: ``MODE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MODE(", *inner, ")", res_type=res_type, **kwargs)

def MODE_MULT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns a vertical array of the most frequently occurring, or repetitive values in an array or range of data

	In Excel: ``MODE.MULT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MODE.MULT(", *inner, ")", res_type=res_type, **kwargs)

def MODE_SNGL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the most common value in a data set

	In Excel: ``MODE.SNGL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MODE.SNGL(", *inner, ")", res_type=res_type, **kwargs)

def MONTH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a month

	In Excel: ``MONTH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MONTH(", *inner, ")", res_type=res_type, **kwargs)

def MROUND(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a number rounded to the desired multiple

	In Excel: ``MROUND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MROUND(", *inner, ")", res_type=res_type, **kwargs)

def MULTINOMIAL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the multinomial of a set of numbers

	In Excel: ``MULTINOMIAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MULTINOMIAL(", *inner, ")", res_type=res_type, **kwargs)

def MUNIT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the unit matrix or the specified dimension

	In Excel: ``MUNIT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MUNIT(", *inner, ")", res_type=res_type, **kwargs)

def N(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns a value converted to a number

	In Excel: ``N()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("N(", *inner, ")", res_type=res_type, **kwargs)

def NA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns the error value #N/A

	In Excel: ``NA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NA(", *inner, ")", res_type=res_type, **kwargs)

def NEGBINOM_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the negative binomial distribution

	In Excel: ``NEGBINOM.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NEGBINOM.DIST(", *inner, ")", res_type=res_type, **kwargs)

def NEGBINOMDIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the negative binomial distribution

	In Excel: ``NEGBINOMDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NEGBINOMDIST(", *inner, ")", res_type=res_type, **kwargs)

def NETWORKDAYS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the number of whole workdays between two dates

	In Excel: ``NETWORKDAYS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NETWORKDAYS(", *inner, ")", res_type=res_type, **kwargs)

def NETWORKDAYS_INTL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the number of whole workdays between two dates using parameters to indicate which and how many days are weekend days

	In Excel: ``NETWORKDAYS.INTL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NETWORKDAYS.INTL(", *inner, ")", res_type=res_type, **kwargs)

def NOMINAL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the annual nominal interest rate

	In Excel: ``NOMINAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NOMINAL(", *inner, ")", res_type=res_type, **kwargs)

def NORM_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the normal cumulative distribution

	In Excel: ``NORM.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORM.DIST(", *inner, ")", res_type=res_type, **kwargs)

def NORMDIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the normal cumulative distribution

	In Excel: ``NORMDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORMDIST(", *inner, ")", res_type=res_type, **kwargs)

def NORMINV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the normal cumulative distribution

	In Excel: ``NORMINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORMINV(", *inner, ")", res_type=res_type, **kwargs)

def NORM_INV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the normal cumulative distribution

	In Excel: ``NORM.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORM.INV(", *inner, ")", res_type=res_type, **kwargs)

def NORM_S_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the standard normal cumulative distribution

	In Excel: ``NORM.S.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORM.S.DIST(", *inner, ")", res_type=res_type, **kwargs)

def NORMSDIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the standard normal cumulative distribution

	In Excel: ``NORMSDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORMSDIST(", *inner, ")", res_type=res_type, **kwargs)

def NORM_S_INV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the standard normal cumulative distribution

	In Excel: ``NORM.S.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORM.S.INV(", *inner, ")", res_type=res_type, **kwargs)

def NORMSINV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the standard normal cumulative distribution

	In Excel: ``NORMSINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORMSINV(", *inner, ")", res_type=res_type, **kwargs)

def NOT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Reverses the logic of its argument

	In Excel: ``NOT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NOT(", *inner, ")", res_type=res_type, **kwargs)

def NOW(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of the current date and time

	In Excel: ``NOW()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NOW(", *inner, ")", res_type=res_type, **kwargs)

def NPER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of periods for an investment

	In Excel: ``NPER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NPER(", *inner, ")", res_type=res_type, **kwargs)

def NPV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the net present value of an investment based on a series of periodic cash flows and a discount rate

	In Excel: ``NPV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NPV(", *inner, ")", res_type=res_type, **kwargs)

def NUMBERVALUE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Converts text to number in a locale-independent manner

	In Excel: ``NUMBERVALUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NUMBERVALUE(", *inner, ")", res_type=res_type, **kwargs)

def OCT2BIN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts an octal number to binary

	In Excel: ``OCT2BIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("OCT2BIN(", *inner, ")", res_type=res_type, **kwargs)

def OCT2DEC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts an octal number to decimal

	In Excel: ``OCT2DEC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("OCT2DEC(", *inner, ")", res_type=res_type, **kwargs)

def OCT2HEX(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts an octal number to hexadecimal

	In Excel: ``OCT2HEX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("OCT2HEX(", *inner, ")", res_type=res_type, **kwargs)

def ODD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number up to the nearest odd integer

	In Excel: ``ODD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ODD(", *inner, ")", res_type=res_type, **kwargs)

def ODDFPRICE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value of a security with an odd first period

	In Excel: ``ODDFPRICE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ODDFPRICE(", *inner, ")", res_type=res_type, **kwargs)

def ODDFYIELD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the yield of a security with an odd first period

	In Excel: ``ODDFYIELD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ODDFYIELD(", *inner, ")", res_type=res_type, **kwargs)

def ODDLPRICE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value of a security with an odd last period

	In Excel: ``ODDLPRICE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ODDLPRICE(", *inner, ")", res_type=res_type, **kwargs)

def ODDLYIELD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the yield of a security with an odd last period

	In Excel: ``ODDLYIELD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ODDLYIELD(", *inner, ")", res_type=res_type, **kwargs)

def OFFSET(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns a reference offset from a given reference

	In Excel: ``OFFSET()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("OFFSET(", *inner, ")", res_type=res_type, **kwargs)

def OR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns TRUE if any argument is TRUE

	In Excel: ``OR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("OR(", *inner, ")", res_type=res_type, **kwargs)

def PDURATION(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of periods required by an investment to reach a specified value

	In Excel: ``PDURATION()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PDURATION(", *inner, ")", res_type=res_type, **kwargs)

def PEARSON(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Pearson product moment correlation coefficient

	In Excel: ``PEARSON()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PEARSON(", *inner, ")", res_type=res_type, **kwargs)

def PERCENTILE_EXC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the k-th percentile of values in a range, where k is in the range 0..1, exclusive

	In Excel: ``PERCENTILE.EXC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTILE.EXC(", *inner, ")", res_type=res_type, **kwargs)

def PERCENTILE_INC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the k-th percentile of values in a range

	In Excel: ``PERCENTILE.INC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTILE.INC(", *inner, ")", res_type=res_type, **kwargs)

def PERCENTILE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the k-th percentile of values in a range

	In Excel: ``PERCENTILE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTILE(", *inner, ")", res_type=res_type, **kwargs)

def PERCENTRANK_EXC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the rank of a value in a data set as a percentage (0..1, exclusive) of the data set

	In Excel: ``PERCENTRANK.EXC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTRANK.EXC(", *inner, ")", res_type=res_type, **kwargs)

def PERCENTRANK_INC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the percentage rank of a value in a data set

	In Excel: ``PERCENTRANK.INC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTRANK.INC(", *inner, ")", res_type=res_type, **kwargs)

def PERCENTRANK(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the percentage rank of a value in a data set

	In Excel: ``PERCENTRANK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTRANK(", *inner, ")", res_type=res_type, **kwargs)

def PERMUT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the number of permutations for a given number of objects

	In Excel: ``PERMUT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERMUT(", *inner, ")", res_type=res_type, **kwargs)

def PERMUTATIONA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the number of permutations for a given number of objects (with repetitions) that can be selected from the total objects

	In Excel: ``PERMUTATIONA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERMUTATIONA(", *inner, ")", res_type=res_type, **kwargs)

def PHI(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the value of the density function for a standard normal distribution

	In Excel: ``PHI()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PHI(", *inner, ")", res_type=res_type, **kwargs)

def PHONETIC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Extracts the phonetic (furigana) characters from a text string

	In Excel: ``PHONETIC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PHONETIC(", *inner, ")", res_type=res_type, **kwargs)

def PI(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the value of pi

	In Excel: ``PI()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PI(", *inner, ")", res_type=res_type, **kwargs)

def PMT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the periodic payment for an annuity

	In Excel: ``PMT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PMT(", *inner, ")", res_type=res_type, **kwargs)

def POISSON_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Poisson distribution

	In Excel: ``POISSON.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("POISSON.DIST(", *inner, ")", res_type=res_type, **kwargs)

def POISSON(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the Poisson distribution

	In Excel: ``POISSON()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("POISSON(", *inner, ")", res_type=res_type, **kwargs)

def POWER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the result of a number raised to a power

	In Excel: ``POWER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("POWER(", *inner, ")", res_type=res_type, **kwargs)

def PPMT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the payment on the principal for an investment for a given period

	In Excel: ``PPMT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PPMT(", *inner, ")", res_type=res_type, **kwargs)

def PRICE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value of a security that pays periodic interest

	In Excel: ``PRICE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PRICE(", *inner, ")", res_type=res_type, **kwargs)

def PRICEDISC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value of a discounted security

	In Excel: ``PRICEDISC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PRICEDISC(", *inner, ")", res_type=res_type, **kwargs)

def PRICEMAT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value of a security that pays interest at maturity

	In Excel: ``PRICEMAT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PRICEMAT(", *inner, ")", res_type=res_type, **kwargs)

def PROB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the probability that values in a range are between two limits

	In Excel: ``PROB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PROB(", *inner, ")", res_type=res_type, **kwargs)

def PRODUCT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Multiplies its arguments

	In Excel: ``PRODUCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PRODUCT(", *inner, ")", res_type=res_type, **kwargs)

def PROPER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Capitalizes the first letter in each word of a text value

	In Excel: ``PROPER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PROPER(", *inner, ")", res_type=res_type, **kwargs)

def PV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the present value of an investment

	In Excel: ``PV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PV(", *inner, ")", res_type=res_type, **kwargs)

def QUARTILE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the quartile of a data set

	In Excel: ``QUARTILE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("QUARTILE(", *inner, ")", res_type=res_type, **kwargs)

def QUARTILE_EXC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the quartile of the data set, based on percentile values from 0..1, exclusive

	In Excel: ``QUARTILE.EXC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("QUARTILE.EXC(", *inner, ")", res_type=res_type, **kwargs)

def QUARTILE_INC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the quartile of a data set

	In Excel: ``QUARTILE.INC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("QUARTILE.INC(", *inner, ")", res_type=res_type, **kwargs)

def QUOTIENT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the integer portion of a division

	In Excel: ``QUOTIENT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("QUOTIENT(", *inner, ")", res_type=res_type, **kwargs)

def RADIANS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts degrees to radians

	In Excel: ``RADIANS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RADIANS(", *inner, ")", res_type=res_type, **kwargs)

def RAND(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a random number between 0 and 1

	In Excel: ``RAND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RAND(", *inner, ")", res_type=res_type, **kwargs)

def RANDARRAY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns an array of random numbers between 0 and 1. However, you can specify the number of rows and columns to fill, minimum and maximum values, and whether to return whole numbers or decimal values.

	In Excel: ``RANDARRAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RANDARRAY(", *inner, ")", res_type=res_type, **kwargs)

def RANDBETWEEN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a random number between the numbers you specify

	In Excel: ``RANDBETWEEN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RANDBETWEEN(", *inner, ")", res_type=res_type, **kwargs)

def RANK_AVG(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the rank of a number in a list of numbers

	In Excel: ``RANK.AVG()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RANK.AVG(", *inner, ")", res_type=res_type, **kwargs)

def RANK_EQ(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the rank of a number in a list of numbers

	In Excel: ``RANK.EQ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RANK.EQ(", *inner, ")", res_type=res_type, **kwargs)

def RANK(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the rank of a number in a list of numbers

	In Excel: ``RANK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RANK(", *inner, ")", res_type=res_type, **kwargs)

def RATE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the interest rate per period of an annuity

	In Excel: ``RATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RATE(", *inner, ")", res_type=res_type, **kwargs)

def RECEIVED(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the amount received at maturity for a fully invested security

	In Excel: ``RECEIVED()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RECEIVED(", *inner, ")", res_type=res_type, **kwargs)

def REDUCE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Reduces an array to an accumulated value by applying a LAMBDA to each value and returning the total value in the accumulator

	In Excel: ``REDUCE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("REDUCE(", *inner, ")", res_type=res_type, **kwargs)

def REGISTER_ID(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Add-in and Automation:** Returns the register ID of the specified dynamic link library (DLL) or code resource that has been previously registered

	In Excel: ``REGISTER.ID()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("REGISTER.ID(", *inner, ")", res_type=res_type, **kwargs)

def REPLACE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Replaces characters within text

	In Excel: ``REPLACE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("REPLACE(", *inner, ")", res_type=res_type, **kwargs)

def REPLACEB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Replaces characters within text

	In Excel: ``REPLACEB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("REPLACEB(", *inner, ")", res_type=res_type, **kwargs)

def REPT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Repeats text a given number of times

	In Excel: ``REPT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("REPT(", *inner, ")", res_type=res_type, **kwargs)

def RIGHT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the rightmost characters from a text value

	In Excel: ``RIGHT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RIGHT(", *inner, ")", res_type=res_type, **kwargs)

def RIGHTB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the rightmost characters from a text value

	In Excel: ``RIGHTB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RIGHTB(", *inner, ")", res_type=res_type, **kwargs)

def ROMAN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts an arabic numeral to roman, as text

	In Excel: ``ROMAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROMAN(", *inner, ")", res_type=res_type, **kwargs)

def ROUND(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number to a specified number of digits

	In Excel: ``ROUND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROUND(", *inner, ")", res_type=res_type, **kwargs)

def ROUNDDOWN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number down, toward zero

	In Excel: ``ROUNDDOWN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROUNDDOWN(", *inner, ")", res_type=res_type, **kwargs)

def ROUNDUP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number up, away from zero

	In Excel: ``ROUNDUP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROUNDUP(", *inner, ")", res_type=res_type, **kwargs)

def ROW(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the row number of a reference

	In Excel: ``ROW()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROW(", *inner, ")", res_type=res_type, **kwargs)

def ROWS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the number of rows in a reference

	In Excel: ``ROWS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROWS(", *inner, ")", res_type=res_type, **kwargs)

def RRI(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns an equivalent interest rate for the growth of an investment

	In Excel: ``RRI()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RRI(", *inner, ")", res_type=res_type, **kwargs)

def RSQ(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the square of the Pearson product moment correlation coefficient

	In Excel: ``RSQ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RSQ(", *inner, ")", res_type=res_type, **kwargs)

def RTD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Retrieves real-time data from a program that supports COM automation

	In Excel: ``RTD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RTD(", *inner, ")", res_type=res_type, **kwargs)

def SCAN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Scans an array by applying a LAMBDA to each value and returns an array that has each intermediate value

	In Excel: ``SCAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SCAN(", *inner, ")", res_type=res_type, **kwargs)

def SEARCH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Finds one text value within another (not case-sensitive)

	In Excel: ``SEARCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SEARCH(", *inner, ")", res_type=res_type, **kwargs)

def SEARCHB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Finds one text value within another (not case-sensitive)

	In Excel: ``SEARCHB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SEARCHB(", *inner, ")", res_type=res_type, **kwargs)

def SEC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the secant of an angle

	In Excel: ``SEC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SEC(", *inner, ")", res_type=res_type, **kwargs)

def SECH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic secant of an angle

	In Excel: ``SECH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SECH(", *inner, ")", res_type=res_type, **kwargs)

def SECOND(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a second

	In Excel: ``SECOND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SECOND(", *inner, ")", res_type=res_type, **kwargs)

def SEQUENCE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Generates a list of sequential numbers in an array, such as 1, 2, 3, 4

	In Excel: ``SEQUENCE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SEQUENCE(", *inner, ")", res_type=res_type, **kwargs)

def SERIESSUM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of a power series based on the formula

	In Excel: ``SERIESSUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SERIESSUM(", *inner, ")", res_type=res_type, **kwargs)

def SHEET(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns the sheet number of the referenced sheet

	In Excel: ``SHEET()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SHEET(", *inner, ")", res_type=res_type, **kwargs)

def SHEETS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns the number of sheets in a reference

	In Excel: ``SHEETS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SHEETS(", *inner, ")", res_type=res_type, **kwargs)

def SIGN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sign of a number

	In Excel: ``SIGN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SIGN(", *inner, ")", res_type=res_type, **kwargs)

def SIN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sine of the given angle

	In Excel: ``SIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SIN(", *inner, ")", res_type=res_type, **kwargs)

def SINH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic sine of a number

	In Excel: ``SINH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SINH(", *inner, ")", res_type=res_type, **kwargs)

def SKEW(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the skewness of a distribution

	In Excel: ``SKEW()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SKEW(", *inner, ")", res_type=res_type, **kwargs)

def SKEW_P(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the skewness of a distribution based on a population: a characterization of the degree of asymmetry of a distribution around its mean

	In Excel: ``SKEW.P()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SKEW.P(", *inner, ")", res_type=res_type, **kwargs)

def SLN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the straight-line depreciation of an asset for one period

	In Excel: ``SLN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SLN(", *inner, ")", res_type=res_type, **kwargs)

def SLOPE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the slope of the linear regression line

	In Excel: ``SLOPE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SLOPE(", *inner, ")", res_type=res_type, **kwargs)

def SMALL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the k-th smallest value in a data set

	In Excel: ``SMALL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SMALL(", *inner, ")", res_type=res_type, **kwargs)

def SORT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Sorts the contents of a range or array

	In Excel: ``SORT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SORT(", *inner, ")", res_type=res_type, **kwargs)

def SORTBY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Sorts the contents of a range or array based on the values in a corresponding range or array

	In Excel: ``SORTBY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SORTBY(", *inner, ")", res_type=res_type, **kwargs)

def SQRT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a positive square root

	In Excel: ``SQRT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SQRT(", *inner, ")", res_type=res_type, **kwargs)

def SQRTPI(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the square root of (number * pi)

	In Excel: ``SQRTPI()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SQRTPI(", *inner, ")", res_type=res_type, **kwargs)

def STANDARDIZE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns a normalized value

	In Excel: ``STANDARDIZE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STANDARDIZE(", *inner, ")", res_type=res_type, **kwargs)

def STOCKHISTORY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Retrieves historical data about a financial instrument

	In Excel: ``STOCKHISTORY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STOCKHISTORY(", *inner, ")", res_type=res_type, **kwargs)

def STDEV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Estimates standard deviation based on a sample

	In Excel: ``STDEV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEV(", *inner, ")", res_type=res_type, **kwargs)

def STDEV_P(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Calculates standard deviation based on the entire population

	In Excel: ``STDEV.P()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEV.P(", *inner, ")", res_type=res_type, **kwargs)

def STDEV_S(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Estimates standard deviation based on a sample

	In Excel: ``STDEV.S()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEV.S(", *inner, ")", res_type=res_type, **kwargs)

def STDEVA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Estimates standard deviation based on a sample, including numbers, text, and logical values

	In Excel: ``STDEVA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEVA(", *inner, ")", res_type=res_type, **kwargs)

def STDEVP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Calculates standard deviation based on the entire population

	In Excel: ``STDEVP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEVP(", *inner, ")", res_type=res_type, **kwargs)

def STDEVPA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Calculates standard deviation based on the entire population, including numbers, text, and logical values

	In Excel: ``STDEVPA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEVPA(", *inner, ")", res_type=res_type, **kwargs)

def STEYX(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the standard error of the predicted y-value for each x in the regression

	In Excel: ``STEYX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STEYX(", *inner, ")", res_type=res_type, **kwargs)

def SUBSTITUTE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Substitutes new text for old text in a text string

	In Excel: ``SUBSTITUTE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUBSTITUTE(", *inner, ")", res_type=res_type, **kwargs)

def SUBTOTAL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a subtotal in a list or database

	In Excel: ``SUBTOTAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUBTOTAL(", *inner, ")", res_type=res_type, **kwargs)

def SUM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Adds its arguments

	In Excel: ``SUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUM(", *inner, ")", res_type=res_type, **kwargs)

def SUMIF(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Adds the cells specified by a given criteria

	In Excel: ``SUMIF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMIF(", *inner, ")", res_type=res_type, **kwargs)

def SUMIFS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Adds the cells in a range that meet multiple criteria

	In Excel: ``SUMIFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMIFS(", *inner, ")", res_type=res_type, **kwargs)

def SUMPRODUCT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of the products of corresponding array components

	In Excel: ``SUMPRODUCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMPRODUCT(", *inner, ")", res_type=res_type, **kwargs)

def SUMSQ(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of the squares of the arguments

	In Excel: ``SUMSQ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMSQ(", *inner, ")", res_type=res_type, **kwargs)

def SUMX2MY2(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of the difference of squares of corresponding values in two arrays

	In Excel: ``SUMX2MY2()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMX2MY2(", *inner, ")", res_type=res_type, **kwargs)

def SUMX2PY2(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of the sum of squares of corresponding values in two arrays

	In Excel: ``SUMX2PY2()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMX2PY2(", *inner, ")", res_type=res_type, **kwargs)

def SUMXMY2(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of squares of differences of corresponding values in two arrays

	In Excel: ``SUMXMY2()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMXMY2(", *inner, ")", res_type=res_type, **kwargs)

def SWITCH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Evaluates an expression against a list of values and returns the result corresponding to the first matching value. If there is no match, an optional default value may be returned.

	In Excel: ``SWITCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SWITCH(", *inner, ")", res_type=res_type, **kwargs)

def SYD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the sum-of-years' digits depreciation of an asset for a specified period

	In Excel: ``SYD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SYD(", *inner, ")", res_type=res_type, **kwargs)

def T(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Converts its arguments to text

	In Excel: ``T()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T(", *inner, ")", res_type=res_type, **kwargs)

def TAN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the tangent of a number

	In Excel: ``TAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TAN(", *inner, ")", res_type=res_type, **kwargs)

def TANH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic tangent of a number

	In Excel: ``TANH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TANH(", *inner, ")", res_type=res_type, **kwargs)

def TAKE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns a specified number of contiguous rows or columns from the start or end of an array

	In Excel: ``TAKE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TAKE(", *inner, ")", res_type=res_type, **kwargs)

def TBILLEQ(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the bond-equivalent yield for a Treasury bill

	In Excel: ``TBILLEQ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TBILLEQ(", *inner, ")", res_type=res_type, **kwargs)

def TBILLPRICE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value for a Treasury bill

	In Excel: ``TBILLPRICE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TBILLPRICE(", *inner, ")", res_type=res_type, **kwargs)

def TBILLYIELD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the yield for a Treasury bill

	In Excel: ``TBILLYIELD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TBILLYIELD(", *inner, ")", res_type=res_type, **kwargs)

def T_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Percentage Points (probability) for the Student t-distribution

	In Excel: ``T.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.DIST(", *inner, ")", res_type=res_type, **kwargs)

def T_DIST_2T(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Percentage Points (probability) for the Student t-distribution

	In Excel: ``T.DIST.2T()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.DIST.2T(", *inner, ")", res_type=res_type, **kwargs)

def T_DIST_RT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Student's t-distribution

	In Excel: ``T.DIST.RT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.DIST.RT(", *inner, ")", res_type=res_type, **kwargs)

def TDIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the Student's t-distribution

	In Excel: ``TDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TDIST(", *inner, ")", res_type=res_type, **kwargs)

def TEXT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Formats a number and converts it to text

	In Excel: ``TEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TEXT(", *inner, ")", res_type=res_type, **kwargs)

def TEXTAFTER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns text that occurs after given character or string

	In Excel: ``TEXTAFTER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TEXTAFTER(", *inner, ")", res_type=res_type, **kwargs)

def TEXTBEFORE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns text that occurs before a given character or string

	In Excel: ``TEXTBEFORE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TEXTBEFORE(", *inner, ")", res_type=res_type, **kwargs)

def TEXTJOIN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Combines the text from multiple ranges and/or strings

	In Excel: ``TEXTJOIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TEXTJOIN(", *inner, ")", res_type=res_type, **kwargs)

def TEXTSPLIT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Splits text strings by using column and row delimiters

	In Excel: ``TEXTSPLIT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TEXTSPLIT(", *inner, ")", res_type=res_type, **kwargs)

def TIME(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of a particular time

	In Excel: ``TIME()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TIME(", *inner, ")", res_type=res_type, **kwargs)

def TIMEVALUE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a time in the form of text to a serial number

	In Excel: ``TIMEVALUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TIMEVALUE(", *inner, ")", res_type=res_type, **kwargs)

def T_INV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the t-value of the Student's t-distribution as a function of the probability and the degrees of freedom

	In Excel: ``T.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.INV(", *inner, ")", res_type=res_type, **kwargs)

def T_INV_2T(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the Student's t-distribution

	In Excel: ``T.INV.2T()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.INV.2T(", *inner, ")", res_type=res_type, **kwargs)

def TINV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the Student's t-distribution

	In Excel: ``TINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TINV(", *inner, ")", res_type=res_type, **kwargs)

def TOCOL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the array in a single column

	In Excel: ``TOCOL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TOCOL(", *inner, ")", res_type=res_type, **kwargs)

def TOROW(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the array in a single row

	In Excel: ``TOROW()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TOROW(", *inner, ")", res_type=res_type, **kwargs)

def TODAY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of today's date

	In Excel: ``TODAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TODAY(", *inner, ")", res_type=res_type, **kwargs)

def TRANSPOSE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the transpose of an array

	In Excel: ``TRANSPOSE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TRANSPOSE(", *inner, ")", res_type=res_type, **kwargs)

def TREND(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns values along a linear trend

	In Excel: ``TREND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TREND(", *inner, ")", res_type=res_type, **kwargs)

def TRIM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Removes spaces from text

	In Excel: ``TRIM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TRIM(", *inner, ")", res_type=res_type, **kwargs)

def TRIMMEAN(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the mean of the interior of a data set

	In Excel: ``TRIMMEAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TRIMMEAN(", *inner, ")", res_type=res_type, **kwargs)

def TRUE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns the logical value TRUE

	In Excel: ``TRUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TRUE(", *inner, ")", res_type=res_type, **kwargs)

def TRUNC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Truncates a number to an integer

	In Excel: ``TRUNC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TRUNC(", *inner, ")", res_type=res_type, **kwargs)

def T_TEST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the probability associated with a Student's t-test

	In Excel: ``T.TEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.TEST(", *inner, ")", res_type=res_type, **kwargs)

def TTEST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the probability associated with a Student's t-test

	In Excel: ``TTEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TTEST(", *inner, ")", res_type=res_type, **kwargs)

def TYPE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Information:** Returns a number indicating the data type of a value

	In Excel: ``TYPE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TYPE(", *inner, ")", res_type=res_type, **kwargs)

def UNICHAR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the Unicode character that is references by the given numeric value

	In Excel: ``UNICHAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("UNICHAR(", *inner, ")", res_type=res_type, **kwargs)

def UNICODE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the number (code point) that corresponds to the first character of the text

	In Excel: ``UNICODE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("UNICODE(", *inner, ")", res_type=res_type, **kwargs)

def UNIQUE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns a list of unique values in a list or range

	In Excel: ``UNIQUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("UNIQUE(", *inner, ")", res_type=res_type, **kwargs)

def UPPER(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Converts text to uppercase

	In Excel: ``UPPER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("UPPER(", *inner, ")", res_type=res_type, **kwargs)

def VALUE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Converts a text argument to a number

	In Excel: ``VALUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VALUE(", *inner, ")", res_type=res_type, **kwargs)

def VALUETOTEXT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Text:** Returns text from any specified value

	In Excel: ``VALUETOTEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VALUETOTEXT(", *inner, ")", res_type=res_type, **kwargs)

def VAR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Estimates variance based on a sample

	In Excel: ``VAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VAR(", *inner, ")", res_type=res_type, **kwargs)

def VAR_P(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Calculates variance based on the entire population

	In Excel: ``VAR.P()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VAR.P(", *inner, ")", res_type=res_type, **kwargs)

def VAR_S(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Estimates variance based on a sample

	In Excel: ``VAR.S()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VAR.S(", *inner, ")", res_type=res_type, **kwargs)

def VARA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Estimates variance based on a sample, including numbers, text, and logical values

	In Excel: ``VARA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VARA(", *inner, ")", res_type=res_type, **kwargs)

def VARP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Calculates variance based on the entire population

	In Excel: ``VARP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VARP(", *inner, ")", res_type=res_type, **kwargs)

def VARPA(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Calculates variance based on the entire population, including numbers, text, and logical values

	In Excel: ``VARPA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VARPA(", *inner, ")", res_type=res_type, **kwargs)

def VDB(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the depreciation of an asset for a specified or partial period by using a declining balance method

	In Excel: ``VDB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VDB(", *inner, ")", res_type=res_type, **kwargs)

def VLOOKUP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Looks in the first column of an array and moves across the row to return the value of a cell

	In Excel: ``VLOOKUP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VLOOKUP(", *inner, ")", res_type=res_type, **kwargs)

def VSTACK(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Look and reference:** Appends arrays vertically and in sequence to return a larger array

	In Excel: ``VSTACK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VSTACK(", *inner, ")", res_type=res_type, **kwargs)

def WEBSERVICE(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Web:** Returns data from a web service.

	In Excel: ``WEBSERVICE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WEBSERVICE(", *inner, ")", res_type=res_type, **kwargs)

def WEEKDAY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a day of the week

	In Excel: ``WEEKDAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WEEKDAY(", *inner, ")", res_type=res_type, **kwargs)

def WEEKNUM(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a number representing where the week falls numerically with a year

	In Excel: ``WEEKNUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WEEKNUM(", *inner, ")", res_type=res_type, **kwargs)

def WEIBULL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Calculates variance based on the entire population, including numbers, text, and logical values

	In Excel: ``WEIBULL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WEIBULL(", *inner, ")", res_type=res_type, **kwargs)

def WEIBULL_DIST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Weibull distribution

	In Excel: ``WEIBULL.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WEIBULL.DIST(", *inner, ")", res_type=res_type, **kwargs)

def WORKDAY(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of the date before or after a specified number of workdays

	In Excel: ``WORKDAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WORKDAY(", *inner, ")", res_type=res_type, **kwargs)

def WORKDAY_INTL(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of the date before or after a specified number of workdays using parameters to indicate which and how many days are weekend days

	In Excel: ``WORKDAY.INTL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WORKDAY.INTL(", *inner, ")", res_type=res_type, **kwargs)

def WRAPCOLS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Look and reference:** Wraps the provided row or column of values by columns after a specified number of elements

	In Excel: ``WRAPCOLS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WRAPCOLS(", *inner, ")", res_type=res_type, **kwargs)

def WRAPROWS(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Look and reference:** Wraps the provided row or column of values by rows after a specified number of elements

	In Excel: ``WRAPROWS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WRAPROWS(", *inner, ")", res_type=res_type, **kwargs)

def XIRR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the internal rate of return for a schedule of cash flows that is not necessarily periodic

	In Excel: ``XIRR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("XIRR(", *inner, ")", res_type=res_type, **kwargs)

def XLOOKUP(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Searches a range or an array, and returns an item corresponding to the first match it finds. If a match doesn't exist, then XLOOKUP can return the closest (approximate) match. 

	In Excel: ``XLOOKUP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("XLOOKUP(", *inner, ")", res_type=res_type, **kwargs)

def XMATCH(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the relative position of an item in an array or range of cells. 

	In Excel: ``XMATCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("XMATCH(", *inner, ")", res_type=res_type, **kwargs)

def XNPV(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the net present value for a schedule of cash flows that is not necessarily periodic

	In Excel: ``XNPV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("XNPV(", *inner, ")", res_type=res_type, **kwargs)

def XOR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns a logical exclusive OR of all arguments

	In Excel: ``XOR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("XOR(", *inner, ")", res_type=res_type, **kwargs)

def YEAR(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a year

	In Excel: ``YEAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("YEAR(", *inner, ")", res_type=res_type, **kwargs)

def YEARFRAC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the year fraction representing the number of whole days between start_date and end_date

	In Excel: ``YEARFRAC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("YEARFRAC(", *inner, ")", res_type=res_type, **kwargs)

def YIELD(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the yield on a security that pays periodic interest

	In Excel: ``YIELD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("YIELD(", *inner, ")", res_type=res_type, **kwargs)

def YIELDDISC(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the annual yield for a discounted security; for example, a Treasury bill

	In Excel: ``YIELDDISC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("YIELDDISC(", *inner, ")", res_type=res_type, **kwargs)

def YIELDMAT(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the annual yield of a security that pays interest at maturity

	In Excel: ``YIELDMAT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("YIELDMAT(", *inner, ")", res_type=res_type, **kwargs)

def Z_TEST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the one-tailed probability-value of a z-test

	In Excel: ``Z.TEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("Z.TEST(", *inner, ")", res_type=res_type, **kwargs)

def ZTEST(*inner: Any, res_type: type | None = None, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the one-tailed probability-value of a z-test

	In Excel: ``ZTEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ZTEST(", *inner, ")", res_type=res_type, **kwargs)


