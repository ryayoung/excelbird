"""

.. role:: html(raw)
   :format: html

All ~500 Excel functions can be accessed in Python, from the :mod:`excelbird.fx` module.
Each is documented with the same short summary as provided by Microsoft's documentation.

Allows for autocomplete and documentation preview in your IDE.

**Syntax Example:** Excel's ``T.DIST.2T()`` is :meth:`T_DIST_2T` in `excelbird`.

.. note::

    Each function is shorthand for an :class:`excelbird.Func`

    .. code-block::

        fx.ABS(some_cell)

    is the same as

    .. code-block::

        Func("ABS(", some_cell, ")")

"""
from excelbird.core.function import Func
from typing import Any


def ABS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the absolute value of a number

	In Excel: ``ABS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ABS(", *args, ")", **kwargs)

def ACCRINT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the accrued interest for a security that pays periodic interest

	In Excel: ``ACCRINT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACCRINT(", *args, ")", **kwargs)

def ACCRINTM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the accrued interest for a security that pays interest at maturity

	In Excel: ``ACCRINTM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACCRINTM(", *args, ")", **kwargs)

def ACOS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the arccosine of a number

	In Excel: ``ACOS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACOS(", *args, ")", **kwargs)

def ACOSH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the inverse hyperbolic cosine of a number

	In Excel: ``ACOSH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACOSH(", *args, ")", **kwargs)

def ACOT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the arccotangent of a number

	In Excel: ``ACOT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACOT(", *args, ")", **kwargs)

def ACOTH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic arccotangent of a number

	In Excel: ``ACOTH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ACOTH(", *args, ")", **kwargs)

def AGGREGATE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns an aggregate in a list or database

	In Excel: ``AGGREGATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AGGREGATE(", *args, ")", **kwargs)

def ADDRESS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns a reference as text to a single cell in a worksheet

	In Excel: ``ADDRESS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ADDRESS(", *args, ")", **kwargs)

def AMORDEGRC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the depreciation for each accounting period by using a depreciation coefficient

	In Excel: ``AMORDEGRC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AMORDEGRC(", *args, ")", **kwargs)

def AMORLINC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the depreciation for each accounting period

	In Excel: ``AMORLINC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AMORLINC(", *args, ")", **kwargs)

def AND(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns TRUE if all of its arguments are TRUE

	In Excel: ``AND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AND(", *args, ")", **kwargs)

def ARABIC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts a Roman number to Arabic, as a number

	In Excel: ``ARABIC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ARABIC(", *args, ")", **kwargs)

def AREAS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the number of areas in a reference

	In Excel: ``AREAS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AREAS(", *args, ")", **kwargs)

def ARRAYTOTEXT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns an array of text values from any specified range

	In Excel: ``ARRAYTOTEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ARRAYTOTEXT(", *args, ")", **kwargs)

def ASC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Changes full-width (double-byte) English letters or katakana within a character string to half-width (single-byte) characters

	In Excel: ``ASC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ASC(", *args, ")", **kwargs)

def ASIN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the arcsine of a number

	In Excel: ``ASIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ASIN(", *args, ")", **kwargs)

def ASINH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the inverse hyperbolic sine of a number

	In Excel: ``ASINH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ASINH(", *args, ")", **kwargs)

def ATAN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the arctangent of a number

	In Excel: ``ATAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ATAN(", *args, ")", **kwargs)

def ATAN2(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the arctangent from x- and y-coordinates

	In Excel: ``ATAN2()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ATAN2(", *args, ")", **kwargs)

def ATANH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the inverse hyperbolic tangent of a number

	In Excel: ``ATANH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ATANH(", *args, ")", **kwargs)

def AVEDEV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the average of the absolute deviations of data points from their mean

	In Excel: ``AVEDEV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AVEDEV(", *args, ")", **kwargs)

def AVERAGE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the average of its arguments

	In Excel: ``AVERAGE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AVERAGE(", *args, ")", **kwargs)

def AVERAGEA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the average of its arguments, including numbers, text, and logical values

	In Excel: ``AVERAGEA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AVERAGEA(", *args, ")", **kwargs)

def AVERAGEIF(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the average (arithmetic mean) of all the cells in a range that meet a given criteria

	In Excel: ``AVERAGEIF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AVERAGEIF(", *args, ")", **kwargs)

def AVERAGEIFS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the average (arithmetic mean) of all cells that meet multiple criteria.

	In Excel: ``AVERAGEIFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("AVERAGEIFS(", *args, ")", **kwargs)

def BAHTTEXT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Converts a number to text, using the ß (baht) currency format

	In Excel: ``BAHTTEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BAHTTEXT(", *args, ")", **kwargs)

def BASE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts a number into a text representation with the given radix (base)

	In Excel: ``BASE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BASE(", *args, ")", **kwargs)

def BESSELI(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the modified Bessel function In(x)

	In Excel: ``BESSELI()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BESSELI(", *args, ")", **kwargs)

def BESSELJ(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the Bessel function Jn(x)

	In Excel: ``BESSELJ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BESSELJ(", *args, ")", **kwargs)

def BESSELK(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the modified Bessel function Kn(x)

	In Excel: ``BESSELK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BESSELK(", *args, ")", **kwargs)

def BESSELY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the Bessel function Yn(x)

	In Excel: ``BESSELY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BESSELY(", *args, ")", **kwargs)

def BETADIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the beta cumulative distribution function

	In Excel: ``BETADIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BETADIST(", *args, ")", **kwargs)

def BETA_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the beta cumulative distribution function

	In Excel: ``BETA.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BETA.DIST(", *args, ")", **kwargs)

def BETAINV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the cumulative distribution function for a specified beta distribution

	In Excel: ``BETAINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BETAINV(", *args, ")", **kwargs)

def BETA_INV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the cumulative distribution function for a specified beta distribution

	In Excel: ``BETA.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BETA.INV(", *args, ")", **kwargs)

def BIN2DEC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a binary number to decimal

	In Excel: ``BIN2DEC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BIN2DEC(", *args, ")", **kwargs)

def BIN2HEX(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a binary number to hexadecimal

	In Excel: ``BIN2HEX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BIN2HEX(", *args, ")", **kwargs)

def BIN2OCT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a binary number to octal

	In Excel: ``BIN2OCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BIN2OCT(", *args, ")", **kwargs)

def BINOMDIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the individual term binomial distribution probability

	In Excel: ``BINOMDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BINOMDIST(", *args, ")", **kwargs)

def BINOM_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the individual term binomial distribution probability

	In Excel: ``BINOM.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BINOM.DIST(", *args, ")", **kwargs)

def BINOM_DIST_RANGE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the probability of a trial result using a binomial distribution

	In Excel: ``BINOM.DIST.RANGE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BINOM.DIST.RANGE(", *args, ")", **kwargs)

def BINOM_INV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the smallest value for which the cumulative binomial distribution is less than or equal to a criterion value

	In Excel: ``BINOM.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BINOM.INV(", *args, ")", **kwargs)

def BITAND(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a 'Bitwise And' of two numbers

	In Excel: ``BITAND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BITAND(", *args, ")", **kwargs)

def BITLSHIFT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a value number shifted left by shift_amount bits

	In Excel: ``BITLSHIFT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BITLSHIFT(", *args, ")", **kwargs)

def BITOR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a bitwise OR of 2 numbers

	In Excel: ``BITOR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BITOR(", *args, ")", **kwargs)

def BITRSHIFT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a value number shifted right by shift_amount bits

	In Excel: ``BITRSHIFT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BITRSHIFT(", *args, ")", **kwargs)

def BITXOR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a bitwise 'Exclusive Or' of two numbers

	In Excel: ``BITXOR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BITXOR(", *args, ")", **kwargs)

def BYCOL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Applies a LAMBDA to each column and returns an array of the results

	In Excel: ``BYCOL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BYCOL(", *args, ")", **kwargs)

def BYROW(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Applies a LAMBDA to each row and returns an array of the results

	In Excel: ``BYROW()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("BYROW(", *args, ")", **kwargs)

def CALL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Add-in and Automation:** Calls a procedure in a dynamic link library or code resource

	In Excel: ``CALL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CALL(", *args, ")", **kwargs)

def CEILING(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Rounds a number to the nearest integer or to the nearest multiple of significance

	In Excel: ``CEILING()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CEILING(", *args, ")", **kwargs)

def CEILING_MATH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number up, to the nearest integer or to the nearest multiple of significance

	In Excel: ``CEILING.MATH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CEILING.MATH(", *args, ")", **kwargs)

def CEILING_PRECISE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number the nearest integer or to the nearest multiple of significance. Regardless of the sign of the number, the number is rounded up.

	In Excel: ``CEILING.PRECISE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CEILING.PRECISE(", *args, ")", **kwargs)

def CELL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns information about the formatting, location, or contents of a cell

	In Excel: ``CELL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CELL(", *args, ")", **kwargs)

def CHAR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the character specified by the code number

	In Excel: ``CHAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHAR(", *args, ")", **kwargs)

def CHIDIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the one-tailed probability of the chi-squared distribution

	In Excel: ``CHIDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHIDIST(", *args, ")", **kwargs)

def CHIINV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the one-tailed probability of the chi-squared distribution

	In Excel: ``CHIINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHIINV(", *args, ")", **kwargs)

def CHITEST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the test for independence

	In Excel: ``CHITEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHITEST(", *args, ")", **kwargs)

def CHISQ_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the cumulative beta probability density function

	In Excel: ``CHISQ.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHISQ.DIST(", *args, ")", **kwargs)

def CHISQ_DIST_RT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the one-tailed probability of the chi-squared distribution

	In Excel: ``CHISQ.DIST.RT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHISQ.DIST.RT(", *args, ")", **kwargs)

def CHISQ_INV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the cumulative beta probability density function

	In Excel: ``CHISQ.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHISQ.INV(", *args, ")", **kwargs)

def CHISQ_INV_RT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the one-tailed probability of the chi-squared distribution

	In Excel: ``CHISQ.INV.RT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHISQ.INV.RT(", *args, ")", **kwargs)

def CHISQ_TEST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the test for independence

	In Excel: ``CHISQ.TEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHISQ.TEST(", *args, ")", **kwargs)

def CHOOSE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Chooses a value from a list of values

	In Excel: ``CHOOSE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHOOSE(", *args, ")", **kwargs)

def CHOOSECOLS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the specified columns from an array

	In Excel: ``CHOOSECOLS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHOOSECOLS(", *args, ")", **kwargs)

def CHOOSEROWS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the specified rows from an array

	In Excel: ``CHOOSEROWS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CHOOSEROWS(", *args, ")", **kwargs)

def CLEAN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Removes all nonprintable characters from text

	In Excel: ``CLEAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CLEAN(", *args, ")", **kwargs)

def CODE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns a numeric code for the first character in a text string

	In Excel: ``CODE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CODE(", *args, ")", **kwargs)

def COLUMN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the column number of a reference

	In Excel: ``COLUMN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COLUMN(", *args, ")", **kwargs)

def COLUMNS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the number of columns in a reference

	In Excel: ``COLUMNS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COLUMNS(", *args, ")", **kwargs)

def COMBIN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the number of combinations for a given number of objects

	In Excel: ``COMBIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COMBIN(", *args, ")", **kwargs)

def COMBINA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts real and imaginary coefficients into a complex number

	In Excel: ``COMBINA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COMBINA(", *args, ")", **kwargs)

def CONCAT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Combines the text from multiple ranges and/or strings, but it doesn't provide the delimiter or IgnoreEmpty arguments.

	In Excel: ``CONCAT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONCAT(", *args, ")", **kwargs)

def CONCATENATE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Joins several text items into one text item

	In Excel: ``CONCATENATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONCATENATE(", *args, ")", **kwargs)

def CONFIDENCE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the confidence interval for a population mean

	In Excel: ``CONFIDENCE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONFIDENCE(", *args, ")", **kwargs)

def CONFIDENCE_NORM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the confidence interval for a population mean

	In Excel: ``CONFIDENCE.NORM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONFIDENCE.NORM(", *args, ")", **kwargs)

def CONFIDENCE_T(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the confidence interval for a population mean, using a Student's t distribution

	In Excel: ``CONFIDENCE.T()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONFIDENCE.T(", *args, ")", **kwargs)

def CONVERT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a number from one measurement system to another

	In Excel: ``CONVERT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CONVERT(", *args, ")", **kwargs)

def CORREL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the correlation coefficient between two data sets

	In Excel: ``CORREL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CORREL(", *args, ")", **kwargs)

def COS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the cosine of a number

	In Excel: ``COS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COS(", *args, ")", **kwargs)

def COSH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic cosine of a number

	In Excel: ``COSH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COSH(", *args, ")", **kwargs)

def COT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic cosine of a number

	In Excel: ``COT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COT(", *args, ")", **kwargs)

def COTH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the cotangent of an angle

	In Excel: ``COTH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COTH(", *args, ")", **kwargs)

def COUNT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Counts how many numbers are in the list of arguments

	In Excel: ``COUNT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUNT(", *args, ")", **kwargs)

def COUNTA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Counts how many values are in the list of arguments

	In Excel: ``COUNTA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUNTA(", *args, ")", **kwargs)

def COUNTBLANK(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Counts the number of blank cells within a range

	In Excel: ``COUNTBLANK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUNTBLANK(", *args, ")", **kwargs)

def COUNTIF(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Counts the number of cells within a range that meet the given criteria

	In Excel: ``COUNTIF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUNTIF(", *args, ")", **kwargs)

def COUNTIFS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Counts the number of cells within a range that meet multiple criteria

	In Excel: ``COUNTIFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUNTIFS(", *args, ")", **kwargs)

def COUPDAYBS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of days from the beginning of the coupon period to the settlement date

	In Excel: ``COUPDAYBS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPDAYBS(", *args, ")", **kwargs)

def COUPDAYS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of days in the coupon period that contains the settlement date

	In Excel: ``COUPDAYS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPDAYS(", *args, ")", **kwargs)

def COUPDAYSNC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of days from the settlement date to the next coupon date

	In Excel: ``COUPDAYSNC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPDAYSNC(", *args, ")", **kwargs)

def COUPNCD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the next coupon date after the settlement date

	In Excel: ``COUPNCD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPNCD(", *args, ")", **kwargs)

def COUPNUM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of coupons payable between the settlement date and maturity date

	In Excel: ``COUPNUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPNUM(", *args, ")", **kwargs)

def COUPPCD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the previous coupon date before the settlement date

	In Excel: ``COUPPCD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COUPPCD(", *args, ")", **kwargs)

def COVAR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns covariance, the average of the products of paired deviations

	In Excel: ``COVAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COVAR(", *args, ")", **kwargs)

def COVARIANCE_P(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns covariance, the average of the products of paired deviations

	In Excel: ``COVARIANCE.P()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COVARIANCE.P(", *args, ")", **kwargs)

def COVARIANCE_S(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the sample covariance, the average of the products deviations for each data point pair in two data sets

	In Excel: ``COVARIANCE.S()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("COVARIANCE.S(", *args, ")", **kwargs)

def CRITBINOM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the smallest value for which the cumulative binomial distribution is less than or equal to a criterion value

	In Excel: ``CRITBINOM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CRITBINOM(", *args, ")", **kwargs)

def CSC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the cosecant of an angle

	In Excel: ``CSC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CSC(", *args, ")", **kwargs)

def CSCH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic cosecant of an angle

	In Excel: ``CSCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CSCH(", *args, ")", **kwargs)

def CUBEKPIMEMBER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns a key performance indicator (KPI) name, property, and measure, and displays the name and property in the cell. A KPI is a quantifiable measurement, such as monthly gross profit or quarterly employee turnover, used to monitor an organization's performance.

	In Excel: ``CUBEKPIMEMBER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBEKPIMEMBER(", *args, ")", **kwargs)

def CUBEMEMBER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns a member or tuple in a cube hierarchy. Use to validate that the member or tuple exists in the cube.

	In Excel: ``CUBEMEMBER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBEMEMBER(", *args, ")", **kwargs)

def CUBEMEMBERPROPERTY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns the value of a member property in the cube. Use to validate that a member name exists within the cube and to return the specified property for this member.

	In Excel: ``CUBEMEMBERPROPERTY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBEMEMBERPROPERTY(", *args, ")", **kwargs)

def CUBERANKEDMEMBER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns the nth, or ranked, member in a set. Use to return one or more elements in a set, such as the top sales performer or top 10 students.

	In Excel: ``CUBERANKEDMEMBER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBERANKEDMEMBER(", *args, ")", **kwargs)

def CUBESET(*args: Any, **kwargs: Any) -> Func:
	"""
	**Cube:** Defines a calculated set of members or tuples by sending a set expression to the cube on the server, which creates the set, and then returns that set to Microsoft Office Excel.

	In Excel: ``CUBESET()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBESET(", *args, ")", **kwargs)

def CUBESETCOUNT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns the number of items in a set.

	In Excel: ``CUBESETCOUNT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBESETCOUNT(", *args, ")", **kwargs)

def CUBEVALUE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Cube:** Returns an aggregated value from a cube.

	In Excel: ``CUBEVALUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUBEVALUE(", *args, ")", **kwargs)

def CUMIPMT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the cumulative interest paid between two periods

	In Excel: ``CUMIPMT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUMIPMT(", *args, ")", **kwargs)

def CUMPRINC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the cumulative principal paid on a loan between two periods

	In Excel: ``CUMPRINC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("CUMPRINC(", *args, ")", **kwargs)

def DATE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of a particular date

	In Excel: ``DATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DATE(", *args, ")", **kwargs)

def DATEDIF(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Calculates the number of days, months, or years between two dates. This function is useful in formulas where you need to calculate an age.

	In Excel: ``DATEDIF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DATEDIF(", *args, ")", **kwargs)

def DATEVALUE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a date in the form of text to a serial number

	In Excel: ``DATEVALUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DATEVALUE(", *args, ")", **kwargs)

def DAVERAGE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Returns the average of selected database entries

	In Excel: ``DAVERAGE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DAVERAGE(", *args, ")", **kwargs)

def DAY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a day of the month

	In Excel: ``DAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DAY(", *args, ")", **kwargs)

def DAYS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the number of days between two dates

	In Excel: ``DAYS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DAYS(", *args, ")", **kwargs)

def DAYS360(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Calculates the number of days between two dates based on a 360-day year

	In Excel: ``DAYS360()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DAYS360(", *args, ")", **kwargs)

def DB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the depreciation of an asset for a specified period by using the fixed-declining balance method

	In Excel: ``DB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DB(", *args, ")", **kwargs)

def DBCS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Changes half-width (single-byte) English letters or katakana within a character string to full-width (double-byte) characters

	In Excel: ``DBCS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DBCS(", *args, ")", **kwargs)

def DCOUNT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Counts the cells that contain numbers in a database

	In Excel: ``DCOUNT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DCOUNT(", *args, ")", **kwargs)

def DCOUNTA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Counts nonblank cells in a database

	In Excel: ``DCOUNTA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DCOUNTA(", *args, ")", **kwargs)

def DDB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the depreciation of an asset for a specified period by using the double-declining balance method or some other method that you specify

	In Excel: ``DDB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DDB(", *args, ")", **kwargs)

def DEC2BIN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a decimal number to binary

	In Excel: ``DEC2BIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DEC2BIN(", *args, ")", **kwargs)

def DEC2HEX(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a decimal number to hexadecimal

	In Excel: ``DEC2HEX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DEC2HEX(", *args, ")", **kwargs)

def DEC2OCT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a decimal number to octal

	In Excel: ``DEC2OCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DEC2OCT(", *args, ")", **kwargs)

def DECIMAL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts a text representation of a number in a given base into a decimal number

	In Excel: ``DECIMAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DECIMAL(", *args, ")", **kwargs)

def DEGREES(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts radians to degrees

	In Excel: ``DEGREES()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DEGREES(", *args, ")", **kwargs)

def DELTA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Tests whether two values are equal

	In Excel: ``DELTA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DELTA(", *args, ")", **kwargs)

def DEVSQ(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the sum of squares of deviations

	In Excel: ``DEVSQ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DEVSQ(", *args, ")", **kwargs)

def DGET(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Extracts from a database a single record that matches the specified criteria

	In Excel: ``DGET()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DGET(", *args, ")", **kwargs)

def DISC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the discount rate for a security

	In Excel: ``DISC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DISC(", *args, ")", **kwargs)

def DMAX(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Returns the maximum value from selected database entries

	In Excel: ``DMAX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DMAX(", *args, ")", **kwargs)

def DMIN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Returns the minimum value from selected database entries

	In Excel: ``DMIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DMIN(", *args, ")", **kwargs)

def DOLLAR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Converts a number to text, using the $ (dollar) currency format

	In Excel: ``DOLLAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DOLLAR(", *args, ")", **kwargs)

def DOLLARDE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Converts a dollar price, expressed as a fraction, into a dollar price, expressed as a decimal number

	In Excel: ``DOLLARDE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DOLLARDE(", *args, ")", **kwargs)

def DOLLARFR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Converts a dollar price, expressed as a decimal number, into a dollar price, expressed as a fraction

	In Excel: ``DOLLARFR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DOLLARFR(", *args, ")", **kwargs)

def DPRODUCT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Multiplies the values in a particular field of records that match the criteria in a database

	In Excel: ``DPRODUCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DPRODUCT(", *args, ")", **kwargs)

def DROP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Excludes a specified number of rows or columns from the start or end of an array

	In Excel: ``DROP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DROP(", *args, ")", **kwargs)

def DSTDEV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Estimates the standard deviation based on a sample of selected database entries

	In Excel: ``DSTDEV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DSTDEV(", *args, ")", **kwargs)

def DSTDEVP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Calculates the standard deviation based on the entire population of selected database entries

	In Excel: ``DSTDEVP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DSTDEVP(", *args, ")", **kwargs)

def DSUM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Adds the numbers in the field column of records in the database that match the criteria

	In Excel: ``DSUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DSUM(", *args, ")", **kwargs)

def DURATION(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the annual duration of a security with periodic interest payments

	In Excel: ``DURATION()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DURATION(", *args, ")", **kwargs)

def DVAR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Estimates variance based on a sample from selected database entries

	In Excel: ``DVAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DVAR(", *args, ")", **kwargs)

def DVARP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Database:** Calculates variance based on the entire population of selected database entries

	In Excel: ``DVARP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("DVARP(", *args, ")", **kwargs)

def EDATE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of the date that is the indicated number of months before or after the start date

	In Excel: ``EDATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EDATE(", *args, ")", **kwargs)

def EFFECT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the effective annual interest rate

	In Excel: ``EFFECT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EFFECT(", *args, ")", **kwargs)

def ENCODEURL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Web:** Returns a URL-encoded string

	In Excel: ``ENCODEURL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ENCODEURL(", *args, ")", **kwargs)

def EOMONTH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of the last day of the month before or after a specified number of months

	In Excel: ``EOMONTH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EOMONTH(", *args, ")", **kwargs)

def ERF(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the error function

	In Excel: ``ERF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ERF(", *args, ")", **kwargs)

def ERF_PRECISE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the error function

	In Excel: ``ERF.PRECISE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ERF.PRECISE(", *args, ")", **kwargs)

def ERFC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the complementary error function

	In Excel: ``ERFC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ERFC(", *args, ")", **kwargs)

def ERFC_PRECISE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the complementary ERF function integrated between x and infinity

	In Excel: ``ERFC.PRECISE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ERFC.PRECISE(", *args, ")", **kwargs)

def ERROR_TYPE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns a number corresponding to an error type

	In Excel: ``ERROR.TYPE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ERROR.TYPE(", *args, ")", **kwargs)

def EUROCONVERT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Add-in and Automation:** Converts a number to euros, converts a number from euros to a euro member currency, or converts a number from one euro member currency to another by using the euro as an intermediary (triangulation).

	In Excel: ``EUROCONVERT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EUROCONVERT(", *args, ")", **kwargs)

def EVEN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number up to the nearest even integer

	In Excel: ``EVEN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EVEN(", *args, ")", **kwargs)

def EXACT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Checks to see if two text values are identical

	In Excel: ``EXACT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EXACT(", *args, ")", **kwargs)

def EXP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns <i class="ocpItalic">e</i> raised to the power of a given number

	In Excel: ``EXP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EXP(", *args, ")", **kwargs)

def EXPAND(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Expands or pads an array to specified row and column dimensions

	In Excel: ``EXPAND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EXPAND(", *args, ")", **kwargs)

def EXPON_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the exponential distribution

	In Excel: ``EXPON.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EXPON.DIST(", *args, ")", **kwargs)

def EXPONDIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the exponential distribution

	In Excel: ``EXPONDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("EXPONDIST(", *args, ")", **kwargs)

def FACT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the factorial of a number

	In Excel: ``FACT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FACT(", *args, ")", **kwargs)

def FACTDOUBLE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the double factorial of a number

	In Excel: ``FACTDOUBLE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FACTDOUBLE(", *args, ")", **kwargs)

def FALSE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns the logical value FALSE

	In Excel: ``FALSE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FALSE(", *args, ")", **kwargs)

def F_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the F probability distribution

	In Excel: ``F.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("F.DIST(", *args, ")", **kwargs)

def FDIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the F probability distribution

	In Excel: ``FDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FDIST(", *args, ")", **kwargs)

def F_DIST_RT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the F probability distribution

	In Excel: ``F.DIST.RT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("F.DIST.RT(", *args, ")", **kwargs)

def FILTER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Filters a range of data based on criteria you define

	In Excel: ``FILTER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FILTER(", *args, ")", **kwargs)

def FILTERXML(*args: Any, **kwargs: Any) -> Func:
	"""
	**Web:** Returns specific data from the XML content by using the specified XPath

	In Excel: ``FILTERXML()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FILTERXML(", *args, ")", **kwargs)

def FIND(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Finds one text value within another (case-sensitive)

	In Excel: ``FIND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FIND(", *args, ")", **kwargs)

def FINDB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Finds one text value within another (case-sensitive)

	In Excel: ``FINDB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FINDB(", *args, ")", **kwargs)

def F_INV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the F probability distribution

	In Excel: ``F.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("F.INV(", *args, ")", **kwargs)

def F_INV_RT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the F probability distribution

	In Excel: ``F.INV.RT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("F.INV.RT(", *args, ")", **kwargs)

def FINV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the F probability distribution

	In Excel: ``FINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FINV(", *args, ")", **kwargs)

def FISHER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Fisher transformation

	In Excel: ``FISHER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FISHER(", *args, ")", **kwargs)

def FISHERINV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the Fisher transformation

	In Excel: ``FISHERINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FISHERINV(", *args, ")", **kwargs)

def FIXED(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Formats a number as text with a fixed number of decimals

	In Excel: ``FIXED()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FIXED(", *args, ")", **kwargs)

def FLOOR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Rounds a number down, toward zero

	In Excel: ``FLOOR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FLOOR(", *args, ")", **kwargs)

def FLOOR_MATH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number down, to the nearest integer or to the nearest multiple of significance

	In Excel: ``FLOOR.MATH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FLOOR.MATH(", *args, ")", **kwargs)

def FLOOR_PRECISE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number the nearest integer or to the nearest multiple of significance. Regardless of the sign of the number, the number is rounded up.

	In Excel: ``FLOOR.PRECISE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FLOOR.PRECISE(", *args, ")", **kwargs)

def FORECAST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns a value along a linear trend

	In Excel: ``FORECAST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FORECAST(", *args, ")", **kwargs)

def FORMULATEXT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the formula at the given reference as text

	In Excel: ``FORMULATEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FORMULATEXT(", *args, ")", **kwargs)

def FREQUENCY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns a frequency distribution as a vertical array

	In Excel: ``FREQUENCY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FREQUENCY(", *args, ")", **kwargs)

def F_TEST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the result of an F-test

	In Excel: ``F.TEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("F.TEST(", *args, ")", **kwargs)

def FTEST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the result of an F-test

	In Excel: ``FTEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FTEST(", *args, ")", **kwargs)

def FV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the future value of an investment

	In Excel: ``FV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FV(", *args, ")", **kwargs)

def FVSCHEDULE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the future value of an initial principal after applying a series of compound interest rates

	In Excel: ``FVSCHEDULE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("FVSCHEDULE(", *args, ")", **kwargs)

def GAMMA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Gamma function value

	In Excel: ``GAMMA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMA(", *args, ")", **kwargs)

def GAMMA_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the gamma distribution

	In Excel: ``GAMMA.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMA.DIST(", *args, ")", **kwargs)

def GAMMADIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the gamma distribution

	In Excel: ``GAMMADIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMADIST(", *args, ")", **kwargs)

def GAMMA_INV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the gamma cumulative distribution

	In Excel: ``GAMMA.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMA.INV(", *args, ")", **kwargs)

def GAMMAINV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the gamma cumulative distribution

	In Excel: ``GAMMAINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMAINV(", *args, ")", **kwargs)

def GAMMALN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the natural logarithm of the gamma function, Γ(x)

	In Excel: ``GAMMALN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMALN(", *args, ")", **kwargs)

def GAMMALN_PRECISE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the natural logarithm of the gamma function, Γ(x)

	In Excel: ``GAMMALN.PRECISE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAMMALN.PRECISE(", *args, ")", **kwargs)

def GAUSS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns 0.5 less than the standard normal cumulative distribution

	In Excel: ``GAUSS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GAUSS(", *args, ")", **kwargs)

def GCD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the greatest common divisor

	In Excel: ``GCD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GCD(", *args, ")", **kwargs)

def GEOMEAN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the geometric mean

	In Excel: ``GEOMEAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GEOMEAN(", *args, ")", **kwargs)

def GESTEP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Tests whether a number is greater than a threshold value

	In Excel: ``GESTEP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GESTEP(", *args, ")", **kwargs)

def GETPIVOTDATA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns data stored in a PivotTable report

	In Excel: ``GETPIVOTDATA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GETPIVOTDATA(", *args, ")", **kwargs)

def GROWTH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns values along an exponential trend

	In Excel: ``GROWTH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("GROWTH(", *args, ")", **kwargs)

def HARMEAN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the harmonic mean

	In Excel: ``HARMEAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HARMEAN(", *args, ")", **kwargs)

def HEX2BIN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a hexadecimal number to binary

	In Excel: ``HEX2BIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HEX2BIN(", *args, ")", **kwargs)

def HEX2DEC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a hexadecimal number to decimal

	In Excel: ``HEX2DEC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HEX2DEC(", *args, ")", **kwargs)

def HEX2OCT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts a hexadecimal number to octal

	In Excel: ``HEX2OCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HEX2OCT(", *args, ")", **kwargs)

def HLOOKUP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Looks in the top row of an array and returns the value of the indicated cell

	In Excel: ``HLOOKUP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HLOOKUP(", *args, ")", **kwargs)

def HOUR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to an hour

	In Excel: ``HOUR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HOUR(", *args, ")", **kwargs)

def HSTACK(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Appends arrays horizontally and in sequence to return a larger array

	In Excel: ``HSTACK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HSTACK(", *args, ")", **kwargs)

def HYPERLINK(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Creates a shortcut or jump that opens a document stored on a network server, an intranet, or the Internet

	In Excel: ``HYPERLINK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HYPERLINK(", *args, ")", **kwargs)

def HYPGEOM_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the hypergeometric distribution

	In Excel: ``HYPGEOM.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HYPGEOM.DIST(", *args, ")", **kwargs)

def HYPGEOMDIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the hypergeometric distribution

	In Excel: ``HYPGEOMDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("HYPGEOMDIST(", *args, ")", **kwargs)

def IF(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Specifies a logical test to perform

	In Excel: ``IF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IF(", *args, ")", **kwargs)

def IFERROR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns a value you specify if a formula evaluates to an error; otherwise, returns the result of the formula

	In Excel: ``IFERROR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IFERROR(", *args, ")", **kwargs)

def IFNA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns the value you specify if the expression resolves to #N/A, otherwise returns the result of the expression

	In Excel: ``IFNA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IFNA(", *args, ")", **kwargs)

def IFS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Checks whether one or more conditions are met and returns a value that corresponds to the first TRUE condition.

	In Excel: ``IFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IFS(", *args, ")", **kwargs)

def IMABS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the absolute value (modulus) of a complex number

	In Excel: ``IMABS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMABS(", *args, ")", **kwargs)

def IMAGINARY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the imaginary coefficient of a complex number

	In Excel: ``IMAGINARY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMAGINARY(", *args, ")", **kwargs)

def IMARGUMENT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the argument theta, an angle expressed in radians

	In Excel: ``IMARGUMENT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMARGUMENT(", *args, ")", **kwargs)

def IMCONJUGATE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the complex conjugate of a complex number

	In Excel: ``IMCONJUGATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCONJUGATE(", *args, ")", **kwargs)

def IMCOS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the cosine of a complex number

	In Excel: ``IMCOS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCOS(", *args, ")", **kwargs)

def IMCOSH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the hyperbolic cosine of a complex number

	In Excel: ``IMCOSH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCOSH(", *args, ")", **kwargs)

def IMCOT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the cotangent of a complex number

	In Excel: ``IMCOT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCOT(", *args, ")", **kwargs)

def IMCSC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the cosecant of a complex number

	In Excel: ``IMCSC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCSC(", *args, ")", **kwargs)

def IMCSCH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the hyperbolic cosecant of a complex number

	In Excel: ``IMCSCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMCSCH(", *args, ")", **kwargs)

def IMDIV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the quotient of two complex numbers

	In Excel: ``IMDIV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMDIV(", *args, ")", **kwargs)

def IMEXP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the exponential of a complex number

	In Excel: ``IMEXP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMEXP(", *args, ")", **kwargs)

def IMLN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the natural logarithm of a complex number

	In Excel: ``IMLN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMLN(", *args, ")", **kwargs)

def IMLOG10(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the base-10 logarithm of a complex number

	In Excel: ``IMLOG10()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMLOG10(", *args, ")", **kwargs)

def IMLOG2(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the base-2 logarithm of a complex number

	In Excel: ``IMLOG2()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMLOG2(", *args, ")", **kwargs)

def IMPOWER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns a complex number raised to an integer power

	In Excel: ``IMPOWER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMPOWER(", *args, ")", **kwargs)

def IMPRODUCT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the product of complex numbers

	In Excel: ``IMPRODUCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMPRODUCT(", *args, ")", **kwargs)

def IMREAL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the real coefficient of a complex number

	In Excel: ``IMREAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMREAL(", *args, ")", **kwargs)

def IMSEC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the secant of a complex number

	In Excel: ``IMSEC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSEC(", *args, ")", **kwargs)

def IMSECH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the hyperbolic secant of a complex number

	In Excel: ``IMSECH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSECH(", *args, ")", **kwargs)

def IMSIN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the sine of a complex number

	In Excel: ``IMSIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSIN(", *args, ")", **kwargs)

def IMSINH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the hyperbolic sine of a complex number

	In Excel: ``IMSINH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSINH(", *args, ")", **kwargs)

def IMSQRT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the square root of a complex number

	In Excel: ``IMSQRT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSQRT(", *args, ")", **kwargs)

def IMSUB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the difference between two complex numbers

	In Excel: ``IMSUB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSUB(", *args, ")", **kwargs)

def IMSUM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the sum of complex numbers

	In Excel: ``IMSUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMSUM(", *args, ")", **kwargs)

def IMTAN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Returns the tangent of a complex number

	In Excel: ``IMTAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IMTAN(", *args, ")", **kwargs)

def INDEX(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Uses an index to choose a value from a reference or array

	In Excel: ``INDEX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INDEX(", *args, ")", **kwargs)

def INDIRECT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns a reference indicated by a text value

	In Excel: ``INDIRECT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INDIRECT(", *args, ")", **kwargs)

def INFO(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns information about the current operating environment

	In Excel: ``INFO()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INFO(", *args, ")", **kwargs)

def INT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number down to the nearest integer

	In Excel: ``INT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INT(", *args, ")", **kwargs)

def INTERCEPT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the intercept of the linear regression line

	In Excel: ``INTERCEPT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INTERCEPT(", *args, ")", **kwargs)

def INTRATE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the interest rate for a fully invested security

	In Excel: ``INTRATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("INTRATE(", *args, ")", **kwargs)

def IPMT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the interest payment for an investment for a given period

	In Excel: ``IPMT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IPMT(", *args, ")", **kwargs)

def IRR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the internal rate of return for a series of cash flows

	In Excel: ``IRR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("IRR(", *args, ")", **kwargs)

def ISBLANK(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is blank

	In Excel: ``ISBLANK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISBLANK(", *args, ")", **kwargs)

def ISERR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is any error value except #N/A

	In Excel: ``ISERR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISERR(", *args, ")", **kwargs)

def ISERROR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is any error value

	In Excel: ``ISERROR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISERROR(", *args, ")", **kwargs)

def ISEVEN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the number is even

	In Excel: ``ISEVEN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISEVEN(", *args, ")", **kwargs)

def ISFORMULA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if there is a reference to a cell that contains a formula

	In Excel: ``ISFORMULA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISFORMULA(", *args, ")", **kwargs)

def ISLOGICAL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is a logical value

	In Excel: ``ISLOGICAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISLOGICAL(", *args, ")", **kwargs)

def ISNA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is the #N/A error value

	In Excel: ``ISNA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISNA(", *args, ")", **kwargs)

def ISNONTEXT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is not text

	In Excel: ``ISNONTEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISNONTEXT(", *args, ")", **kwargs)

def ISNUMBER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is a number

	In Excel: ``ISNUMBER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISNUMBER(", *args, ")", **kwargs)

def ISODD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the number is odd

	In Excel: ``ISODD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISODD(", *args, ")", **kwargs)

def ISOMITTED(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Checks whether the value in a LAMBDA is missing and returns TRUE or FALSE

	In Excel: ``ISOMITTED()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISOMITTED(", *args, ")", **kwargs)

def ISREF(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is a reference

	In Excel: ``ISREF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISREF(", *args, ")", **kwargs)

def ISTEXT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns TRUE if the value is text

	In Excel: ``ISTEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISTEXT(", *args, ")", **kwargs)

def ISO_CEILING(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a number that is rounded up to the nearest integer or to the nearest multiple of significance

	In Excel: ``ISO.CEILING()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISO.CEILING(", *args, ")", **kwargs)

def ISOWEEKNUM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the number of the ISO week number of the year for a given date

	In Excel: ``ISOWEEKNUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISOWEEKNUM(", *args, ")", **kwargs)

def ISPMT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Calculates the interest paid during a specific period of an investment

	In Excel: ``ISPMT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ISPMT(", *args, ")", **kwargs)

def JIS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Changes half-width (single-byte) characters within a string to full-width (double-byte) characters

	In Excel: ``JIS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("JIS(", *args, ")", **kwargs)

def KURT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the kurtosis of a data set

	In Excel: ``KURT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("KURT(", *args, ")", **kwargs)

def LAMBDA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Create custom, reusable functions and call them by a friendly name

	In Excel: ``LAMBDA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LAMBDA(", *args, ")", **kwargs)

def LARGE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the k-th largest value in a data set

	In Excel: ``LARGE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LARGE(", *args, ")", **kwargs)

def LCM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the least common multiple

	In Excel: ``LCM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LCM(", *args, ")", **kwargs)

def LEFT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the leftmost characters from a text value

	In Excel: ``LEFT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LEFT(", *args, ")", **kwargs)

def LEFTB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the leftmost characters from a text value

	In Excel: ``LEFTB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LEFTB(", *args, ")", **kwargs)

def LEN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the number of characters in a text string

	In Excel: ``LEN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LEN(", *args, ")", **kwargs)

def LENB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the number of characters in a text string

	In Excel: ``LENB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LENB(", *args, ")", **kwargs)

def LET(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Assigns names to calculation results

	In Excel: ``LET()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LET(", *args, ")", **kwargs)

def LINEST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the parameters of a linear trend

	In Excel: ``LINEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LINEST(", *args, ")", **kwargs)

def LN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the natural logarithm of a number

	In Excel: ``LN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LN(", *args, ")", **kwargs)

def LOG(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the logarithm of a number to a specified base

	In Excel: ``LOG()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOG(", *args, ")", **kwargs)

def LOG10(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the base-10 logarithm of a number

	In Excel: ``LOG10()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOG10(", *args, ")", **kwargs)

def LOGEST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the parameters of an exponential trend

	In Excel: ``LOGEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOGEST(", *args, ")", **kwargs)

def LOGINV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the lognormal cumulative distribution

	In Excel: ``LOGINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOGINV(", *args, ")", **kwargs)

def LOGNORM_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the cumulative lognormal distribution

	In Excel: ``LOGNORM.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOGNORM.DIST(", *args, ")", **kwargs)

def LOGNORMDIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the cumulative lognormal distribution

	In Excel: ``LOGNORMDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOGNORMDIST(", *args, ")", **kwargs)

def LOGNORM_INV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the lognormal cumulative distribution

	In Excel: ``LOGNORM.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOGNORM.INV(", *args, ")", **kwargs)

def LOOKUP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Looks up values in a vector or array

	In Excel: ``LOOKUP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOOKUP(", *args, ")", **kwargs)

def LOWER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Converts text to lowercase

	In Excel: ``LOWER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("LOWER(", *args, ")", **kwargs)

def MAKEARRAY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns a calculated array of a specified row and column size, by applying a LAMBDA

	In Excel: ``MAKEARRAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MAKEARRAY(", *args, ")", **kwargs)

def MAP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns an array formed by mapping each value in the array(s) to a new value by applying a LAMBDA to create a new value

	In Excel: ``MAP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MAP(", *args, ")", **kwargs)

def MATCH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Looks up values in a reference or array

	In Excel: ``MATCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MATCH(", *args, ")", **kwargs)

def MAX(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the maximum value in a list of arguments

	In Excel: ``MAX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MAX(", *args, ")", **kwargs)

def MAXA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the maximum value in a list of arguments, including numbers, text, and logical values

	In Excel: ``MAXA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MAXA(", *args, ")", **kwargs)

def MAXIFS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the maximum value among cells specified by a given set of conditions or criteria

	In Excel: ``MAXIFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MAXIFS(", *args, ")", **kwargs)

def MDETERM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the matrix determinant of an array

	In Excel: ``MDETERM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MDETERM(", *args, ")", **kwargs)

def MDURATION(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the Macauley modified duration for a security with an assumed par value of $100

	In Excel: ``MDURATION()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MDURATION(", *args, ")", **kwargs)

def MEDIAN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the median of the given numbers

	In Excel: ``MEDIAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MEDIAN(", *args, ")", **kwargs)

def MID(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns a specific number of characters from a text string starting at the position you specify

	In Excel: ``MID()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MID(", *args, ")", **kwargs)

def MIDB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns a specific number of characters from a text string starting at the position you specify

	In Excel: ``MIDB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MIDB(", *args, ")", **kwargs)

def MIN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the minimum value in a list of arguments

	In Excel: ``MIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MIN(", *args, ")", **kwargs)

def MINIFS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the minimum value among cells specified by a given set of conditions or criteria.

	In Excel: ``MINIFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MINIFS(", *args, ")", **kwargs)

def MINA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the smallest value in a list of arguments, including numbers, text, and logical values

	In Excel: ``MINA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MINA(", *args, ")", **kwargs)

def MINUTE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a minute

	In Excel: ``MINUTE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MINUTE(", *args, ")", **kwargs)

def MINVERSE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the matrix inverse of an array

	In Excel: ``MINVERSE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MINVERSE(", *args, ")", **kwargs)

def MIRR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the internal rate of return where positive and negative cash flows are financed at different rates

	In Excel: ``MIRR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MIRR(", *args, ")", **kwargs)

def MMULT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the matrix product of two arrays

	In Excel: ``MMULT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MMULT(", *args, ")", **kwargs)

def MOD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the remainder from division

	In Excel: ``MOD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MOD(", *args, ")", **kwargs)

def MODE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the most common value in a data set

	In Excel: ``MODE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MODE(", *args, ")", **kwargs)

def MODE_MULT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns a vertical array of the most frequently occurring, or repetitive values in an array or range of data

	In Excel: ``MODE.MULT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MODE.MULT(", *args, ")", **kwargs)

def MODE_SNGL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the most common value in a data set

	In Excel: ``MODE.SNGL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MODE.SNGL(", *args, ")", **kwargs)

def MONTH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a month

	In Excel: ``MONTH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MONTH(", *args, ")", **kwargs)

def MROUND(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a number rounded to the desired multiple

	In Excel: ``MROUND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MROUND(", *args, ")", **kwargs)

def MULTINOMIAL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the multinomial of a set of numbers

	In Excel: ``MULTINOMIAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MULTINOMIAL(", *args, ")", **kwargs)

def MUNIT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the unit matrix or the specified dimension

	In Excel: ``MUNIT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("MUNIT(", *args, ")", **kwargs)

def N(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns a value converted to a number

	In Excel: ``N()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("N(", *args, ")", **kwargs)

def NA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns the error value #N/A

	In Excel: ``NA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NA(", *args, ")", **kwargs)

def NEGBINOM_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the negative binomial distribution

	In Excel: ``NEGBINOM.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NEGBINOM.DIST(", *args, ")", **kwargs)

def NEGBINOMDIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the negative binomial distribution

	In Excel: ``NEGBINOMDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NEGBINOMDIST(", *args, ")", **kwargs)

def NETWORKDAYS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the number of whole workdays between two dates

	In Excel: ``NETWORKDAYS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NETWORKDAYS(", *args, ")", **kwargs)

def NETWORKDAYS_INTL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the number of whole workdays between two dates using parameters to indicate which and how many days are weekend days

	In Excel: ``NETWORKDAYS.INTL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NETWORKDAYS.INTL(", *args, ")", **kwargs)

def NOMINAL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the annual nominal interest rate

	In Excel: ``NOMINAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NOMINAL(", *args, ")", **kwargs)

def NORM_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the normal cumulative distribution

	In Excel: ``NORM.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORM.DIST(", *args, ")", **kwargs)

def NORMDIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the normal cumulative distribution

	In Excel: ``NORMDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORMDIST(", *args, ")", **kwargs)

def NORMINV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the normal cumulative distribution

	In Excel: ``NORMINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORMINV(", *args, ")", **kwargs)

def NORM_INV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the normal cumulative distribution

	In Excel: ``NORM.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORM.INV(", *args, ")", **kwargs)

def NORM_S_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the standard normal cumulative distribution

	In Excel: ``NORM.S.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORM.S.DIST(", *args, ")", **kwargs)

def NORMSDIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the standard normal cumulative distribution

	In Excel: ``NORMSDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORMSDIST(", *args, ")", **kwargs)

def NORM_S_INV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the standard normal cumulative distribution

	In Excel: ``NORM.S.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORM.S.INV(", *args, ")", **kwargs)

def NORMSINV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the standard normal cumulative distribution

	In Excel: ``NORMSINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NORMSINV(", *args, ")", **kwargs)

def NOT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Reverses the logic of its argument

	In Excel: ``NOT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NOT(", *args, ")", **kwargs)

def NOW(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of the current date and time

	In Excel: ``NOW()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NOW(", *args, ")", **kwargs)

def NPER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of periods for an investment

	In Excel: ``NPER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NPER(", *args, ")", **kwargs)

def NPV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the net present value of an investment based on a series of periodic cash flows and a discount rate

	In Excel: ``NPV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NPV(", *args, ")", **kwargs)

def NUMBERVALUE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Converts text to number in a locale-independent manner

	In Excel: ``NUMBERVALUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("NUMBERVALUE(", *args, ")", **kwargs)

def OCT2BIN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts an octal number to binary

	In Excel: ``OCT2BIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("OCT2BIN(", *args, ")", **kwargs)

def OCT2DEC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts an octal number to decimal

	In Excel: ``OCT2DEC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("OCT2DEC(", *args, ")", **kwargs)

def OCT2HEX(*args: Any, **kwargs: Any) -> Func:
	"""
	**Engineering:** Converts an octal number to hexadecimal

	In Excel: ``OCT2HEX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("OCT2HEX(", *args, ")", **kwargs)

def ODD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number up to the nearest odd integer

	In Excel: ``ODD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ODD(", *args, ")", **kwargs)

def ODDFPRICE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value of a security with an odd first period

	In Excel: ``ODDFPRICE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ODDFPRICE(", *args, ")", **kwargs)

def ODDFYIELD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the yield of a security with an odd first period

	In Excel: ``ODDFYIELD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ODDFYIELD(", *args, ")", **kwargs)

def ODDLPRICE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value of a security with an odd last period

	In Excel: ``ODDLPRICE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ODDLPRICE(", *args, ")", **kwargs)

def ODDLYIELD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the yield of a security with an odd last period

	In Excel: ``ODDLYIELD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ODDLYIELD(", *args, ")", **kwargs)

def OFFSET(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns a reference offset from a given reference

	In Excel: ``OFFSET()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("OFFSET(", *args, ")", **kwargs)

def OR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns TRUE if any argument is TRUE

	In Excel: ``OR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("OR(", *args, ")", **kwargs)

def PDURATION(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the number of periods required by an investment to reach a specified value

	In Excel: ``PDURATION()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PDURATION(", *args, ")", **kwargs)

def PEARSON(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Pearson product moment correlation coefficient

	In Excel: ``PEARSON()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PEARSON(", *args, ")", **kwargs)

def PERCENTILE_EXC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the k-th percentile of values in a range, where k is in the range 0..1, exclusive

	In Excel: ``PERCENTILE.EXC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTILE.EXC(", *args, ")", **kwargs)

def PERCENTILE_INC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the k-th percentile of values in a range

	In Excel: ``PERCENTILE.INC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTILE.INC(", *args, ")", **kwargs)

def PERCENTILE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the k-th percentile of values in a range

	In Excel: ``PERCENTILE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTILE(", *args, ")", **kwargs)

def PERCENTRANK_EXC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the rank of a value in a data set as a percentage (0..1, exclusive) of the data set

	In Excel: ``PERCENTRANK.EXC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTRANK.EXC(", *args, ")", **kwargs)

def PERCENTRANK_INC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the percentage rank of a value in a data set

	In Excel: ``PERCENTRANK.INC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTRANK.INC(", *args, ")", **kwargs)

def PERCENTRANK(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the percentage rank of a value in a data set

	In Excel: ``PERCENTRANK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERCENTRANK(", *args, ")", **kwargs)

def PERMUT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the number of permutations for a given number of objects

	In Excel: ``PERMUT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERMUT(", *args, ")", **kwargs)

def PERMUTATIONA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the number of permutations for a given number of objects (with repetitions) that can be selected from the total objects

	In Excel: ``PERMUTATIONA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PERMUTATIONA(", *args, ")", **kwargs)

def PHI(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the value of the density function for a standard normal distribution

	In Excel: ``PHI()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PHI(", *args, ")", **kwargs)

def PHONETIC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Extracts the phonetic (furigana) characters from a text string

	In Excel: ``PHONETIC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PHONETIC(", *args, ")", **kwargs)

def PI(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the value of pi

	In Excel: ``PI()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PI(", *args, ")", **kwargs)

def PMT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the periodic payment for an annuity

	In Excel: ``PMT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PMT(", *args, ")", **kwargs)

def POISSON_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Poisson distribution

	In Excel: ``POISSON.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("POISSON.DIST(", *args, ")", **kwargs)

def POISSON(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the Poisson distribution

	In Excel: ``POISSON()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("POISSON(", *args, ")", **kwargs)

def POWER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the result of a number raised to a power

	In Excel: ``POWER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("POWER(", *args, ")", **kwargs)

def PPMT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the payment on the principal for an investment for a given period

	In Excel: ``PPMT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PPMT(", *args, ")", **kwargs)

def PRICE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value of a security that pays periodic interest

	In Excel: ``PRICE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PRICE(", *args, ")", **kwargs)

def PRICEDISC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value of a discounted security

	In Excel: ``PRICEDISC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PRICEDISC(", *args, ")", **kwargs)

def PRICEMAT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value of a security that pays interest at maturity

	In Excel: ``PRICEMAT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PRICEMAT(", *args, ")", **kwargs)

def PROB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the probability that values in a range are between two limits

	In Excel: ``PROB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PROB(", *args, ")", **kwargs)

def PRODUCT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Multiplies its arguments

	In Excel: ``PRODUCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PRODUCT(", *args, ")", **kwargs)

def PROPER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Capitalizes the first letter in each word of a text value

	In Excel: ``PROPER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PROPER(", *args, ")", **kwargs)

def PV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the present value of an investment

	In Excel: ``PV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("PV(", *args, ")", **kwargs)

def QUARTILE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the quartile of a data set

	In Excel: ``QUARTILE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("QUARTILE(", *args, ")", **kwargs)

def QUARTILE_EXC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the quartile of the data set, based on percentile values from 0..1, exclusive

	In Excel: ``QUARTILE.EXC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("QUARTILE.EXC(", *args, ")", **kwargs)

def QUARTILE_INC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the quartile of a data set

	In Excel: ``QUARTILE.INC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("QUARTILE.INC(", *args, ")", **kwargs)

def QUOTIENT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the integer portion of a division

	In Excel: ``QUOTIENT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("QUOTIENT(", *args, ")", **kwargs)

def RADIANS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts degrees to radians

	In Excel: ``RADIANS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RADIANS(", *args, ")", **kwargs)

def RAND(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a random number between 0 and 1

	In Excel: ``RAND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RAND(", *args, ")", **kwargs)

def RANDARRAY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns an array of random numbers between 0 and 1. However, you can specify the number of rows and columns to fill, minimum and maximum values, and whether to return whole numbers or decimal values.

	In Excel: ``RANDARRAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RANDARRAY(", *args, ")", **kwargs)

def RANDBETWEEN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a random number between the numbers you specify

	In Excel: ``RANDBETWEEN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RANDBETWEEN(", *args, ")", **kwargs)

def RANK_AVG(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the rank of a number in a list of numbers

	In Excel: ``RANK.AVG()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RANK.AVG(", *args, ")", **kwargs)

def RANK_EQ(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the rank of a number in a list of numbers

	In Excel: ``RANK.EQ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RANK.EQ(", *args, ")", **kwargs)

def RANK(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the rank of a number in a list of numbers

	In Excel: ``RANK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RANK(", *args, ")", **kwargs)

def RATE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the interest rate per period of an annuity

	In Excel: ``RATE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RATE(", *args, ")", **kwargs)

def RECEIVED(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the amount received at maturity for a fully invested security

	In Excel: ``RECEIVED()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RECEIVED(", *args, ")", **kwargs)

def REDUCE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Reduces an array to an accumulated value by applying a LAMBDA to each value and returning the total value in the accumulator

	In Excel: ``REDUCE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("REDUCE(", *args, ")", **kwargs)

def REGISTER_ID(*args: Any, **kwargs: Any) -> Func:
	"""
	**Add-in and Automation:** Returns the register ID of the specified dynamic link library (DLL) or code resource that has been previously registered

	In Excel: ``REGISTER.ID()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("REGISTER.ID(", *args, ")", **kwargs)

def REPLACE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Replaces characters within text

	In Excel: ``REPLACE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("REPLACE(", *args, ")", **kwargs)

def REPLACEB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Replaces characters within text

	In Excel: ``REPLACEB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("REPLACEB(", *args, ")", **kwargs)

def REPT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Repeats text a given number of times

	In Excel: ``REPT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("REPT(", *args, ")", **kwargs)

def RIGHT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the rightmost characters from a text value

	In Excel: ``RIGHT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RIGHT(", *args, ")", **kwargs)

def RIGHTB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the rightmost characters from a text value

	In Excel: ``RIGHTB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RIGHTB(", *args, ")", **kwargs)

def ROMAN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Converts an arabic numeral to roman, as text

	In Excel: ``ROMAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROMAN(", *args, ")", **kwargs)

def ROUND(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number to a specified number of digits

	In Excel: ``ROUND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROUND(", *args, ")", **kwargs)

def ROUNDDOWN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number down, toward zero

	In Excel: ``ROUNDDOWN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROUNDDOWN(", *args, ")", **kwargs)

def ROUNDUP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Rounds a number up, away from zero

	In Excel: ``ROUNDUP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROUNDUP(", *args, ")", **kwargs)

def ROW(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the row number of a reference

	In Excel: ``ROW()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROW(", *args, ")", **kwargs)

def ROWS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the number of rows in a reference

	In Excel: ``ROWS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ROWS(", *args, ")", **kwargs)

def RRI(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns an equivalent interest rate for the growth of an investment

	In Excel: ``RRI()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RRI(", *args, ")", **kwargs)

def RSQ(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the square of the Pearson product moment correlation coefficient

	In Excel: ``RSQ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RSQ(", *args, ")", **kwargs)

def RTD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Retrieves real-time data from a program that supports COM automation

	In Excel: ``RTD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("RTD(", *args, ")", **kwargs)

def SCAN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Scans an array by applying a LAMBDA to each value and returns an array that has each intermediate value

	In Excel: ``SCAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SCAN(", *args, ")", **kwargs)

def SEARCH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Finds one text value within another (not case-sensitive)

	In Excel: ``SEARCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SEARCH(", *args, ")", **kwargs)

def SEARCHB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Finds one text value within another (not case-sensitive)

	In Excel: ``SEARCHB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SEARCHB(", *args, ")", **kwargs)

def SEC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the secant of an angle

	In Excel: ``SEC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SEC(", *args, ")", **kwargs)

def SECH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic secant of an angle

	In Excel: ``SECH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SECH(", *args, ")", **kwargs)

def SECOND(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a second

	In Excel: ``SECOND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SECOND(", *args, ")", **kwargs)

def SEQUENCE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Generates a list of sequential numbers in an array, such as 1, 2, 3, 4

	In Excel: ``SEQUENCE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SEQUENCE(", *args, ")", **kwargs)

def SERIESSUM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of a power series based on the formula

	In Excel: ``SERIESSUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SERIESSUM(", *args, ")", **kwargs)

def SHEET(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns the sheet number of the referenced sheet

	In Excel: ``SHEET()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SHEET(", *args, ")", **kwargs)

def SHEETS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns the number of sheets in a reference

	In Excel: ``SHEETS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SHEETS(", *args, ")", **kwargs)

def SIGN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sign of a number

	In Excel: ``SIGN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SIGN(", *args, ")", **kwargs)

def SIN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sine of the given angle

	In Excel: ``SIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SIN(", *args, ")", **kwargs)

def SINH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic sine of a number

	In Excel: ``SINH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SINH(", *args, ")", **kwargs)

def SKEW(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the skewness of a distribution

	In Excel: ``SKEW()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SKEW(", *args, ")", **kwargs)

def SKEW_P(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the skewness of a distribution based on a population: a characterization of the degree of asymmetry of a distribution around its mean

	In Excel: ``SKEW.P()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SKEW.P(", *args, ")", **kwargs)

def SLN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the straight-line depreciation of an asset for one period

	In Excel: ``SLN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SLN(", *args, ")", **kwargs)

def SLOPE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the slope of the linear regression line

	In Excel: ``SLOPE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SLOPE(", *args, ")", **kwargs)

def SMALL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the k-th smallest value in a data set

	In Excel: ``SMALL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SMALL(", *args, ")", **kwargs)

def SORT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Sorts the contents of a range or array

	In Excel: ``SORT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SORT(", *args, ")", **kwargs)

def SORTBY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Sorts the contents of a range or array based on the values in a corresponding range or array

	In Excel: ``SORTBY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SORTBY(", *args, ")", **kwargs)

def SQRT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a positive square root

	In Excel: ``SQRT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SQRT(", *args, ")", **kwargs)

def SQRTPI(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the square root of (number * pi)

	In Excel: ``SQRTPI()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SQRTPI(", *args, ")", **kwargs)

def STANDARDIZE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns a normalized value

	In Excel: ``STANDARDIZE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STANDARDIZE(", *args, ")", **kwargs)

def STOCKHISTORY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Retrieves historical data about a financial instrument

	In Excel: ``STOCKHISTORY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STOCKHISTORY(", *args, ")", **kwargs)

def STDEV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Estimates standard deviation based on a sample

	In Excel: ``STDEV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEV(", *args, ")", **kwargs)

def STDEV_P(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Calculates standard deviation based on the entire population

	In Excel: ``STDEV.P()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEV.P(", *args, ")", **kwargs)

def STDEV_S(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Estimates standard deviation based on a sample

	In Excel: ``STDEV.S()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEV.S(", *args, ")", **kwargs)

def STDEVA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Estimates standard deviation based on a sample, including numbers, text, and logical values

	In Excel: ``STDEVA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEVA(", *args, ")", **kwargs)

def STDEVP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Calculates standard deviation based on the entire population

	In Excel: ``STDEVP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEVP(", *args, ")", **kwargs)

def STDEVPA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Calculates standard deviation based on the entire population, including numbers, text, and logical values

	In Excel: ``STDEVPA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STDEVPA(", *args, ")", **kwargs)

def STEYX(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the standard error of the predicted y-value for each x in the regression

	In Excel: ``STEYX()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("STEYX(", *args, ")", **kwargs)

def SUBSTITUTE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Substitutes new text for old text in a text string

	In Excel: ``SUBSTITUTE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUBSTITUTE(", *args, ")", **kwargs)

def SUBTOTAL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns a subtotal in a list or database

	In Excel: ``SUBTOTAL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUBTOTAL(", *args, ")", **kwargs)

def SUM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Adds its arguments

	In Excel: ``SUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUM(", *args, ")", **kwargs)

def SUMIF(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Adds the cells specified by a given criteria

	In Excel: ``SUMIF()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMIF(", *args, ")", **kwargs)

def SUMIFS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Adds the cells in a range that meet multiple criteria

	In Excel: ``SUMIFS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMIFS(", *args, ")", **kwargs)

def SUMPRODUCT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of the products of corresponding array components

	In Excel: ``SUMPRODUCT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMPRODUCT(", *args, ")", **kwargs)

def SUMSQ(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of the squares of the arguments

	In Excel: ``SUMSQ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMSQ(", *args, ")", **kwargs)

def SUMX2MY2(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of the difference of squares of corresponding values in two arrays

	In Excel: ``SUMX2MY2()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMX2MY2(", *args, ")", **kwargs)

def SUMX2PY2(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of the sum of squares of corresponding values in two arrays

	In Excel: ``SUMX2PY2()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMX2PY2(", *args, ")", **kwargs)

def SUMXMY2(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the sum of squares of differences of corresponding values in two arrays

	In Excel: ``SUMXMY2()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SUMXMY2(", *args, ")", **kwargs)

def SWITCH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Evaluates an expression against a list of values and returns the result corresponding to the first matching value. If there is no match, an optional default value may be returned.

	In Excel: ``SWITCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SWITCH(", *args, ")", **kwargs)

def SYD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the sum-of-years' digits depreciation of an asset for a specified period

	In Excel: ``SYD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("SYD(", *args, ")", **kwargs)

def T(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Converts its arguments to text

	In Excel: ``T()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T(", *args, ")", **kwargs)

def TAN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the tangent of a number

	In Excel: ``TAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TAN(", *args, ")", **kwargs)

def TANH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Returns the hyperbolic tangent of a number

	In Excel: ``TANH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TANH(", *args, ")", **kwargs)

def TAKE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns a specified number of contiguous rows or columns from the start or end of an array

	In Excel: ``TAKE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TAKE(", *args, ")", **kwargs)

def TBILLEQ(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the bond-equivalent yield for a Treasury bill

	In Excel: ``TBILLEQ()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TBILLEQ(", *args, ")", **kwargs)

def TBILLPRICE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the price per $100 face value for a Treasury bill

	In Excel: ``TBILLPRICE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TBILLPRICE(", *args, ")", **kwargs)

def TBILLYIELD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the yield for a Treasury bill

	In Excel: ``TBILLYIELD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TBILLYIELD(", *args, ")", **kwargs)

def T_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Percentage Points (probability) for the Student t-distribution

	In Excel: ``T.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.DIST(", *args, ")", **kwargs)

def T_DIST_2T(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Percentage Points (probability) for the Student t-distribution

	In Excel: ``T.DIST.2T()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.DIST.2T(", *args, ")", **kwargs)

def T_DIST_RT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Student's t-distribution

	In Excel: ``T.DIST.RT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.DIST.RT(", *args, ")", **kwargs)

def TDIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the Student's t-distribution

	In Excel: ``TDIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TDIST(", *args, ")", **kwargs)

def TEXT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Formats a number and converts it to text

	In Excel: ``TEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TEXT(", *args, ")", **kwargs)

def TEXTAFTER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns text that occurs after given character or string

	In Excel: ``TEXTAFTER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TEXTAFTER(", *args, ")", **kwargs)

def TEXTBEFORE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns text that occurs before a given character or string

	In Excel: ``TEXTBEFORE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TEXTBEFORE(", *args, ")", **kwargs)

def TEXTJOIN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Combines the text from multiple ranges and/or strings

	In Excel: ``TEXTJOIN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TEXTJOIN(", *args, ")", **kwargs)

def TEXTSPLIT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Splits text strings by using column and row delimiters

	In Excel: ``TEXTSPLIT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TEXTSPLIT(", *args, ")", **kwargs)

def TIME(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of a particular time

	In Excel: ``TIME()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TIME(", *args, ")", **kwargs)

def TIMEVALUE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a time in the form of text to a serial number

	In Excel: ``TIMEVALUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TIMEVALUE(", *args, ")", **kwargs)

def T_INV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the t-value of the Student's t-distribution as a function of the probability and the degrees of freedom

	In Excel: ``T.INV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.INV(", *args, ")", **kwargs)

def T_INV_2T(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the inverse of the Student's t-distribution

	In Excel: ``T.INV.2T()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.INV.2T(", *args, ")", **kwargs)

def TINV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the inverse of the Student's t-distribution

	In Excel: ``TINV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TINV(", *args, ")", **kwargs)

def TOCOL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the array in a single column

	In Excel: ``TOCOL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TOCOL(", *args, ")", **kwargs)

def TOROW(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the array in a single row

	In Excel: ``TOROW()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TOROW(", *args, ")", **kwargs)

def TODAY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of today's date

	In Excel: ``TODAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TODAY(", *args, ")", **kwargs)

def TRANSPOSE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the transpose of an array

	In Excel: ``TRANSPOSE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TRANSPOSE(", *args, ")", **kwargs)

def TREND(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns values along a linear trend

	In Excel: ``TREND()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TREND(", *args, ")", **kwargs)

def TRIM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Removes spaces from text

	In Excel: ``TRIM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TRIM(", *args, ")", **kwargs)

def TRIMMEAN(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the mean of the interior of a data set

	In Excel: ``TRIMMEAN()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TRIMMEAN(", *args, ")", **kwargs)

def TRUE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns the logical value TRUE

	In Excel: ``TRUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TRUE(", *args, ")", **kwargs)

def TRUNC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Math and trigonometry:** Truncates a number to an integer

	In Excel: ``TRUNC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TRUNC(", *args, ")", **kwargs)

def T_TEST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the probability associated with a Student's t-test

	In Excel: ``T.TEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("T.TEST(", *args, ")", **kwargs)

def TTEST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the probability associated with a Student's t-test

	In Excel: ``TTEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TTEST(", *args, ")", **kwargs)

def TYPE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Information:** Returns a number indicating the data type of a value

	In Excel: ``TYPE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("TYPE(", *args, ")", **kwargs)

def UNICHAR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the Unicode character that is references by the given numeric value

	In Excel: ``UNICHAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("UNICHAR(", *args, ")", **kwargs)

def UNICODE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns the number (code point) that corresponds to the first character of the text

	In Excel: ``UNICODE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("UNICODE(", *args, ")", **kwargs)

def UNIQUE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns a list of unique values in a list or range

	In Excel: ``UNIQUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("UNIQUE(", *args, ")", **kwargs)

def UPPER(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Converts text to uppercase

	In Excel: ``UPPER()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("UPPER(", *args, ")", **kwargs)

def VALUE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Converts a text argument to a number

	In Excel: ``VALUE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VALUE(", *args, ")", **kwargs)

def VALUETOTEXT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Text:** Returns text from any specified value

	In Excel: ``VALUETOTEXT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VALUETOTEXT(", *args, ")", **kwargs)

def VAR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Estimates variance based on a sample

	In Excel: ``VAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VAR(", *args, ")", **kwargs)

def VAR_P(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Calculates variance based on the entire population

	In Excel: ``VAR.P()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VAR.P(", *args, ")", **kwargs)

def VAR_S(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Estimates variance based on a sample

	In Excel: ``VAR.S()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VAR.S(", *args, ")", **kwargs)

def VARA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Estimates variance based on a sample, including numbers, text, and logical values

	In Excel: ``VARA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VARA(", *args, ")", **kwargs)

def VARP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Calculates variance based on the entire population

	In Excel: ``VARP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VARP(", *args, ")", **kwargs)

def VARPA(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Calculates variance based on the entire population, including numbers, text, and logical values

	In Excel: ``VARPA()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VARPA(", *args, ")", **kwargs)

def VDB(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the depreciation of an asset for a specified or partial period by using a declining balance method

	In Excel: ``VDB()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VDB(", *args, ")", **kwargs)

def VLOOKUP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Looks in the first column of an array and moves across the row to return the value of a cell

	In Excel: ``VLOOKUP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VLOOKUP(", *args, ")", **kwargs)

def VSTACK(*args: Any, **kwargs: Any) -> Func:
	"""
	**Look and reference:** Appends arrays vertically and in sequence to return a larger array

	In Excel: ``VSTACK()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("VSTACK(", *args, ")", **kwargs)

def WEBSERVICE(*args: Any, **kwargs: Any) -> Func:
	"""
	**Web:** Returns data from a web service.

	In Excel: ``WEBSERVICE()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WEBSERVICE(", *args, ")", **kwargs)

def WEEKDAY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a day of the week

	In Excel: ``WEEKDAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WEEKDAY(", *args, ")", **kwargs)

def WEEKNUM(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a number representing where the week falls numerically with a year

	In Excel: ``WEEKNUM()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WEEKNUM(", *args, ")", **kwargs)

def WEIBULL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Calculates variance based on the entire population, including numbers, text, and logical values

	In Excel: ``WEIBULL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WEIBULL(", *args, ")", **kwargs)

def WEIBULL_DIST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the Weibull distribution

	In Excel: ``WEIBULL.DIST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WEIBULL.DIST(", *args, ")", **kwargs)

def WORKDAY(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of the date before or after a specified number of workdays

	In Excel: ``WORKDAY()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WORKDAY(", *args, ")", **kwargs)

def WORKDAY_INTL(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the serial number of the date before or after a specified number of workdays using parameters to indicate which and how many days are weekend days

	In Excel: ``WORKDAY.INTL()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WORKDAY.INTL(", *args, ")", **kwargs)

def WRAPCOLS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Look and reference:** Wraps the provided row or column of values by columns after a specified number of elements

	In Excel: ``WRAPCOLS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WRAPCOLS(", *args, ")", **kwargs)

def WRAPROWS(*args: Any, **kwargs: Any) -> Func:
	"""
	**Look and reference:** Wraps the provided row or column of values by rows after a specified number of elements

	In Excel: ``WRAPROWS()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("WRAPROWS(", *args, ")", **kwargs)

def XIRR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the internal rate of return for a schedule of cash flows that is not necessarily periodic

	In Excel: ``XIRR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("XIRR(", *args, ")", **kwargs)

def XLOOKUP(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Searches a range or an array, and returns an item corresponding to the first match it finds. If a match doesn't exist, then XLOOKUP can return the closest (approximate) match. 

	In Excel: ``XLOOKUP()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("XLOOKUP(", *args, ")", **kwargs)

def XMATCH(*args: Any, **kwargs: Any) -> Func:
	"""
	**Lookup and reference:** Returns the relative position of an item in an array or range of cells. 

	In Excel: ``XMATCH()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("XMATCH(", *args, ")", **kwargs)

def XNPV(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the net present value for a schedule of cash flows that is not necessarily periodic

	In Excel: ``XNPV()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("XNPV(", *args, ")", **kwargs)

def XOR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Logical:** Returns a logical exclusive OR of all arguments

	In Excel: ``XOR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("XOR(", *args, ")", **kwargs)

def YEAR(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Converts a serial number to a year

	In Excel: ``YEAR()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("YEAR(", *args, ")", **kwargs)

def YEARFRAC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Date and time:** Returns the year fraction representing the number of whole days between start_date and end_date

	In Excel: ``YEARFRAC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("YEARFRAC(", *args, ")", **kwargs)

def YIELD(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the yield on a security that pays periodic interest

	In Excel: ``YIELD()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("YIELD(", *args, ")", **kwargs)

def YIELDDISC(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the annual yield for a discounted security; for example, a Treasury bill

	In Excel: ``YIELDDISC()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("YIELDDISC(", *args, ")", **kwargs)

def YIELDMAT(*args: Any, **kwargs: Any) -> Func:
	"""
	**Financial:** Returns the annual yield of a security that pays interest at maturity

	In Excel: ``YIELDMAT()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("YIELDMAT(", *args, ")", **kwargs)

def Z_TEST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Statistical:** Returns the one-tailed probability-value of a z-test

	In Excel: ``Z.TEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("Z.TEST(", *args, ")", **kwargs)

def ZTEST(*args: Any, **kwargs: Any) -> Func:
	"""
	**Compatibility:** Returns the one-tailed probability-value of a z-test

	In Excel: ``ZTEST()``

	Returns
	-------
	:class:`Func <excelbird.Func>`
	"""
	return Func("ZTEST(", *args, ")", **kwargs)


