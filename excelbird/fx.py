"""
All ~500 Excel functions can be accessed in Python, from the :mod:`excelbird.fx` module. They are
all documented with the same short summary as provided in Microsoft's documentation.

This let's your IDE provide autocompletion and documentation as you type, just as Excel would.

**Syntax:** Same as Excel, but dots are replaced with underscores, and letters are lowercase.

**Example:** ``T.DIST.2T()`` in Excel is :meth:`t_dist_2t() <excelbird.fx.t_dist_2t>`
"""


def abs(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ABS` - **Math and trigonometry:** Returns the absolute value of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ABS(", *args, ")", **kwargs)``
	"""
	return Func("ABS(", *args, ")", **kwargs)

def accrint(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ACCRINT` - **Financial:** Returns the accrued interest for a security that pays periodic interest

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ACCRINT(", *args, ")", **kwargs)``
	"""
	return Func("ACCRINT(", *args, ")", **kwargs)

def accrintm(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ACCRINTM` - **Financial:** Returns the accrued interest for a security that pays interest at maturity

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ACCRINTM(", *args, ")", **kwargs)``
	"""
	return Func("ACCRINTM(", *args, ")", **kwargs)

def acos(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ACOS` - **Math and trigonometry:** Returns the arccosine of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ACOS(", *args, ")", **kwargs)``
	"""
	return Func("ACOS(", *args, ")", **kwargs)

def acosh(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ACOSH` - **Math and trigonometry:** Returns the inverse hyperbolic cosine of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ACOSH(", *args, ")", **kwargs)``
	"""
	return Func("ACOSH(", *args, ")", **kwargs)

def acot(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ACOT` - **Math and trigonometry:** Returns the arccotangent of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ACOT(", *args, ")", **kwargs)``
	"""
	return Func("ACOT(", *args, ")", **kwargs)

def acoth(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ACOTH` - **Math and trigonometry:** Returns the hyperbolic arccotangent of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ACOTH(", *args, ")", **kwargs)``
	"""
	return Func("ACOTH(", *args, ")", **kwargs)

def aggregate(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`AGGREGATE` - **Math and trigonometry:** Returns an aggregate in a list or database

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("AGGREGATE(", *args, ")", **kwargs)``
	"""
	return Func("AGGREGATE(", *args, ")", **kwargs)

def address(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ADDRESS` - **Lookup and reference:** Returns a reference as text to a single cell in a worksheet

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ADDRESS(", *args, ")", **kwargs)``
	"""
	return Func("ADDRESS(", *args, ")", **kwargs)

def amordegrc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`AMORDEGRC` - **Financial:** Returns the depreciation for each accounting period by using a depreciation coefficient

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("AMORDEGRC(", *args, ")", **kwargs)``
	"""
	return Func("AMORDEGRC(", *args, ")", **kwargs)

def amorlinc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`AMORLINC` - **Financial:** Returns the depreciation for each accounting period

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("AMORLINC(", *args, ")", **kwargs)``
	"""
	return Func("AMORLINC(", *args, ")", **kwargs)

def and(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`AND` - **Logical:** Returns TRUE if all of its arguments are TRUE

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("AND(", *args, ")", **kwargs)``
	"""
	return Func("AND(", *args, ")", **kwargs)

def arabic(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ARABIC` - **Math and trigonometry:** Converts a Roman number to Arabic, as a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ARABIC(", *args, ")", **kwargs)``
	"""
	return Func("ARABIC(", *args, ")", **kwargs)

def areas(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`AREAS` - **Lookup and reference:** Returns the number of areas in a reference

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("AREAS(", *args, ")", **kwargs)``
	"""
	return Func("AREAS(", *args, ")", **kwargs)

def arraytotext(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ARRAYTOTEXT` - **Text:** Returns an array of text values from any specified range

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ARRAYTOTEXT(", *args, ")", **kwargs)``
	"""
	return Func("ARRAYTOTEXT(", *args, ")", **kwargs)

def asc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ASC` - **Text:** Changes full-width (double-byte) English letters or katakana within a character string to half-width (single-byte) characters

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ASC(", *args, ")", **kwargs)``
	"""
	return Func("ASC(", *args, ")", **kwargs)

def asin(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ASIN` - **Math and trigonometry:** Returns the arcsine of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ASIN(", *args, ")", **kwargs)``
	"""
	return Func("ASIN(", *args, ")", **kwargs)

def asinh(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ASINH` - **Math and trigonometry:** Returns the inverse hyperbolic sine of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ASINH(", *args, ")", **kwargs)``
	"""
	return Func("ASINH(", *args, ")", **kwargs)

def atan(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ATAN` - **Math and trigonometry:** Returns the arctangent of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ATAN(", *args, ")", **kwargs)``
	"""
	return Func("ATAN(", *args, ")", **kwargs)

def atan2(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ATAN2` - **Math and trigonometry:** Returns the arctangent from x- and y-coordinates

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ATAN2(", *args, ")", **kwargs)``
	"""
	return Func("ATAN2(", *args, ")", **kwargs)

def atanh(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ATANH` - **Math and trigonometry:** Returns the inverse hyperbolic tangent of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ATANH(", *args, ")", **kwargs)``
	"""
	return Func("ATANH(", *args, ")", **kwargs)

def avedev(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`AVEDEV` - **Statistical:** Returns the average of the absolute deviations of data points from their mean

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("AVEDEV(", *args, ")", **kwargs)``
	"""
	return Func("AVEDEV(", *args, ")", **kwargs)

def average(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`AVERAGE` - **Statistical:** Returns the average of its arguments

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("AVERAGE(", *args, ")", **kwargs)``
	"""
	return Func("AVERAGE(", *args, ")", **kwargs)

def averagea(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`AVERAGEA` - **Statistical:** Returns the average of its arguments, including numbers, text, and logical values

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("AVERAGEA(", *args, ")", **kwargs)``
	"""
	return Func("AVERAGEA(", *args, ")", **kwargs)

def averageif(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`AVERAGEIF` - **Statistical:** Returns the average (arithmetic mean) of all the cells in a range that meet a given criteria

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("AVERAGEIF(", *args, ")", **kwargs)``
	"""
	return Func("AVERAGEIF(", *args, ")", **kwargs)

def averageifs(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`AVERAGEIFS` - **Statistical:** Returns the average (arithmetic mean) of all cells that meet multiple criteria.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("AVERAGEIFS(", *args, ")", **kwargs)``
	"""
	return Func("AVERAGEIFS(", *args, ")", **kwargs)

def bahttext(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BAHTTEXT` - **Text:** Converts a number to text, using the ß (baht) currency format

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BAHTTEXT(", *args, ")", **kwargs)``
	"""
	return Func("BAHTTEXT(", *args, ")", **kwargs)

def base(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BASE` - **Math and trigonometry:** Converts a number into a text representation with the given radix (base)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BASE(", *args, ")", **kwargs)``
	"""
	return Func("BASE(", *args, ")", **kwargs)

def besseli(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BESSELI` - **Engineering:** Returns the modified Bessel function In(x)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BESSELI(", *args, ")", **kwargs)``
	"""
	return Func("BESSELI(", *args, ")", **kwargs)

def besselj(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BESSELJ` - **Engineering:** Returns the Bessel function Jn(x)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BESSELJ(", *args, ")", **kwargs)``
	"""
	return Func("BESSELJ(", *args, ")", **kwargs)

def besselk(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BESSELK` - **Engineering:** Returns the modified Bessel function Kn(x)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BESSELK(", *args, ")", **kwargs)``
	"""
	return Func("BESSELK(", *args, ")", **kwargs)

def bessely(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BESSELY` - **Engineering:** Returns the Bessel function Yn(x)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BESSELY(", *args, ")", **kwargs)``
	"""
	return Func("BESSELY(", *args, ")", **kwargs)

def betadist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BETADIST` - **Compatibility:** Returns the beta cumulative distribution function

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BETADIST(", *args, ")", **kwargs)``
	"""
	return Func("BETADIST(", *args, ")", **kwargs)

def beta_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BETA.DIST` - **Statistical:** Returns the beta cumulative distribution function

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BETA.DIST(", *args, ")", **kwargs)``
	"""
	return Func("BETA.DIST(", *args, ")", **kwargs)

def betainv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BETAINV` - **Compatibility:** Returns the inverse of the cumulative distribution function for a specified beta distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BETAINV(", *args, ")", **kwargs)``
	"""
	return Func("BETAINV(", *args, ")", **kwargs)

def beta_inv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BETA.INV` - **Statistical:** Returns the inverse of the cumulative distribution function for a specified beta distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BETA.INV(", *args, ")", **kwargs)``
	"""
	return Func("BETA.INV(", *args, ")", **kwargs)

def bin2dec(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BIN2DEC` - **Engineering:** Converts a binary number to decimal

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BIN2DEC(", *args, ")", **kwargs)``
	"""
	return Func("BIN2DEC(", *args, ")", **kwargs)

def bin2hex(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BIN2HEX` - **Engineering:** Converts a binary number to hexadecimal

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BIN2HEX(", *args, ")", **kwargs)``
	"""
	return Func("BIN2HEX(", *args, ")", **kwargs)

def bin2oct(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BIN2OCT` - **Engineering:** Converts a binary number to octal

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BIN2OCT(", *args, ")", **kwargs)``
	"""
	return Func("BIN2OCT(", *args, ")", **kwargs)

def binomdist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BINOMDIST` - **Compatibility:** Returns the individual term binomial distribution probability

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BINOMDIST(", *args, ")", **kwargs)``
	"""
	return Func("BINOMDIST(", *args, ")", **kwargs)

def binom_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BINOM.DIST` - **Statistical:** Returns the individual term binomial distribution probability

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BINOM.DIST(", *args, ")", **kwargs)``
	"""
	return Func("BINOM.DIST(", *args, ")", **kwargs)

def binom_dist_range(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BINOM.DIST.RANGE` - **Statistical:** Returns the probability of a trial result using a binomial distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BINOM.DIST.RANGE(", *args, ")", **kwargs)``
	"""
	return Func("BINOM.DIST.RANGE(", *args, ")", **kwargs)

def binom_inv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BINOM.INV` - **Statistical:** Returns the smallest value for which the cumulative binomial distribution is less than or equal to a criterion value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BINOM.INV(", *args, ")", **kwargs)``
	"""
	return Func("BINOM.INV(", *args, ")", **kwargs)

def bitand(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BITAND` - **Engineering:** Returns a 'Bitwise And' of two numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BITAND(", *args, ")", **kwargs)``
	"""
	return Func("BITAND(", *args, ")", **kwargs)

def bitlshift(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BITLSHIFT` - **Engineering:** Returns a value number shifted left by shift_amount bits

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BITLSHIFT(", *args, ")", **kwargs)``
	"""
	return Func("BITLSHIFT(", *args, ")", **kwargs)

def bitor(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BITOR` - **Engineering:** Returns a bitwise OR of 2 numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BITOR(", *args, ")", **kwargs)``
	"""
	return Func("BITOR(", *args, ")", **kwargs)

def bitrshift(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BITRSHIFT` - **Engineering:** Returns a value number shifted right by shift_amount bits

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BITRSHIFT(", *args, ")", **kwargs)``
	"""
	return Func("BITRSHIFT(", *args, ")", **kwargs)

def bitxor(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BITXOR` - **Engineering:** Returns a bitwise 'Exclusive Or' of two numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BITXOR(", *args, ")", **kwargs)``
	"""
	return Func("BITXOR(", *args, ")", **kwargs)

def bycol(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BYCOL` - **Logical:** Applies a LAMBDA to each column and returns an array of the results

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BYCOL(", *args, ")", **kwargs)``
	"""
	return Func("BYCOL(", *args, ")", **kwargs)

def byrow(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`BYROW` - **Logical:** Applies a LAMBDA to each row and returns an array of the results

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("BYROW(", *args, ")", **kwargs)``
	"""
	return Func("BYROW(", *args, ")", **kwargs)

def call(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CALL` - **Add-in and Automation:** Calls a procedure in a dynamic link library or code resource

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CALL(", *args, ")", **kwargs)``
	"""
	return Func("CALL(", *args, ")", **kwargs)

def ceiling(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CEILING` - **Compatibility:** Rounds a number to the nearest integer or to the nearest multiple of significance

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CEILING(", *args, ")", **kwargs)``
	"""
	return Func("CEILING(", *args, ")", **kwargs)

def ceiling_math(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CEILING.MATH` - **Math and trigonometry:** Rounds a number up, to the nearest integer or to the nearest multiple of significance

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CEILING.MATH(", *args, ")", **kwargs)``
	"""
	return Func("CEILING.MATH(", *args, ")", **kwargs)

def ceiling_precise(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CEILING.PRECISE` - **Math and trigonometry:** Rounds a number the nearest integer or to the nearest multiple of significance. Regardless of the sign of the number, the number is rounded up.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CEILING.PRECISE(", *args, ")", **kwargs)``
	"""
	return Func("CEILING.PRECISE(", *args, ")", **kwargs)

def cell(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CELL` - **Information:** Returns information about the formatting, location, or contents of a cell

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CELL(", *args, ")", **kwargs)``
	"""
	return Func("CELL(", *args, ")", **kwargs)

def char(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHAR` - **Text:** Returns the character specified by the code number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHAR(", *args, ")", **kwargs)``
	"""
	return Func("CHAR(", *args, ")", **kwargs)

def chidist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHIDIST` - **Compatibility:** Returns the one-tailed probability of the chi-squared distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHIDIST(", *args, ")", **kwargs)``
	"""
	return Func("CHIDIST(", *args, ")", **kwargs)

def chiinv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHIINV` - **Compatibility:** Returns the inverse of the one-tailed probability of the chi-squared distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHIINV(", *args, ")", **kwargs)``
	"""
	return Func("CHIINV(", *args, ")", **kwargs)

def chitest(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHITEST` - **Compatibility:** Returns the test for independence

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHITEST(", *args, ")", **kwargs)``
	"""
	return Func("CHITEST(", *args, ")", **kwargs)

def chisq_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHISQ.DIST` - **Statistical:** Returns the cumulative beta probability density function

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHISQ.DIST(", *args, ")", **kwargs)``
	"""
	return Func("CHISQ.DIST(", *args, ")", **kwargs)

def chisq_dist_rt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHISQ.DIST.RT` - **Statistical:** Returns the one-tailed probability of the chi-squared distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHISQ.DIST.RT(", *args, ")", **kwargs)``
	"""
	return Func("CHISQ.DIST.RT(", *args, ")", **kwargs)

def chisq_inv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHISQ.INV` - **Statistical:** Returns the cumulative beta probability density function

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHISQ.INV(", *args, ")", **kwargs)``
	"""
	return Func("CHISQ.INV(", *args, ")", **kwargs)

def chisq_inv_rt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHISQ.INV.RT` - **Statistical:** Returns the inverse of the one-tailed probability of the chi-squared distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHISQ.INV.RT(", *args, ")", **kwargs)``
	"""
	return Func("CHISQ.INV.RT(", *args, ")", **kwargs)

def chisq_test(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHISQ.TEST` - **Statistical:** Returns the test for independence

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHISQ.TEST(", *args, ")", **kwargs)``
	"""
	return Func("CHISQ.TEST(", *args, ")", **kwargs)

def choose(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHOOSE` - **Lookup and reference:** Chooses a value from a list of values

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHOOSE(", *args, ")", **kwargs)``
	"""
	return Func("CHOOSE(", *args, ")", **kwargs)

def choosecols(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHOOSECOLS` - **Lookup and reference:** Returns the specified columns from an array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHOOSECOLS(", *args, ")", **kwargs)``
	"""
	return Func("CHOOSECOLS(", *args, ")", **kwargs)

def chooserows(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CHOOSEROWS` - **Lookup and reference:** Returns the specified rows from an array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CHOOSEROWS(", *args, ")", **kwargs)``
	"""
	return Func("CHOOSEROWS(", *args, ")", **kwargs)

def clean(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CLEAN` - **Text:** Removes all nonprintable characters from text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CLEAN(", *args, ")", **kwargs)``
	"""
	return Func("CLEAN(", *args, ")", **kwargs)

def code(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CODE` - **Text:** Returns a numeric code for the first character in a text string

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CODE(", *args, ")", **kwargs)``
	"""
	return Func("CODE(", *args, ")", **kwargs)

def column(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COLUMN` - **Lookup and reference:** Returns the column number of a reference

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COLUMN(", *args, ")", **kwargs)``
	"""
	return Func("COLUMN(", *args, ")", **kwargs)

def columns(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COLUMNS` - **Lookup and reference:** Returns the number of columns in a reference

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COLUMNS(", *args, ")", **kwargs)``
	"""
	return Func("COLUMNS(", *args, ")", **kwargs)

def combin(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COMBIN` - **Math and trigonometry:** Returns the number of combinations for a given number of objects

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COMBIN(", *args, ")", **kwargs)``
	"""
	return Func("COMBIN(", *args, ")", **kwargs)

def combina(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COMBINA` - **Engineering:** Converts real and imaginary coefficients into a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COMBINA(", *args, ")", **kwargs)``
	"""
	return Func("COMBINA(", *args, ")", **kwargs)

def concat(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CONCAT` - **Text:** Combines the text from multiple ranges and/or strings, but it doesn't provide the delimiter or IgnoreEmpty arguments.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CONCAT(", *args, ")", **kwargs)``
	"""
	return Func("CONCAT(", *args, ")", **kwargs)

def concatenate(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CONCATENATE` - **Text:** Joins several text items into one text item

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CONCATENATE(", *args, ")", **kwargs)``
	"""
	return Func("CONCATENATE(", *args, ")", **kwargs)

def confidence(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CONFIDENCE` - **Compatibility:** Returns the confidence interval for a population mean

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CONFIDENCE(", *args, ")", **kwargs)``
	"""
	return Func("CONFIDENCE(", *args, ")", **kwargs)

def confidence_norm(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CONFIDENCE.NORM` - **Statistical:** Returns the confidence interval for a population mean

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CONFIDENCE.NORM(", *args, ")", **kwargs)``
	"""
	return Func("CONFIDENCE.NORM(", *args, ")", **kwargs)

def confidence_t(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CONFIDENCE.T` - **Statistical:** Returns the confidence interval for a population mean, using a Student's t distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CONFIDENCE.T(", *args, ")", **kwargs)``
	"""
	return Func("CONFIDENCE.T(", *args, ")", **kwargs)

def convert(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CONVERT` - **Engineering:** Converts a number from one measurement system to another

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CONVERT(", *args, ")", **kwargs)``
	"""
	return Func("CONVERT(", *args, ")", **kwargs)

def correl(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CORREL` - **Statistical:** Returns the correlation coefficient between two data sets

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CORREL(", *args, ")", **kwargs)``
	"""
	return Func("CORREL(", *args, ")", **kwargs)

def cos(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COS` - **Math and trigonometry:** Returns the cosine of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COS(", *args, ")", **kwargs)``
	"""
	return Func("COS(", *args, ")", **kwargs)

def cosh(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COSH` - **Math and trigonometry:** Returns the hyperbolic cosine of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COSH(", *args, ")", **kwargs)``
	"""
	return Func("COSH(", *args, ")", **kwargs)

def cot(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COT` - **Math and trigonometry:** Returns the hyperbolic cosine of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COT(", *args, ")", **kwargs)``
	"""
	return Func("COT(", *args, ")", **kwargs)

def coth(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COTH` - **Math and trigonometry:** Returns the cotangent of an angle

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COTH(", *args, ")", **kwargs)``
	"""
	return Func("COTH(", *args, ")", **kwargs)

def count(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUNT` - **Statistical:** Counts how many numbers are in the list of arguments

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUNT(", *args, ")", **kwargs)``
	"""
	return Func("COUNT(", *args, ")", **kwargs)

def counta(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUNTA` - **Statistical:** Counts how many values are in the list of arguments

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUNTA(", *args, ")", **kwargs)``
	"""
	return Func("COUNTA(", *args, ")", **kwargs)

def countblank(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUNTBLANK` - **Statistical:** Counts the number of blank cells within a range

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUNTBLANK(", *args, ")", **kwargs)``
	"""
	return Func("COUNTBLANK(", *args, ")", **kwargs)

def countif(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUNTIF` - **Statistical:** Counts the number of cells within a range that meet the given criteria

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUNTIF(", *args, ")", **kwargs)``
	"""
	return Func("COUNTIF(", *args, ")", **kwargs)

def countifs(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUNTIFS` - **Statistical:** Counts the number of cells within a range that meet multiple criteria

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUNTIFS(", *args, ")", **kwargs)``
	"""
	return Func("COUNTIFS(", *args, ")", **kwargs)

def coupdaybs(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUPDAYBS` - **Financial:** Returns the number of days from the beginning of the coupon period to the settlement date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUPDAYBS(", *args, ")", **kwargs)``
	"""
	return Func("COUPDAYBS(", *args, ")", **kwargs)

def coupdays(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUPDAYS` - **Financial:** Returns the number of days in the coupon period that contains the settlement date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUPDAYS(", *args, ")", **kwargs)``
	"""
	return Func("COUPDAYS(", *args, ")", **kwargs)

def coupdaysnc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUPDAYSNC` - **Financial:** Returns the number of days from the settlement date to the next coupon date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUPDAYSNC(", *args, ")", **kwargs)``
	"""
	return Func("COUPDAYSNC(", *args, ")", **kwargs)

def coupncd(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUPNCD` - **Financial:** Returns the next coupon date after the settlement date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUPNCD(", *args, ")", **kwargs)``
	"""
	return Func("COUPNCD(", *args, ")", **kwargs)

def coupnum(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUPNUM` - **Financial:** Returns the number of coupons payable between the settlement date and maturity date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUPNUM(", *args, ")", **kwargs)``
	"""
	return Func("COUPNUM(", *args, ")", **kwargs)

def couppcd(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COUPPCD` - **Financial:** Returns the previous coupon date before the settlement date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COUPPCD(", *args, ")", **kwargs)``
	"""
	return Func("COUPPCD(", *args, ")", **kwargs)

def covar(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COVAR` - **Compatibility:** Returns covariance, the average of the products of paired deviations

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COVAR(", *args, ")", **kwargs)``
	"""
	return Func("COVAR(", *args, ")", **kwargs)

def covariance_p(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COVARIANCE.P` - **Statistical:** Returns covariance, the average of the products of paired deviations

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COVARIANCE.P(", *args, ")", **kwargs)``
	"""
	return Func("COVARIANCE.P(", *args, ")", **kwargs)

def covariance_s(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`COVARIANCE.S` - **Statistical:** Returns the sample covariance, the average of the products deviations for each data point pair in two data sets

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("COVARIANCE.S(", *args, ")", **kwargs)``
	"""
	return Func("COVARIANCE.S(", *args, ")", **kwargs)

def critbinom(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CRITBINOM` - **Compatibility:** Returns the smallest value for which the cumulative binomial distribution is less than or equal to a criterion value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CRITBINOM(", *args, ")", **kwargs)``
	"""
	return Func("CRITBINOM(", *args, ")", **kwargs)

def csc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CSC` - **Math and trigonometry:** Returns the cosecant of an angle

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CSC(", *args, ")", **kwargs)``
	"""
	return Func("CSC(", *args, ")", **kwargs)

def csch(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CSCH` - **Math and trigonometry:** Returns the hyperbolic cosecant of an angle

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CSCH(", *args, ")", **kwargs)``
	"""
	return Func("CSCH(", *args, ")", **kwargs)

def cubekpimember(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CUBEKPIMEMBER` - **Cube:** Returns a key performance indicator (KPI) name, property, and measure, and displays the name and property in the cell. A KPI is a quantifiable measurement, such as monthly gross profit or quarterly employee turnover, used to monitor an organization's performance.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CUBEKPIMEMBER(", *args, ")", **kwargs)``
	"""
	return Func("CUBEKPIMEMBER(", *args, ")", **kwargs)

def cubemember(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CUBEMEMBER` - **Cube:** Returns a member or tuple in a cube hierarchy. Use to validate that the member or tuple exists in the cube.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CUBEMEMBER(", *args, ")", **kwargs)``
	"""
	return Func("CUBEMEMBER(", *args, ")", **kwargs)

def cubememberproperty(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CUBEMEMBERPROPERTY` - **Cube:** Returns the value of a member property in the cube. Use to validate that a member name exists within the cube and to return the specified property for this member.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CUBEMEMBERPROPERTY(", *args, ")", **kwargs)``
	"""
	return Func("CUBEMEMBERPROPERTY(", *args, ")", **kwargs)

def cuberankedmember(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CUBERANKEDMEMBER` - **Cube:** Returns the nth, or ranked, member in a set. Use to return one or more elements in a set, such as the top sales performer or top 10 students.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CUBERANKEDMEMBER(", *args, ")", **kwargs)``
	"""
	return Func("CUBERANKEDMEMBER(", *args, ")", **kwargs)

def cubeset(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CUBESET` - **Cube:** Defines a calculated set of members or tuples by sending a set expression to the cube on the server, which creates the set, and then returns that set to Microsoft Office Excel.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CUBESET(", *args, ")", **kwargs)``
	"""
	return Func("CUBESET(", *args, ")", **kwargs)

def cubesetcount(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CUBESETCOUNT` - **Cube:** Returns the number of items in a set.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CUBESETCOUNT(", *args, ")", **kwargs)``
	"""
	return Func("CUBESETCOUNT(", *args, ")", **kwargs)

def cubevalue(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CUBEVALUE` - **Cube:** Returns an aggregated value from a cube.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CUBEVALUE(", *args, ")", **kwargs)``
	"""
	return Func("CUBEVALUE(", *args, ")", **kwargs)

def cumipmt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CUMIPMT` - **Financial:** Returns the cumulative interest paid between two periods

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CUMIPMT(", *args, ")", **kwargs)``
	"""
	return Func("CUMIPMT(", *args, ")", **kwargs)

def cumprinc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`CUMPRINC` - **Financial:** Returns the cumulative principal paid on a loan between two periods

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("CUMPRINC(", *args, ")", **kwargs)``
	"""
	return Func("CUMPRINC(", *args, ")", **kwargs)

def date(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DATE` - **Date and time:** Returns the serial number of a particular date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DATE(", *args, ")", **kwargs)``
	"""
	return Func("DATE(", *args, ")", **kwargs)

def datedif(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DATEDIF` - **Date and time:** Calculates the number of days, months, or years between two dates. This function is useful in formulas where you need to calculate an age.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DATEDIF(", *args, ")", **kwargs)``
	"""
	return Func("DATEDIF(", *args, ")", **kwargs)

def datevalue(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DATEVALUE` - **Date and time:** Converts a date in the form of text to a serial number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DATEVALUE(", *args, ")", **kwargs)``
	"""
	return Func("DATEVALUE(", *args, ")", **kwargs)

def daverage(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DAVERAGE` - **Database:** Returns the average of selected database entries

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DAVERAGE(", *args, ")", **kwargs)``
	"""
	return Func("DAVERAGE(", *args, ")", **kwargs)

def day(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DAY` - **Date and time:** Converts a serial number to a day of the month

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DAY(", *args, ")", **kwargs)``
	"""
	return Func("DAY(", *args, ")", **kwargs)

def days(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DAYS` - **Date and time:** Returns the number of days between two dates

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DAYS(", *args, ")", **kwargs)``
	"""
	return Func("DAYS(", *args, ")", **kwargs)

def days360(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DAYS360` - **Date and time:** Calculates the number of days between two dates based on a 360-day year

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DAYS360(", *args, ")", **kwargs)``
	"""
	return Func("DAYS360(", *args, ")", **kwargs)

def db(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DB` - **Financial:** Returns the depreciation of an asset for a specified period by using the fixed-declining balance method

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DB(", *args, ")", **kwargs)``
	"""
	return Func("DB(", *args, ")", **kwargs)

def dbcs(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DBCS` - **Text:** Changes half-width (single-byte) English letters or katakana within a character string to full-width (double-byte) characters

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DBCS(", *args, ")", **kwargs)``
	"""
	return Func("DBCS(", *args, ")", **kwargs)

def dcount(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DCOUNT` - **Database:** Counts the cells that contain numbers in a database

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DCOUNT(", *args, ")", **kwargs)``
	"""
	return Func("DCOUNT(", *args, ")", **kwargs)

def dcounta(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DCOUNTA` - **Database:** Counts nonblank cells in a database

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DCOUNTA(", *args, ")", **kwargs)``
	"""
	return Func("DCOUNTA(", *args, ")", **kwargs)

def ddb(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DDB` - **Financial:** Returns the depreciation of an asset for a specified period by using the double-declining balance method or some other method that you specify

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DDB(", *args, ")", **kwargs)``
	"""
	return Func("DDB(", *args, ")", **kwargs)

def dec2bin(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DEC2BIN` - **Engineering:** Converts a decimal number to binary

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DEC2BIN(", *args, ")", **kwargs)``
	"""
	return Func("DEC2BIN(", *args, ")", **kwargs)

def dec2hex(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DEC2HEX` - **Engineering:** Converts a decimal number to hexadecimal

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DEC2HEX(", *args, ")", **kwargs)``
	"""
	return Func("DEC2HEX(", *args, ")", **kwargs)

def dec2oct(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DEC2OCT` - **Engineering:** Converts a decimal number to octal

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DEC2OCT(", *args, ")", **kwargs)``
	"""
	return Func("DEC2OCT(", *args, ")", **kwargs)

def decimal(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DECIMAL` - **Math and trigonometry:** Converts a text representation of a number in a given base into a decimal number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DECIMAL(", *args, ")", **kwargs)``
	"""
	return Func("DECIMAL(", *args, ")", **kwargs)

def degrees(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DEGREES` - **Math and trigonometry:** Converts radians to degrees

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DEGREES(", *args, ")", **kwargs)``
	"""
	return Func("DEGREES(", *args, ")", **kwargs)

def delta(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DELTA` - **Engineering:** Tests whether two values are equal

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DELTA(", *args, ")", **kwargs)``
	"""
	return Func("DELTA(", *args, ")", **kwargs)

def devsq(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DEVSQ` - **Statistical:** Returns the sum of squares of deviations

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DEVSQ(", *args, ")", **kwargs)``
	"""
	return Func("DEVSQ(", *args, ")", **kwargs)

def dget(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DGET` - **Database:** Extracts from a database a single record that matches the specified criteria

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DGET(", *args, ")", **kwargs)``
	"""
	return Func("DGET(", *args, ")", **kwargs)

def disc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DISC` - **Financial:** Returns the discount rate for a security

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DISC(", *args, ")", **kwargs)``
	"""
	return Func("DISC(", *args, ")", **kwargs)

def dmax(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DMAX` - **Database:** Returns the maximum value from selected database entries

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DMAX(", *args, ")", **kwargs)``
	"""
	return Func("DMAX(", *args, ")", **kwargs)

def dmin(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DMIN` - **Database:** Returns the minimum value from selected database entries

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DMIN(", *args, ")", **kwargs)``
	"""
	return Func("DMIN(", *args, ")", **kwargs)

def dollar(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DOLLAR` - **Text:** Converts a number to text, using the $ (dollar) currency format

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DOLLAR(", *args, ")", **kwargs)``
	"""
	return Func("DOLLAR(", *args, ")", **kwargs)

def dollarde(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DOLLARDE` - **Financial:** Converts a dollar price, expressed as a fraction, into a dollar price, expressed as a decimal number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DOLLARDE(", *args, ")", **kwargs)``
	"""
	return Func("DOLLARDE(", *args, ")", **kwargs)

def dollarfr(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DOLLARFR` - **Financial:** Converts a dollar price, expressed as a decimal number, into a dollar price, expressed as a fraction

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DOLLARFR(", *args, ")", **kwargs)``
	"""
	return Func("DOLLARFR(", *args, ")", **kwargs)

def dproduct(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DPRODUCT` - **Database:** Multiplies the values in a particular field of records that match the criteria in a database

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DPRODUCT(", *args, ")", **kwargs)``
	"""
	return Func("DPRODUCT(", *args, ")", **kwargs)

def drop(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DROP` - **Lookup and reference:** Excludes a specified number of rows or columns from the start or end of an array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DROP(", *args, ")", **kwargs)``
	"""
	return Func("DROP(", *args, ")", **kwargs)

def dstdev(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DSTDEV` - **Database:** Estimates the standard deviation based on a sample of selected database entries

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DSTDEV(", *args, ")", **kwargs)``
	"""
	return Func("DSTDEV(", *args, ")", **kwargs)

def dstdevp(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DSTDEVP` - **Database:** Calculates the standard deviation based on the entire population of selected database entries

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DSTDEVP(", *args, ")", **kwargs)``
	"""
	return Func("DSTDEVP(", *args, ")", **kwargs)

def dsum(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DSUM` - **Database:** Adds the numbers in the field column of records in the database that match the criteria

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DSUM(", *args, ")", **kwargs)``
	"""
	return Func("DSUM(", *args, ")", **kwargs)

def duration(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DURATION` - **Financial:** Returns the annual duration of a security with periodic interest payments

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DURATION(", *args, ")", **kwargs)``
	"""
	return Func("DURATION(", *args, ")", **kwargs)

def dvar(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DVAR` - **Database:** Estimates variance based on a sample from selected database entries

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DVAR(", *args, ")", **kwargs)``
	"""
	return Func("DVAR(", *args, ")", **kwargs)

def dvarp(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`DVARP` - **Database:** Calculates variance based on the entire population of selected database entries

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("DVARP(", *args, ")", **kwargs)``
	"""
	return Func("DVARP(", *args, ")", **kwargs)

def edate(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`EDATE` - **Date and time:** Returns the serial number of the date that is the indicated number of months before or after the start date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("EDATE(", *args, ")", **kwargs)``
	"""
	return Func("EDATE(", *args, ")", **kwargs)

def effect(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`EFFECT` - **Financial:** Returns the effective annual interest rate

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("EFFECT(", *args, ")", **kwargs)``
	"""
	return Func("EFFECT(", *args, ")", **kwargs)

def encodeurl(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ENCODEURL` - **Web:** Returns a URL-encoded string

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ENCODEURL(", *args, ")", **kwargs)``
	"""
	return Func("ENCODEURL(", *args, ")", **kwargs)

def eomonth(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`EOMONTH` - **Date and time:** Returns the serial number of the last day of the month before or after a specified number of months

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("EOMONTH(", *args, ")", **kwargs)``
	"""
	return Func("EOMONTH(", *args, ")", **kwargs)

def erf(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ERF` - **Engineering:** Returns the error function

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ERF(", *args, ")", **kwargs)``
	"""
	return Func("ERF(", *args, ")", **kwargs)

def erf_precise(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ERF.PRECISE` - **Engineering:** Returns the error function

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ERF.PRECISE(", *args, ")", **kwargs)``
	"""
	return Func("ERF.PRECISE(", *args, ")", **kwargs)

def erfc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ERFC` - **Engineering:** Returns the complementary error function

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ERFC(", *args, ")", **kwargs)``
	"""
	return Func("ERFC(", *args, ")", **kwargs)

def erfc_precise(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ERFC.PRECISE` - **Engineering:** Returns the complementary ERF function integrated between x and infinity

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ERFC.PRECISE(", *args, ")", **kwargs)``
	"""
	return Func("ERFC.PRECISE(", *args, ")", **kwargs)

def error_type(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ERROR.TYPE` - **Information:** Returns a number corresponding to an error type

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ERROR.TYPE(", *args, ")", **kwargs)``
	"""
	return Func("ERROR.TYPE(", *args, ")", **kwargs)

def euroconvert(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`EUROCONVERT` - **Add-in and Automation:** Converts a number to euros, converts a number from euros to a euro member currency, or converts a number from one euro member currency to another by using the euro as an intermediary (triangulation).

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("EUROCONVERT(", *args, ")", **kwargs)``
	"""
	return Func("EUROCONVERT(", *args, ")", **kwargs)

def even(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`EVEN` - **Math and trigonometry:** Rounds a number up to the nearest even integer

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("EVEN(", *args, ")", **kwargs)``
	"""
	return Func("EVEN(", *args, ")", **kwargs)

def exact(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`EXACT` - **Text:** Checks to see if two text values are identical

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("EXACT(", *args, ")", **kwargs)``
	"""
	return Func("EXACT(", *args, ")", **kwargs)

def exp(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`EXP` - **Math and trigonometry:** Returns <i class="ocpItalic">e</i> raised to the power of a given number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("EXP(", *args, ")", **kwargs)``
	"""
	return Func("EXP(", *args, ")", **kwargs)

def expand(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`EXPAND` - **Lookup and reference:** Expands or pads an array to specified row and column dimensions

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("EXPAND(", *args, ")", **kwargs)``
	"""
	return Func("EXPAND(", *args, ")", **kwargs)

def expon_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`EXPON.DIST` - **Statistical:** Returns the exponential distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("EXPON.DIST(", *args, ")", **kwargs)``
	"""
	return Func("EXPON.DIST(", *args, ")", **kwargs)

def expondist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`EXPONDIST` - **Compatibility:** Returns the exponential distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("EXPONDIST(", *args, ")", **kwargs)``
	"""
	return Func("EXPONDIST(", *args, ")", **kwargs)

def fact(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FACT` - **Math and trigonometry:** Returns the factorial of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FACT(", *args, ")", **kwargs)``
	"""
	return Func("FACT(", *args, ")", **kwargs)

def factdouble(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FACTDOUBLE` - **Math and trigonometry:** Returns the double factorial of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FACTDOUBLE(", *args, ")", **kwargs)``
	"""
	return Func("FACTDOUBLE(", *args, ")", **kwargs)

def false(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FALSE` - **Logical:** Returns the logical value FALSE

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FALSE(", *args, ")", **kwargs)``
	"""
	return Func("FALSE(", *args, ")", **kwargs)

def f_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`F.DIST` - **Statistical:** Returns the F probability distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("F.DIST(", *args, ")", **kwargs)``
	"""
	return Func("F.DIST(", *args, ")", **kwargs)

def fdist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FDIST` - **Compatibility:** Returns the F probability distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FDIST(", *args, ")", **kwargs)``
	"""
	return Func("FDIST(", *args, ")", **kwargs)

def f_dist_rt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`F.DIST.RT` - **Statistical:** Returns the F probability distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("F.DIST.RT(", *args, ")", **kwargs)``
	"""
	return Func("F.DIST.RT(", *args, ")", **kwargs)

def filter(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FILTER` - **Lookup and reference:** Filters a range of data based on criteria you define

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FILTER(", *args, ")", **kwargs)``
	"""
	return Func("FILTER(", *args, ")", **kwargs)

def filterxml(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FILTERXML` - **Web:** Returns specific data from the XML content by using the specified XPath

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FILTERXML(", *args, ")", **kwargs)``
	"""
	return Func("FILTERXML(", *args, ")", **kwargs)

def find(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FIND` - **Text:** Finds one text value within another (case-sensitive)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FIND(", *args, ")", **kwargs)``
	"""
	return Func("FIND(", *args, ")", **kwargs)

def findb(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FINDB` - **Text:** Finds one text value within another (case-sensitive)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FINDB(", *args, ")", **kwargs)``
	"""
	return Func("FINDB(", *args, ")", **kwargs)

def f_inv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`F.INV` - **Statistical:** Returns the inverse of the F probability distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("F.INV(", *args, ")", **kwargs)``
	"""
	return Func("F.INV(", *args, ")", **kwargs)

def f_inv_rt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`F.INV.RT` - **Statistical:** Returns the inverse of the F probability distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("F.INV.RT(", *args, ")", **kwargs)``
	"""
	return Func("F.INV.RT(", *args, ")", **kwargs)

def finv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FINV` - **Compatibility:** Returns the inverse of the F probability distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FINV(", *args, ")", **kwargs)``
	"""
	return Func("FINV(", *args, ")", **kwargs)

def fisher(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FISHER` - **Statistical:** Returns the Fisher transformation

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FISHER(", *args, ")", **kwargs)``
	"""
	return Func("FISHER(", *args, ")", **kwargs)

def fisherinv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FISHERINV` - **Statistical:** Returns the inverse of the Fisher transformation

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FISHERINV(", *args, ")", **kwargs)``
	"""
	return Func("FISHERINV(", *args, ")", **kwargs)

def fixed(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FIXED` - **Text:** Formats a number as text with a fixed number of decimals

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FIXED(", *args, ")", **kwargs)``
	"""
	return Func("FIXED(", *args, ")", **kwargs)

def floor(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FLOOR` - **Compatibility:** Rounds a number down, toward zero

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FLOOR(", *args, ")", **kwargs)``
	"""
	return Func("FLOOR(", *args, ")", **kwargs)

def floor_math(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FLOOR.MATH` - **Math and trigonometry:** Rounds a number down, to the nearest integer or to the nearest multiple of significance

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FLOOR.MATH(", *args, ")", **kwargs)``
	"""
	return Func("FLOOR.MATH(", *args, ")", **kwargs)

def floor_precise(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FLOOR.PRECISE` - **Math and trigonometry:** Rounds a number the nearest integer or to the nearest multiple of significance. Regardless of the sign of the number, the number is rounded up.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FLOOR.PRECISE(", *args, ")", **kwargs)``
	"""
	return Func("FLOOR.PRECISE(", *args, ")", **kwargs)

def forecast(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FORECAST` - **Statistical:** Returns a value along a linear trend

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FORECAST(", *args, ")", **kwargs)``
	"""
	return Func("FORECAST(", *args, ")", **kwargs)

def formulatext(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FORMULATEXT` - **Lookup and reference:** Returns the formula at the given reference as text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FORMULATEXT(", *args, ")", **kwargs)``
	"""
	return Func("FORMULATEXT(", *args, ")", **kwargs)

def frequency(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FREQUENCY` - **Statistical:** Returns a frequency distribution as a vertical array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FREQUENCY(", *args, ")", **kwargs)``
	"""
	return Func("FREQUENCY(", *args, ")", **kwargs)

def f_test(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`F.TEST` - **Statistical:** Returns the result of an F-test

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("F.TEST(", *args, ")", **kwargs)``
	"""
	return Func("F.TEST(", *args, ")", **kwargs)

def ftest(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FTEST` - **Compatibility:** Returns the result of an F-test

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FTEST(", *args, ")", **kwargs)``
	"""
	return Func("FTEST(", *args, ")", **kwargs)

def fv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FV` - **Financial:** Returns the future value of an investment

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FV(", *args, ")", **kwargs)``
	"""
	return Func("FV(", *args, ")", **kwargs)

def fvschedule(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`FVSCHEDULE` - **Financial:** Returns the future value of an initial principal after applying a series of compound interest rates

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("FVSCHEDULE(", *args, ")", **kwargs)``
	"""
	return Func("FVSCHEDULE(", *args, ")", **kwargs)

def gamma(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GAMMA` - **Statistical:** Returns the Gamma function value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GAMMA(", *args, ")", **kwargs)``
	"""
	return Func("GAMMA(", *args, ")", **kwargs)

def gamma_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GAMMA.DIST` - **Statistical:** Returns the gamma distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GAMMA.DIST(", *args, ")", **kwargs)``
	"""
	return Func("GAMMA.DIST(", *args, ")", **kwargs)

def gammadist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GAMMADIST` - **Compatibility:** Returns the gamma distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GAMMADIST(", *args, ")", **kwargs)``
	"""
	return Func("GAMMADIST(", *args, ")", **kwargs)

def gamma_inv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GAMMA.INV` - **Statistical:** Returns the inverse of the gamma cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GAMMA.INV(", *args, ")", **kwargs)``
	"""
	return Func("GAMMA.INV(", *args, ")", **kwargs)

def gammainv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GAMMAINV` - **Compatibility:** Returns the inverse of the gamma cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GAMMAINV(", *args, ")", **kwargs)``
	"""
	return Func("GAMMAINV(", *args, ")", **kwargs)

def gammaln(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GAMMALN` - **Statistical:** Returns the natural logarithm of the gamma function, Γ(x)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GAMMALN(", *args, ")", **kwargs)``
	"""
	return Func("GAMMALN(", *args, ")", **kwargs)

def gammaln_precise(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GAMMALN.PRECISE` - **Statistical:** Returns the natural logarithm of the gamma function, Γ(x)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GAMMALN.PRECISE(", *args, ")", **kwargs)``
	"""
	return Func("GAMMALN.PRECISE(", *args, ")", **kwargs)

def gauss(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GAUSS` - **Statistical:** Returns 0.5 less than the standard normal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GAUSS(", *args, ")", **kwargs)``
	"""
	return Func("GAUSS(", *args, ")", **kwargs)

def gcd(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GCD` - **Math and trigonometry:** Returns the greatest common divisor

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GCD(", *args, ")", **kwargs)``
	"""
	return Func("GCD(", *args, ")", **kwargs)

def geomean(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GEOMEAN` - **Statistical:** Returns the geometric mean

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GEOMEAN(", *args, ")", **kwargs)``
	"""
	return Func("GEOMEAN(", *args, ")", **kwargs)

def gestep(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GESTEP` - **Engineering:** Tests whether a number is greater than a threshold value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GESTEP(", *args, ")", **kwargs)``
	"""
	return Func("GESTEP(", *args, ")", **kwargs)

def getpivotdata(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GETPIVOTDATA` - **Lookup and reference:** Returns data stored in a PivotTable report

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GETPIVOTDATA(", *args, ")", **kwargs)``
	"""
	return Func("GETPIVOTDATA(", *args, ")", **kwargs)

def growth(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`GROWTH` - **Statistical:** Returns values along an exponential trend

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("GROWTH(", *args, ")", **kwargs)``
	"""
	return Func("GROWTH(", *args, ")", **kwargs)

def harmean(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`HARMEAN` - **Statistical:** Returns the harmonic mean

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("HARMEAN(", *args, ")", **kwargs)``
	"""
	return Func("HARMEAN(", *args, ")", **kwargs)

def hex2bin(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`HEX2BIN` - **Engineering:** Converts a hexadecimal number to binary

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("HEX2BIN(", *args, ")", **kwargs)``
	"""
	return Func("HEX2BIN(", *args, ")", **kwargs)

def hex2dec(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`HEX2DEC` - **Engineering:** Converts a hexadecimal number to decimal

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("HEX2DEC(", *args, ")", **kwargs)``
	"""
	return Func("HEX2DEC(", *args, ")", **kwargs)

def hex2oct(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`HEX2OCT` - **Engineering:** Converts a hexadecimal number to octal

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("HEX2OCT(", *args, ")", **kwargs)``
	"""
	return Func("HEX2OCT(", *args, ")", **kwargs)

def hlookup(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`HLOOKUP` - **Lookup and reference:** Looks in the top row of an array and returns the value of the indicated cell

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("HLOOKUP(", *args, ")", **kwargs)``
	"""
	return Func("HLOOKUP(", *args, ")", **kwargs)

def hour(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`HOUR` - **Date and time:** Converts a serial number to an hour

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("HOUR(", *args, ")", **kwargs)``
	"""
	return Func("HOUR(", *args, ")", **kwargs)

def hstack(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`HSTACK` - **Lookup and reference:** Appends arrays horizontally and in sequence to return a larger array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("HSTACK(", *args, ")", **kwargs)``
	"""
	return Func("HSTACK(", *args, ")", **kwargs)

def hyperlink(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`HYPERLINK` - **Lookup and reference:** Creates a shortcut or jump that opens a document stored on a network server, an intranet, or the Internet

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("HYPERLINK(", *args, ")", **kwargs)``
	"""
	return Func("HYPERLINK(", *args, ")", **kwargs)

def hypgeom_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`HYPGEOM.DIST` - **Statistical:** Returns the hypergeometric distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("HYPGEOM.DIST(", *args, ")", **kwargs)``
	"""
	return Func("HYPGEOM.DIST(", *args, ")", **kwargs)

def hypgeomdist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`HYPGEOMDIST` - **Compatibility:** Returns the hypergeometric distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("HYPGEOMDIST(", *args, ")", **kwargs)``
	"""
	return Func("HYPGEOMDIST(", *args, ")", **kwargs)

def if(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IF` - **Logical:** Specifies a logical test to perform

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IF(", *args, ")", **kwargs)``
	"""
	return Func("IF(", *args, ")", **kwargs)

def iferror(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IFERROR` - **Logical:** Returns a value you specify if a formula evaluates to an error; otherwise, returns the result of the formula

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IFERROR(", *args, ")", **kwargs)``
	"""
	return Func("IFERROR(", *args, ")", **kwargs)

def ifna(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IFNA` - **Logical:** Returns the value you specify if the expression resolves to #N/A, otherwise returns the result of the expression

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IFNA(", *args, ")", **kwargs)``
	"""
	return Func("IFNA(", *args, ")", **kwargs)

def ifs(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IFS` - **Logical:** Checks whether one or more conditions are met and returns a value that corresponds to the first TRUE condition.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IFS(", *args, ")", **kwargs)``
	"""
	return Func("IFS(", *args, ")", **kwargs)

def imabs(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMABS` - **Engineering:** Returns the absolute value (modulus) of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMABS(", *args, ")", **kwargs)``
	"""
	return Func("IMABS(", *args, ")", **kwargs)

def imaginary(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMAGINARY` - **Engineering:** Returns the imaginary coefficient of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMAGINARY(", *args, ")", **kwargs)``
	"""
	return Func("IMAGINARY(", *args, ")", **kwargs)

def imargument(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMARGUMENT` - **Engineering:** Returns the argument theta, an angle expressed in radians

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMARGUMENT(", *args, ")", **kwargs)``
	"""
	return Func("IMARGUMENT(", *args, ")", **kwargs)

def imconjugate(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMCONJUGATE` - **Engineering:** Returns the complex conjugate of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMCONJUGATE(", *args, ")", **kwargs)``
	"""
	return Func("IMCONJUGATE(", *args, ")", **kwargs)

def imcos(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMCOS` - **Engineering:** Returns the cosine of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMCOS(", *args, ")", **kwargs)``
	"""
	return Func("IMCOS(", *args, ")", **kwargs)

def imcosh(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMCOSH` - **Engineering:** Returns the hyperbolic cosine of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMCOSH(", *args, ")", **kwargs)``
	"""
	return Func("IMCOSH(", *args, ")", **kwargs)

def imcot(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMCOT` - **Engineering:** Returns the cotangent of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMCOT(", *args, ")", **kwargs)``
	"""
	return Func("IMCOT(", *args, ")", **kwargs)

def imcsc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMCSC` - **Engineering:** Returns the cosecant of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMCSC(", *args, ")", **kwargs)``
	"""
	return Func("IMCSC(", *args, ")", **kwargs)

def imcsch(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMCSCH` - **Engineering:** Returns the hyperbolic cosecant of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMCSCH(", *args, ")", **kwargs)``
	"""
	return Func("IMCSCH(", *args, ")", **kwargs)

def imdiv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMDIV` - **Engineering:** Returns the quotient of two complex numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMDIV(", *args, ")", **kwargs)``
	"""
	return Func("IMDIV(", *args, ")", **kwargs)

def imexp(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMEXP` - **Engineering:** Returns the exponential of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMEXP(", *args, ")", **kwargs)``
	"""
	return Func("IMEXP(", *args, ")", **kwargs)

def imln(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMLN` - **Engineering:** Returns the natural logarithm of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMLN(", *args, ")", **kwargs)``
	"""
	return Func("IMLN(", *args, ")", **kwargs)

def imlog10(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMLOG10` - **Engineering:** Returns the base-10 logarithm of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMLOG10(", *args, ")", **kwargs)``
	"""
	return Func("IMLOG10(", *args, ")", **kwargs)

def imlog2(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMLOG2` - **Engineering:** Returns the base-2 logarithm of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMLOG2(", *args, ")", **kwargs)``
	"""
	return Func("IMLOG2(", *args, ")", **kwargs)

def impower(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMPOWER` - **Engineering:** Returns a complex number raised to an integer power

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMPOWER(", *args, ")", **kwargs)``
	"""
	return Func("IMPOWER(", *args, ")", **kwargs)

def improduct(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMPRODUCT` - **Engineering:** Returns the product of complex numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMPRODUCT(", *args, ")", **kwargs)``
	"""
	return Func("IMPRODUCT(", *args, ")", **kwargs)

def imreal(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMREAL` - **Engineering:** Returns the real coefficient of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMREAL(", *args, ")", **kwargs)``
	"""
	return Func("IMREAL(", *args, ")", **kwargs)

def imsec(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMSEC` - **Engineering:** Returns the secant of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMSEC(", *args, ")", **kwargs)``
	"""
	return Func("IMSEC(", *args, ")", **kwargs)

def imsech(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMSECH` - **Engineering:** Returns the hyperbolic secant of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMSECH(", *args, ")", **kwargs)``
	"""
	return Func("IMSECH(", *args, ")", **kwargs)

def imsin(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMSIN` - **Engineering:** Returns the sine of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMSIN(", *args, ")", **kwargs)``
	"""
	return Func("IMSIN(", *args, ")", **kwargs)

def imsinh(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMSINH` - **Engineering:** Returns the hyperbolic sine of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMSINH(", *args, ")", **kwargs)``
	"""
	return Func("IMSINH(", *args, ")", **kwargs)

def imsqrt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMSQRT` - **Engineering:** Returns the square root of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMSQRT(", *args, ")", **kwargs)``
	"""
	return Func("IMSQRT(", *args, ")", **kwargs)

def imsub(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMSUB` - **Engineering:** Returns the difference between two complex numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMSUB(", *args, ")", **kwargs)``
	"""
	return Func("IMSUB(", *args, ")", **kwargs)

def imsum(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMSUM` - **Engineering:** Returns the sum of complex numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMSUM(", *args, ")", **kwargs)``
	"""
	return Func("IMSUM(", *args, ")", **kwargs)

def imtan(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IMTAN` - **Engineering:** Returns the tangent of a complex number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IMTAN(", *args, ")", **kwargs)``
	"""
	return Func("IMTAN(", *args, ")", **kwargs)

def index(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`INDEX` - **Lookup and reference:** Uses an index to choose a value from a reference or array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("INDEX(", *args, ")", **kwargs)``
	"""
	return Func("INDEX(", *args, ")", **kwargs)

def indirect(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`INDIRECT` - **Lookup and reference:** Returns a reference indicated by a text value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("INDIRECT(", *args, ")", **kwargs)``
	"""
	return Func("INDIRECT(", *args, ")", **kwargs)

def info(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`INFO` - **Information:** Returns information about the current operating environment

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("INFO(", *args, ")", **kwargs)``
	"""
	return Func("INFO(", *args, ")", **kwargs)

def int(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`INT` - **Math and trigonometry:** Rounds a number down to the nearest integer

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("INT(", *args, ")", **kwargs)``
	"""
	return Func("INT(", *args, ")", **kwargs)

def intercept(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`INTERCEPT` - **Statistical:** Returns the intercept of the linear regression line

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("INTERCEPT(", *args, ")", **kwargs)``
	"""
	return Func("INTERCEPT(", *args, ")", **kwargs)

def intrate(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`INTRATE` - **Financial:** Returns the interest rate for a fully invested security

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("INTRATE(", *args, ")", **kwargs)``
	"""
	return Func("INTRATE(", *args, ")", **kwargs)

def ipmt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IPMT` - **Financial:** Returns the interest payment for an investment for a given period

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IPMT(", *args, ")", **kwargs)``
	"""
	return Func("IPMT(", *args, ")", **kwargs)

def irr(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`IRR` - **Financial:** Returns the internal rate of return for a series of cash flows

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("IRR(", *args, ")", **kwargs)``
	"""
	return Func("IRR(", *args, ")", **kwargs)

def isblank(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISBLANK` - **Information:** Returns TRUE if the value is blank

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISBLANK(", *args, ")", **kwargs)``
	"""
	return Func("ISBLANK(", *args, ")", **kwargs)

def iserr(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISERR` - **Information:** Returns TRUE if the value is any error value except #N/A

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISERR(", *args, ")", **kwargs)``
	"""
	return Func("ISERR(", *args, ")", **kwargs)

def iserror(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISERROR` - **Information:** Returns TRUE if the value is any error value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISERROR(", *args, ")", **kwargs)``
	"""
	return Func("ISERROR(", *args, ")", **kwargs)

def iseven(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISEVEN` - **Information:** Returns TRUE if the number is even

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISEVEN(", *args, ")", **kwargs)``
	"""
	return Func("ISEVEN(", *args, ")", **kwargs)

def isformula(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISFORMULA` - **Information:** Returns TRUE if there is a reference to a cell that contains a formula

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISFORMULA(", *args, ")", **kwargs)``
	"""
	return Func("ISFORMULA(", *args, ")", **kwargs)

def islogical(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISLOGICAL` - **Information:** Returns TRUE if the value is a logical value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISLOGICAL(", *args, ")", **kwargs)``
	"""
	return Func("ISLOGICAL(", *args, ")", **kwargs)

def isna(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISNA` - **Information:** Returns TRUE if the value is the #N/A error value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISNA(", *args, ")", **kwargs)``
	"""
	return Func("ISNA(", *args, ")", **kwargs)

def isnontext(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISNONTEXT` - **Information:** Returns TRUE if the value is not text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISNONTEXT(", *args, ")", **kwargs)``
	"""
	return Func("ISNONTEXT(", *args, ")", **kwargs)

def isnumber(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISNUMBER` - **Information:** Returns TRUE if the value is a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISNUMBER(", *args, ")", **kwargs)``
	"""
	return Func("ISNUMBER(", *args, ")", **kwargs)

def isodd(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISODD` - **Information:** Returns TRUE if the number is odd

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISODD(", *args, ")", **kwargs)``
	"""
	return Func("ISODD(", *args, ")", **kwargs)

def isomitted(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISOMITTED` - **Information:** Checks whether the value in a LAMBDA is missing and returns TRUE or FALSE

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISOMITTED(", *args, ")", **kwargs)``
	"""
	return Func("ISOMITTED(", *args, ")", **kwargs)

def isref(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISREF` - **Information:** Returns TRUE if the value is a reference

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISREF(", *args, ")", **kwargs)``
	"""
	return Func("ISREF(", *args, ")", **kwargs)

def istext(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISTEXT` - **Information:** Returns TRUE if the value is text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISTEXT(", *args, ")", **kwargs)``
	"""
	return Func("ISTEXT(", *args, ")", **kwargs)

def iso_ceiling(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISO.CEILING` - **Math and trigonometry:** Returns a number that is rounded up to the nearest integer or to the nearest multiple of significance

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISO.CEILING(", *args, ")", **kwargs)``
	"""
	return Func("ISO.CEILING(", *args, ")", **kwargs)

def isoweeknum(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISOWEEKNUM` - **Date and time:** Returns the number of the ISO week number of the year for a given date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISOWEEKNUM(", *args, ")", **kwargs)``
	"""
	return Func("ISOWEEKNUM(", *args, ")", **kwargs)

def ispmt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ISPMT` - **Financial:** Calculates the interest paid during a specific period of an investment

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ISPMT(", *args, ")", **kwargs)``
	"""
	return Func("ISPMT(", *args, ")", **kwargs)

def jis(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`JIS` - **Text:** Changes half-width (single-byte) characters within a string to full-width (double-byte) characters

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("JIS(", *args, ")", **kwargs)``
	"""
	return Func("JIS(", *args, ")", **kwargs)

def kurt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`KURT` - **Statistical:** Returns the kurtosis of a data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("KURT(", *args, ")", **kwargs)``
	"""
	return Func("KURT(", *args, ")", **kwargs)

def lambda(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LAMBDA` - **Logical:** Create custom, reusable functions and call them by a friendly name

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LAMBDA(", *args, ")", **kwargs)``
	"""
	return Func("LAMBDA(", *args, ")", **kwargs)

def large(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LARGE` - **Statistical:** Returns the k-th largest value in a data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LARGE(", *args, ")", **kwargs)``
	"""
	return Func("LARGE(", *args, ")", **kwargs)

def lcm(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LCM` - **Math and trigonometry:** Returns the least common multiple

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LCM(", *args, ")", **kwargs)``
	"""
	return Func("LCM(", *args, ")", **kwargs)

def left(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LEFT` - **Text:** Returns the leftmost characters from a text value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LEFT(", *args, ")", **kwargs)``
	"""
	return Func("LEFT(", *args, ")", **kwargs)

def leftb(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LEFTB` - **Text:** Returns the leftmost characters from a text value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LEFTB(", *args, ")", **kwargs)``
	"""
	return Func("LEFTB(", *args, ")", **kwargs)

def len(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LEN` - **Text:** Returns the number of characters in a text string

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LEN(", *args, ")", **kwargs)``
	"""
	return Func("LEN(", *args, ")", **kwargs)

def lenb(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LENB` - **Text:** Returns the number of characters in a text string

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LENB(", *args, ")", **kwargs)``
	"""
	return Func("LENB(", *args, ")", **kwargs)

def let(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LET` - **Logical:** Assigns names to calculation results

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LET(", *args, ")", **kwargs)``
	"""
	return Func("LET(", *args, ")", **kwargs)

def linest(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LINEST` - **Statistical:** Returns the parameters of a linear trend

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LINEST(", *args, ")", **kwargs)``
	"""
	return Func("LINEST(", *args, ")", **kwargs)

def ln(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LN` - **Math and trigonometry:** Returns the natural logarithm of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LN(", *args, ")", **kwargs)``
	"""
	return Func("LN(", *args, ")", **kwargs)

def log(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LOG` - **Math and trigonometry:** Returns the logarithm of a number to a specified base

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LOG(", *args, ")", **kwargs)``
	"""
	return Func("LOG(", *args, ")", **kwargs)

def log10(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LOG10` - **Math and trigonometry:** Returns the base-10 logarithm of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LOG10(", *args, ")", **kwargs)``
	"""
	return Func("LOG10(", *args, ")", **kwargs)

def logest(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LOGEST` - **Statistical:** Returns the parameters of an exponential trend

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LOGEST(", *args, ")", **kwargs)``
	"""
	return Func("LOGEST(", *args, ")", **kwargs)

def loginv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LOGINV` - **Compatibility:** Returns the inverse of the lognormal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LOGINV(", *args, ")", **kwargs)``
	"""
	return Func("LOGINV(", *args, ")", **kwargs)

def lognorm_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LOGNORM.DIST` - **Statistical:** Returns the cumulative lognormal distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LOGNORM.DIST(", *args, ")", **kwargs)``
	"""
	return Func("LOGNORM.DIST(", *args, ")", **kwargs)

def lognormdist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LOGNORMDIST` - **Compatibility:** Returns the cumulative lognormal distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LOGNORMDIST(", *args, ")", **kwargs)``
	"""
	return Func("LOGNORMDIST(", *args, ")", **kwargs)

def lognorm_inv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LOGNORM.INV` - **Statistical:** Returns the inverse of the lognormal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LOGNORM.INV(", *args, ")", **kwargs)``
	"""
	return Func("LOGNORM.INV(", *args, ")", **kwargs)

def lookup(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LOOKUP` - **Lookup and reference:** Looks up values in a vector or array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LOOKUP(", *args, ")", **kwargs)``
	"""
	return Func("LOOKUP(", *args, ")", **kwargs)

def lower(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`LOWER` - **Text:** Converts text to lowercase

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("LOWER(", *args, ")", **kwargs)``
	"""
	return Func("LOWER(", *args, ")", **kwargs)

def makearray(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MAKEARRAY` - **Logical:** Returns a calculated array of a specified row and column size, by applying a LAMBDA

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MAKEARRAY(", *args, ")", **kwargs)``
	"""
	return Func("MAKEARRAY(", *args, ")", **kwargs)

def map(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MAP` - **Logical:** Returns an array formed by mapping each value in the array(s) to a new value by applying a LAMBDA to create a new value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MAP(", *args, ")", **kwargs)``
	"""
	return Func("MAP(", *args, ")", **kwargs)

def match(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MATCH` - **Lookup and reference:** Looks up values in a reference or array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MATCH(", *args, ")", **kwargs)``
	"""
	return Func("MATCH(", *args, ")", **kwargs)

def max(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MAX` - **Statistical:** Returns the maximum value in a list of arguments

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MAX(", *args, ")", **kwargs)``
	"""
	return Func("MAX(", *args, ")", **kwargs)

def maxa(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MAXA` - **Statistical:** Returns the maximum value in a list of arguments, including numbers, text, and logical values

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MAXA(", *args, ")", **kwargs)``
	"""
	return Func("MAXA(", *args, ")", **kwargs)

def maxifs(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MAXIFS` - **Statistical:** Returns the maximum value among cells specified by a given set of conditions or criteria

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MAXIFS(", *args, ")", **kwargs)``
	"""
	return Func("MAXIFS(", *args, ")", **kwargs)

def mdeterm(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MDETERM` - **Math and trigonometry:** Returns the matrix determinant of an array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MDETERM(", *args, ")", **kwargs)``
	"""
	return Func("MDETERM(", *args, ")", **kwargs)

def mduration(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MDURATION` - **Financial:** Returns the Macauley modified duration for a security with an assumed par value of $100

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MDURATION(", *args, ")", **kwargs)``
	"""
	return Func("MDURATION(", *args, ")", **kwargs)

def median(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MEDIAN` - **Statistical:** Returns the median of the given numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MEDIAN(", *args, ")", **kwargs)``
	"""
	return Func("MEDIAN(", *args, ")", **kwargs)

def mid(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MID` - **Text:** Returns a specific number of characters from a text string starting at the position you specify

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MID(", *args, ")", **kwargs)``
	"""
	return Func("MID(", *args, ")", **kwargs)

def midb(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MIDB` - **Text:** Returns a specific number of characters from a text string starting at the position you specify

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MIDB(", *args, ")", **kwargs)``
	"""
	return Func("MIDB(", *args, ")", **kwargs)

def min(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MIN` - **Statistical:** Returns the minimum value in a list of arguments

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MIN(", *args, ")", **kwargs)``
	"""
	return Func("MIN(", *args, ")", **kwargs)

def minifs(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MINIFS` - **Statistical:** Returns the minimum value among cells specified by a given set of conditions or criteria.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MINIFS(", *args, ")", **kwargs)``
	"""
	return Func("MINIFS(", *args, ")", **kwargs)

def mina(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MINA` - **Statistical:** Returns the smallest value in a list of arguments, including numbers, text, and logical values

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MINA(", *args, ")", **kwargs)``
	"""
	return Func("MINA(", *args, ")", **kwargs)

def minute(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MINUTE` - **Date and time:** Converts a serial number to a minute

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MINUTE(", *args, ")", **kwargs)``
	"""
	return Func("MINUTE(", *args, ")", **kwargs)

def minverse(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MINVERSE` - **Math and trigonometry:** Returns the matrix inverse of an array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MINVERSE(", *args, ")", **kwargs)``
	"""
	return Func("MINVERSE(", *args, ")", **kwargs)

def mirr(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MIRR` - **Financial:** Returns the internal rate of return where positive and negative cash flows are financed at different rates

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MIRR(", *args, ")", **kwargs)``
	"""
	return Func("MIRR(", *args, ")", **kwargs)

def mmult(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MMULT` - **Math and trigonometry:** Returns the matrix product of two arrays

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MMULT(", *args, ")", **kwargs)``
	"""
	return Func("MMULT(", *args, ")", **kwargs)

def mod(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MOD` - **Math and trigonometry:** Returns the remainder from division

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MOD(", *args, ")", **kwargs)``
	"""
	return Func("MOD(", *args, ")", **kwargs)

def mode(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MODE` - **Compatibility:** Returns the most common value in a data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MODE(", *args, ")", **kwargs)``
	"""
	return Func("MODE(", *args, ")", **kwargs)

def mode_mult(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MODE.MULT` - **Statistical:** Returns a vertical array of the most frequently occurring, or repetitive values in an array or range of data

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MODE.MULT(", *args, ")", **kwargs)``
	"""
	return Func("MODE.MULT(", *args, ")", **kwargs)

def mode_sngl(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MODE.SNGL` - **Statistical:** Returns the most common value in a data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MODE.SNGL(", *args, ")", **kwargs)``
	"""
	return Func("MODE.SNGL(", *args, ")", **kwargs)

def month(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MONTH` - **Date and time:** Converts a serial number to a month

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MONTH(", *args, ")", **kwargs)``
	"""
	return Func("MONTH(", *args, ")", **kwargs)

def mround(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MROUND` - **Math and trigonometry:** Returns a number rounded to the desired multiple

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MROUND(", *args, ")", **kwargs)``
	"""
	return Func("MROUND(", *args, ")", **kwargs)

def multinomial(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MULTINOMIAL` - **Math and trigonometry:** Returns the multinomial of a set of numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MULTINOMIAL(", *args, ")", **kwargs)``
	"""
	return Func("MULTINOMIAL(", *args, ")", **kwargs)

def munit(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`MUNIT` - **Math and trigonometry:** Returns the unit matrix or the specified dimension

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("MUNIT(", *args, ")", **kwargs)``
	"""
	return Func("MUNIT(", *args, ")", **kwargs)

def n(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`N` - **Information:** Returns a value converted to a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("N(", *args, ")", **kwargs)``
	"""
	return Func("N(", *args, ")", **kwargs)

def na(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NA` - **Information:** Returns the error value #N/A

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NA(", *args, ")", **kwargs)``
	"""
	return Func("NA(", *args, ")", **kwargs)

def negbinom_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NEGBINOM.DIST` - **Statistical:** Returns the negative binomial distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NEGBINOM.DIST(", *args, ")", **kwargs)``
	"""
	return Func("NEGBINOM.DIST(", *args, ")", **kwargs)

def negbinomdist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NEGBINOMDIST` - **Compatibility:** Returns the negative binomial distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NEGBINOMDIST(", *args, ")", **kwargs)``
	"""
	return Func("NEGBINOMDIST(", *args, ")", **kwargs)

def networkdays(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NETWORKDAYS` - **Date and time:** Returns the number of whole workdays between two dates

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NETWORKDAYS(", *args, ")", **kwargs)``
	"""
	return Func("NETWORKDAYS(", *args, ")", **kwargs)

def networkdays_intl(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NETWORKDAYS.INTL` - **Date and time:** Returns the number of whole workdays between two dates using parameters to indicate which and how many days are weekend days

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NETWORKDAYS.INTL(", *args, ")", **kwargs)``
	"""
	return Func("NETWORKDAYS.INTL(", *args, ")", **kwargs)

def nominal(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NOMINAL` - **Financial:** Returns the annual nominal interest rate

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NOMINAL(", *args, ")", **kwargs)``
	"""
	return Func("NOMINAL(", *args, ")", **kwargs)

def norm_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NORM.DIST` - **Statistical:** Returns the normal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NORM.DIST(", *args, ")", **kwargs)``
	"""
	return Func("NORM.DIST(", *args, ")", **kwargs)

def normdist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NORMDIST` - **Compatibility:** Returns the normal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NORMDIST(", *args, ")", **kwargs)``
	"""
	return Func("NORMDIST(", *args, ")", **kwargs)

def norminv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NORMINV` - **Statistical:** Returns the inverse of the normal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NORMINV(", *args, ")", **kwargs)``
	"""
	return Func("NORMINV(", *args, ")", **kwargs)

def norm_inv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NORM.INV` - **Compatibility:** Returns the inverse of the normal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NORM.INV(", *args, ")", **kwargs)``
	"""
	return Func("NORM.INV(", *args, ")", **kwargs)

def norm_s_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NORM.S.DIST` - **Statistical:** Returns the standard normal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NORM.S.DIST(", *args, ")", **kwargs)``
	"""
	return Func("NORM.S.DIST(", *args, ")", **kwargs)

def normsdist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NORMSDIST` - **Compatibility:** Returns the standard normal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NORMSDIST(", *args, ")", **kwargs)``
	"""
	return Func("NORMSDIST(", *args, ")", **kwargs)

def norm_s_inv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NORM.S.INV` - **Statistical:** Returns the inverse of the standard normal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NORM.S.INV(", *args, ")", **kwargs)``
	"""
	return Func("NORM.S.INV(", *args, ")", **kwargs)

def normsinv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NORMSINV` - **Compatibility:** Returns the inverse of the standard normal cumulative distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NORMSINV(", *args, ")", **kwargs)``
	"""
	return Func("NORMSINV(", *args, ")", **kwargs)

def not(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NOT` - **Logical:** Reverses the logic of its argument

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NOT(", *args, ")", **kwargs)``
	"""
	return Func("NOT(", *args, ")", **kwargs)

def now(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NOW` - **Date and time:** Returns the serial number of the current date and time

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NOW(", *args, ")", **kwargs)``
	"""
	return Func("NOW(", *args, ")", **kwargs)

def nper(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NPER` - **Financial:** Returns the number of periods for an investment

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NPER(", *args, ")", **kwargs)``
	"""
	return Func("NPER(", *args, ")", **kwargs)

def npv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NPV` - **Financial:** Returns the net present value of an investment based on a series of periodic cash flows and a discount rate

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NPV(", *args, ")", **kwargs)``
	"""
	return Func("NPV(", *args, ")", **kwargs)

def numbervalue(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`NUMBERVALUE` - **Text:** Converts text to number in a locale-independent manner

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("NUMBERVALUE(", *args, ")", **kwargs)``
	"""
	return Func("NUMBERVALUE(", *args, ")", **kwargs)

def oct2bin(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`OCT2BIN` - **Engineering:** Converts an octal number to binary

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("OCT2BIN(", *args, ")", **kwargs)``
	"""
	return Func("OCT2BIN(", *args, ")", **kwargs)

def oct2dec(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`OCT2DEC` - **Engineering:** Converts an octal number to decimal

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("OCT2DEC(", *args, ")", **kwargs)``
	"""
	return Func("OCT2DEC(", *args, ")", **kwargs)

def oct2hex(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`OCT2HEX` - **Engineering:** Converts an octal number to hexadecimal

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("OCT2HEX(", *args, ")", **kwargs)``
	"""
	return Func("OCT2HEX(", *args, ")", **kwargs)

def odd(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ODD` - **Math and trigonometry:** Rounds a number up to the nearest odd integer

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ODD(", *args, ")", **kwargs)``
	"""
	return Func("ODD(", *args, ")", **kwargs)

def oddfprice(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ODDFPRICE` - **Financial:** Returns the price per $100 face value of a security with an odd first period

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ODDFPRICE(", *args, ")", **kwargs)``
	"""
	return Func("ODDFPRICE(", *args, ")", **kwargs)

def oddfyield(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ODDFYIELD` - **Financial:** Returns the yield of a security with an odd first period

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ODDFYIELD(", *args, ")", **kwargs)``
	"""
	return Func("ODDFYIELD(", *args, ")", **kwargs)

def oddlprice(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ODDLPRICE` - **Financial:** Returns the price per $100 face value of a security with an odd last period

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ODDLPRICE(", *args, ")", **kwargs)``
	"""
	return Func("ODDLPRICE(", *args, ")", **kwargs)

def oddlyield(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ODDLYIELD` - **Financial:** Returns the yield of a security with an odd last period

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ODDLYIELD(", *args, ")", **kwargs)``
	"""
	return Func("ODDLYIELD(", *args, ")", **kwargs)

def offset(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`OFFSET` - **Lookup and reference:** Returns a reference offset from a given reference

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("OFFSET(", *args, ")", **kwargs)``
	"""
	return Func("OFFSET(", *args, ")", **kwargs)

def or(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`OR` - **Logical:** Returns TRUE if any argument is TRUE

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("OR(", *args, ")", **kwargs)``
	"""
	return Func("OR(", *args, ")", **kwargs)

def pduration(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PDURATION` - **Financial:** Returns the number of periods required by an investment to reach a specified value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PDURATION(", *args, ")", **kwargs)``
	"""
	return Func("PDURATION(", *args, ")", **kwargs)

def pearson(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PEARSON` - **Statistical:** Returns the Pearson product moment correlation coefficient

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PEARSON(", *args, ")", **kwargs)``
	"""
	return Func("PEARSON(", *args, ")", **kwargs)

def percentile_exc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PERCENTILE.EXC` - **Statistical:** Returns the k-th percentile of values in a range, where k is in the range 0..1, exclusive

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PERCENTILE.EXC(", *args, ")", **kwargs)``
	"""
	return Func("PERCENTILE.EXC(", *args, ")", **kwargs)

def percentile_inc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PERCENTILE.INC` - **Statistical:** Returns the k-th percentile of values in a range

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PERCENTILE.INC(", *args, ")", **kwargs)``
	"""
	return Func("PERCENTILE.INC(", *args, ")", **kwargs)

def percentile(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PERCENTILE` - **Compatibility:** Returns the k-th percentile of values in a range

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PERCENTILE(", *args, ")", **kwargs)``
	"""
	return Func("PERCENTILE(", *args, ")", **kwargs)

def percentrank_exc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PERCENTRANK.EXC` - **Statistical:** Returns the rank of a value in a data set as a percentage (0..1, exclusive) of the data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PERCENTRANK.EXC(", *args, ")", **kwargs)``
	"""
	return Func("PERCENTRANK.EXC(", *args, ")", **kwargs)

def percentrank_inc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PERCENTRANK.INC` - **Statistical:** Returns the percentage rank of a value in a data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PERCENTRANK.INC(", *args, ")", **kwargs)``
	"""
	return Func("PERCENTRANK.INC(", *args, ")", **kwargs)

def percentrank(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PERCENTRANK` - **Compatibility:** Returns the percentage rank of a value in a data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PERCENTRANK(", *args, ")", **kwargs)``
	"""
	return Func("PERCENTRANK(", *args, ")", **kwargs)

def permut(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PERMUT` - **Statistical:** Returns the number of permutations for a given number of objects

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PERMUT(", *args, ")", **kwargs)``
	"""
	return Func("PERMUT(", *args, ")", **kwargs)

def permutationa(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PERMUTATIONA` - **Statistical:** Returns the number of permutations for a given number of objects (with repetitions) that can be selected from the total objects

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PERMUTATIONA(", *args, ")", **kwargs)``
	"""
	return Func("PERMUTATIONA(", *args, ")", **kwargs)

def phi(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PHI` - **Statistical:** Returns the value of the density function for a standard normal distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PHI(", *args, ")", **kwargs)``
	"""
	return Func("PHI(", *args, ")", **kwargs)

def phonetic(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PHONETIC` - **Text:** Extracts the phonetic (furigana) characters from a text string

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PHONETIC(", *args, ")", **kwargs)``
	"""
	return Func("PHONETIC(", *args, ")", **kwargs)

def pi(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PI` - **Math and trigonometry:** Returns the value of pi

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PI(", *args, ")", **kwargs)``
	"""
	return Func("PI(", *args, ")", **kwargs)

def pmt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PMT` - **Financial:** Returns the periodic payment for an annuity

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PMT(", *args, ")", **kwargs)``
	"""
	return Func("PMT(", *args, ")", **kwargs)

def poisson_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`POISSON.DIST` - **Statistical:** Returns the Poisson distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("POISSON.DIST(", *args, ")", **kwargs)``
	"""
	return Func("POISSON.DIST(", *args, ")", **kwargs)

def poisson(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`POISSON` - **Compatibility:** Returns the Poisson distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("POISSON(", *args, ")", **kwargs)``
	"""
	return Func("POISSON(", *args, ")", **kwargs)

def power(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`POWER` - **Math and trigonometry:** Returns the result of a number raised to a power

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("POWER(", *args, ")", **kwargs)``
	"""
	return Func("POWER(", *args, ")", **kwargs)

def ppmt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PPMT` - **Financial:** Returns the payment on the principal for an investment for a given period

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PPMT(", *args, ")", **kwargs)``
	"""
	return Func("PPMT(", *args, ")", **kwargs)

def price(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PRICE` - **Financial:** Returns the price per $100 face value of a security that pays periodic interest

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PRICE(", *args, ")", **kwargs)``
	"""
	return Func("PRICE(", *args, ")", **kwargs)

def pricedisc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PRICEDISC` - **Financial:** Returns the price per $100 face value of a discounted security

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PRICEDISC(", *args, ")", **kwargs)``
	"""
	return Func("PRICEDISC(", *args, ")", **kwargs)

def pricemat(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PRICEMAT` - **Financial:** Returns the price per $100 face value of a security that pays interest at maturity

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PRICEMAT(", *args, ")", **kwargs)``
	"""
	return Func("PRICEMAT(", *args, ")", **kwargs)

def prob(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PROB` - **Statistical:** Returns the probability that values in a range are between two limits

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PROB(", *args, ")", **kwargs)``
	"""
	return Func("PROB(", *args, ")", **kwargs)

def product(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PRODUCT` - **Math and trigonometry:** Multiplies its arguments

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PRODUCT(", *args, ")", **kwargs)``
	"""
	return Func("PRODUCT(", *args, ")", **kwargs)

def proper(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PROPER` - **Text:** Capitalizes the first letter in each word of a text value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PROPER(", *args, ")", **kwargs)``
	"""
	return Func("PROPER(", *args, ")", **kwargs)

def pv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`PV` - **Financial:** Returns the present value of an investment

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("PV(", *args, ")", **kwargs)``
	"""
	return Func("PV(", *args, ")", **kwargs)

def quartile(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`QUARTILE` - **Compatibility:** Returns the quartile of a data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("QUARTILE(", *args, ")", **kwargs)``
	"""
	return Func("QUARTILE(", *args, ")", **kwargs)

def quartile_exc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`QUARTILE.EXC` - **Statistical:** Returns the quartile of the data set, based on percentile values from 0..1, exclusive

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("QUARTILE.EXC(", *args, ")", **kwargs)``
	"""
	return Func("QUARTILE.EXC(", *args, ")", **kwargs)

def quartile_inc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`QUARTILE.INC` - **Statistical:** Returns the quartile of a data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("QUARTILE.INC(", *args, ")", **kwargs)``
	"""
	return Func("QUARTILE.INC(", *args, ")", **kwargs)

def quotient(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`QUOTIENT` - **Math and trigonometry:** Returns the integer portion of a division

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("QUOTIENT(", *args, ")", **kwargs)``
	"""
	return Func("QUOTIENT(", *args, ")", **kwargs)

def radians(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RADIANS` - **Math and trigonometry:** Converts degrees to radians

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RADIANS(", *args, ")", **kwargs)``
	"""
	return Func("RADIANS(", *args, ")", **kwargs)

def rand(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RAND` - **Math and trigonometry:** Returns a random number between 0 and 1

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RAND(", *args, ")", **kwargs)``
	"""
	return Func("RAND(", *args, ")", **kwargs)

def randarray(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RANDARRAY` - **Math and trigonometry:** Returns an array of random numbers between 0 and 1. However, you can specify the number of rows and columns to fill, minimum and maximum values, and whether to return whole numbers or decimal values.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RANDARRAY(", *args, ")", **kwargs)``
	"""
	return Func("RANDARRAY(", *args, ")", **kwargs)

def randbetween(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RANDBETWEEN` - **Math and trigonometry:** Returns a random number between the numbers you specify

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RANDBETWEEN(", *args, ")", **kwargs)``
	"""
	return Func("RANDBETWEEN(", *args, ")", **kwargs)

def rank_avg(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RANK.AVG` - **Statistical:** Returns the rank of a number in a list of numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RANK.AVG(", *args, ")", **kwargs)``
	"""
	return Func("RANK.AVG(", *args, ")", **kwargs)

def rank_eq(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RANK.EQ` - **Statistical:** Returns the rank of a number in a list of numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RANK.EQ(", *args, ")", **kwargs)``
	"""
	return Func("RANK.EQ(", *args, ")", **kwargs)

def rank(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RANK` - **Compatibility:** Returns the rank of a number in a list of numbers

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RANK(", *args, ")", **kwargs)``
	"""
	return Func("RANK(", *args, ")", **kwargs)

def rate(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RATE` - **Financial:** Returns the interest rate per period of an annuity

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RATE(", *args, ")", **kwargs)``
	"""
	return Func("RATE(", *args, ")", **kwargs)

def received(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RECEIVED` - **Financial:** Returns the amount received at maturity for a fully invested security

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RECEIVED(", *args, ")", **kwargs)``
	"""
	return Func("RECEIVED(", *args, ")", **kwargs)

def reduce(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`REDUCE` - **Logical:** Reduces an array to an accumulated value by applying a LAMBDA to each value and returning the total value in the accumulator

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("REDUCE(", *args, ")", **kwargs)``
	"""
	return Func("REDUCE(", *args, ")", **kwargs)

def register_id(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`REGISTER.ID` - **Add-in and Automation:** Returns the register ID of the specified dynamic link library (DLL) or code resource that has been previously registered

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("REGISTER.ID(", *args, ")", **kwargs)``
	"""
	return Func("REGISTER.ID(", *args, ")", **kwargs)

def replace(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`REPLACE` - **Text:** Replaces characters within text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("REPLACE(", *args, ")", **kwargs)``
	"""
	return Func("REPLACE(", *args, ")", **kwargs)

def replaceb(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`REPLACEB` - **Text:** Replaces characters within text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("REPLACEB(", *args, ")", **kwargs)``
	"""
	return Func("REPLACEB(", *args, ")", **kwargs)

def rept(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`REPT` - **Text:** Repeats text a given number of times

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("REPT(", *args, ")", **kwargs)``
	"""
	return Func("REPT(", *args, ")", **kwargs)

def right(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RIGHT` - **Text:** Returns the rightmost characters from a text value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RIGHT(", *args, ")", **kwargs)``
	"""
	return Func("RIGHT(", *args, ")", **kwargs)

def rightb(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RIGHTB` - **Text:** Returns the rightmost characters from a text value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RIGHTB(", *args, ")", **kwargs)``
	"""
	return Func("RIGHTB(", *args, ")", **kwargs)

def roman(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ROMAN` - **Math and trigonometry:** Converts an arabic numeral to roman, as text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ROMAN(", *args, ")", **kwargs)``
	"""
	return Func("ROMAN(", *args, ")", **kwargs)

def round(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ROUND` - **Math and trigonometry:** Rounds a number to a specified number of digits

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ROUND(", *args, ")", **kwargs)``
	"""
	return Func("ROUND(", *args, ")", **kwargs)

def rounddown(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ROUNDDOWN` - **Math and trigonometry:** Rounds a number down, toward zero

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ROUNDDOWN(", *args, ")", **kwargs)``
	"""
	return Func("ROUNDDOWN(", *args, ")", **kwargs)

def roundup(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ROUNDUP` - **Math and trigonometry:** Rounds a number up, away from zero

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ROUNDUP(", *args, ")", **kwargs)``
	"""
	return Func("ROUNDUP(", *args, ")", **kwargs)

def row(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ROW` - **Lookup and reference:** Returns the row number of a reference

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ROW(", *args, ")", **kwargs)``
	"""
	return Func("ROW(", *args, ")", **kwargs)

def rows(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ROWS` - **Lookup and reference:** Returns the number of rows in a reference

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ROWS(", *args, ")", **kwargs)``
	"""
	return Func("ROWS(", *args, ")", **kwargs)

def rri(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RRI` - **Financial:** Returns an equivalent interest rate for the growth of an investment

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RRI(", *args, ")", **kwargs)``
	"""
	return Func("RRI(", *args, ")", **kwargs)

def rsq(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RSQ` - **Statistical:** Returns the square of the Pearson product moment correlation coefficient

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RSQ(", *args, ")", **kwargs)``
	"""
	return Func("RSQ(", *args, ")", **kwargs)

def rtd(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`RTD` - **Lookup and reference:** Retrieves real-time data from a program that supports COM automation

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("RTD(", *args, ")", **kwargs)``
	"""
	return Func("RTD(", *args, ")", **kwargs)

def scan(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SCAN` - **Logical:** Scans an array by applying a LAMBDA to each value and returns an array that has each intermediate value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SCAN(", *args, ")", **kwargs)``
	"""
	return Func("SCAN(", *args, ")", **kwargs)

def search(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SEARCH` - **Text:** Finds one text value within another (not case-sensitive)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SEARCH(", *args, ")", **kwargs)``
	"""
	return Func("SEARCH(", *args, ")", **kwargs)

def searchb(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SEARCHB` - **Text:** Finds one text value within another (not case-sensitive)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SEARCHB(", *args, ")", **kwargs)``
	"""
	return Func("SEARCHB(", *args, ")", **kwargs)

def sec(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SEC` - **Math and trigonometry:** Returns the secant of an angle

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SEC(", *args, ")", **kwargs)``
	"""
	return Func("SEC(", *args, ")", **kwargs)

def sech(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SECH` - **Math and trigonometry:** Returns the hyperbolic secant of an angle

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SECH(", *args, ")", **kwargs)``
	"""
	return Func("SECH(", *args, ")", **kwargs)

def second(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SECOND` - **Date and time:** Converts a serial number to a second

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SECOND(", *args, ")", **kwargs)``
	"""
	return Func("SECOND(", *args, ")", **kwargs)

def sequence(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SEQUENCE` - **Math and trigonometry:** Generates a list of sequential numbers in an array, such as 1, 2, 3, 4

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SEQUENCE(", *args, ")", **kwargs)``
	"""
	return Func("SEQUENCE(", *args, ")", **kwargs)

def seriessum(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SERIESSUM` - **Math and trigonometry:** Returns the sum of a power series based on the formula

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SERIESSUM(", *args, ")", **kwargs)``
	"""
	return Func("SERIESSUM(", *args, ")", **kwargs)

def sheet(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SHEET` - **Information:** Returns the sheet number of the referenced sheet

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SHEET(", *args, ")", **kwargs)``
	"""
	return Func("SHEET(", *args, ")", **kwargs)

def sheets(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SHEETS` - **Information:** Returns the number of sheets in a reference

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SHEETS(", *args, ")", **kwargs)``
	"""
	return Func("SHEETS(", *args, ")", **kwargs)

def sign(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SIGN` - **Math and trigonometry:** Returns the sign of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SIGN(", *args, ")", **kwargs)``
	"""
	return Func("SIGN(", *args, ")", **kwargs)

def sin(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SIN` - **Math and trigonometry:** Returns the sine of the given angle

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SIN(", *args, ")", **kwargs)``
	"""
	return Func("SIN(", *args, ")", **kwargs)

def sinh(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SINH` - **Math and trigonometry:** Returns the hyperbolic sine of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SINH(", *args, ")", **kwargs)``
	"""
	return Func("SINH(", *args, ")", **kwargs)

def skew(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SKEW` - **Statistical:** Returns the skewness of a distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SKEW(", *args, ")", **kwargs)``
	"""
	return Func("SKEW(", *args, ")", **kwargs)

def skew_p(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SKEW.P` - **Statistical:** Returns the skewness of a distribution based on a population: a characterization of the degree of asymmetry of a distribution around its mean

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SKEW.P(", *args, ")", **kwargs)``
	"""
	return Func("SKEW.P(", *args, ")", **kwargs)

def sln(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SLN` - **Financial:** Returns the straight-line depreciation of an asset for one period

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SLN(", *args, ")", **kwargs)``
	"""
	return Func("SLN(", *args, ")", **kwargs)

def slope(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SLOPE` - **Statistical:** Returns the slope of the linear regression line

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SLOPE(", *args, ")", **kwargs)``
	"""
	return Func("SLOPE(", *args, ")", **kwargs)

def small(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SMALL` - **Statistical:** Returns the k-th smallest value in a data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SMALL(", *args, ")", **kwargs)``
	"""
	return Func("SMALL(", *args, ")", **kwargs)

def sort(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SORT` - **Lookup and reference:** Sorts the contents of a range or array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SORT(", *args, ")", **kwargs)``
	"""
	return Func("SORT(", *args, ")", **kwargs)

def sortby(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SORTBY` - **Lookup and reference:** Sorts the contents of a range or array based on the values in a corresponding range or array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SORTBY(", *args, ")", **kwargs)``
	"""
	return Func("SORTBY(", *args, ")", **kwargs)

def sqrt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SQRT` - **Math and trigonometry:** Returns a positive square root

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SQRT(", *args, ")", **kwargs)``
	"""
	return Func("SQRT(", *args, ")", **kwargs)

def sqrtpi(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SQRTPI` - **Math and trigonometry:** Returns the square root of (number * pi)

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SQRTPI(", *args, ")", **kwargs)``
	"""
	return Func("SQRTPI(", *args, ")", **kwargs)

def standardize(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`STANDARDIZE` - **Statistical:** Returns a normalized value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("STANDARDIZE(", *args, ")", **kwargs)``
	"""
	return Func("STANDARDIZE(", *args, ")", **kwargs)

def stockhistory(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`STOCKHISTORY` - **Financial:** Retrieves historical data about a financial instrument

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("STOCKHISTORY(", *args, ")", **kwargs)``
	"""
	return Func("STOCKHISTORY(", *args, ")", **kwargs)

def stdev(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`STDEV` - **Compatibility:** Estimates standard deviation based on a sample

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("STDEV(", *args, ")", **kwargs)``
	"""
	return Func("STDEV(", *args, ")", **kwargs)

def stdev_p(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`STDEV.P` - **Statistical:** Calculates standard deviation based on the entire population

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("STDEV.P(", *args, ")", **kwargs)``
	"""
	return Func("STDEV.P(", *args, ")", **kwargs)

def stdev_s(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`STDEV.S` - **Statistical:** Estimates standard deviation based on a sample

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("STDEV.S(", *args, ")", **kwargs)``
	"""
	return Func("STDEV.S(", *args, ")", **kwargs)

def stdeva(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`STDEVA` - **Statistical:** Estimates standard deviation based on a sample, including numbers, text, and logical values

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("STDEVA(", *args, ")", **kwargs)``
	"""
	return Func("STDEVA(", *args, ")", **kwargs)

def stdevp(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`STDEVP` - **Compatibility:** Calculates standard deviation based on the entire population

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("STDEVP(", *args, ")", **kwargs)``
	"""
	return Func("STDEVP(", *args, ")", **kwargs)

def stdevpa(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`STDEVPA` - **Statistical:** Calculates standard deviation based on the entire population, including numbers, text, and logical values

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("STDEVPA(", *args, ")", **kwargs)``
	"""
	return Func("STDEVPA(", *args, ")", **kwargs)

def steyx(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`STEYX` - **Statistical:** Returns the standard error of the predicted y-value for each x in the regression

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("STEYX(", *args, ")", **kwargs)``
	"""
	return Func("STEYX(", *args, ")", **kwargs)

def substitute(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SUBSTITUTE` - **Text:** Substitutes new text for old text in a text string

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SUBSTITUTE(", *args, ")", **kwargs)``
	"""
	return Func("SUBSTITUTE(", *args, ")", **kwargs)

def subtotal(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SUBTOTAL` - **Math and trigonometry:** Returns a subtotal in a list or database

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SUBTOTAL(", *args, ")", **kwargs)``
	"""
	return Func("SUBTOTAL(", *args, ")", **kwargs)

def sum(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SUM` - **Math and trigonometry:** Adds its arguments

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SUM(", *args, ")", **kwargs)``
	"""
	return Func("SUM(", *args, ")", **kwargs)

def sumif(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SUMIF` - **Math and trigonometry:** Adds the cells specified by a given criteria

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SUMIF(", *args, ")", **kwargs)``
	"""
	return Func("SUMIF(", *args, ")", **kwargs)

def sumifs(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SUMIFS` - **Math and trigonometry:** Adds the cells in a range that meet multiple criteria

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SUMIFS(", *args, ")", **kwargs)``
	"""
	return Func("SUMIFS(", *args, ")", **kwargs)

def sumproduct(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SUMPRODUCT` - **Math and trigonometry:** Returns the sum of the products of corresponding array components

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SUMPRODUCT(", *args, ")", **kwargs)``
	"""
	return Func("SUMPRODUCT(", *args, ")", **kwargs)

def sumsq(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SUMSQ` - **Math and trigonometry:** Returns the sum of the squares of the arguments

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SUMSQ(", *args, ")", **kwargs)``
	"""
	return Func("SUMSQ(", *args, ")", **kwargs)

def sumx2my2(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SUMX2MY2` - **Math and trigonometry:** Returns the sum of the difference of squares of corresponding values in two arrays

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SUMX2MY2(", *args, ")", **kwargs)``
	"""
	return Func("SUMX2MY2(", *args, ")", **kwargs)

def sumx2py2(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SUMX2PY2` - **Math and trigonometry:** Returns the sum of the sum of squares of corresponding values in two arrays

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SUMX2PY2(", *args, ")", **kwargs)``
	"""
	return Func("SUMX2PY2(", *args, ")", **kwargs)

def sumxmy2(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SUMXMY2` - **Math and trigonometry:** Returns the sum of squares of differences of corresponding values in two arrays

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SUMXMY2(", *args, ")", **kwargs)``
	"""
	return Func("SUMXMY2(", *args, ")", **kwargs)

def switch(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SWITCH` - **Logical:** Evaluates an expression against a list of values and returns the result corresponding to the first matching value. If there is no match, an optional default value may be returned.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SWITCH(", *args, ")", **kwargs)``
	"""
	return Func("SWITCH(", *args, ")", **kwargs)

def syd(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`SYD` - **Financial:** Returns the sum-of-years' digits depreciation of an asset for a specified period

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("SYD(", *args, ")", **kwargs)``
	"""
	return Func("SYD(", *args, ")", **kwargs)

def t(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`T` - **Text:** Converts its arguments to text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("T(", *args, ")", **kwargs)``
	"""
	return Func("T(", *args, ")", **kwargs)

def tan(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TAN` - **Math and trigonometry:** Returns the tangent of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TAN(", *args, ")", **kwargs)``
	"""
	return Func("TAN(", *args, ")", **kwargs)

def tanh(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TANH` - **Math and trigonometry:** Returns the hyperbolic tangent of a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TANH(", *args, ")", **kwargs)``
	"""
	return Func("TANH(", *args, ")", **kwargs)

def take(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TAKE` - **Lookup and reference:** Returns a specified number of contiguous rows or columns from the start or end of an array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TAKE(", *args, ")", **kwargs)``
	"""
	return Func("TAKE(", *args, ")", **kwargs)

def tbilleq(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TBILLEQ` - **Financial:** Returns the bond-equivalent yield for a Treasury bill

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TBILLEQ(", *args, ")", **kwargs)``
	"""
	return Func("TBILLEQ(", *args, ")", **kwargs)

def tbillprice(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TBILLPRICE` - **Financial:** Returns the price per $100 face value for a Treasury bill

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TBILLPRICE(", *args, ")", **kwargs)``
	"""
	return Func("TBILLPRICE(", *args, ")", **kwargs)

def tbillyield(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TBILLYIELD` - **Financial:** Returns the yield for a Treasury bill

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TBILLYIELD(", *args, ")", **kwargs)``
	"""
	return Func("TBILLYIELD(", *args, ")", **kwargs)

def t_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`T.DIST` - **Statistical:** Returns the Percentage Points (probability) for the Student t-distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("T.DIST(", *args, ")", **kwargs)``
	"""
	return Func("T.DIST(", *args, ")", **kwargs)

def t_dist_2t(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`T.DIST.2T` - **Statistical:** Returns the Percentage Points (probability) for the Student t-distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("T.DIST.2T(", *args, ")", **kwargs)``
	"""
	return Func("T.DIST.2T(", *args, ")", **kwargs)

def t_dist_rt(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`T.DIST.RT` - **Statistical:** Returns the Student's t-distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("T.DIST.RT(", *args, ")", **kwargs)``
	"""
	return Func("T.DIST.RT(", *args, ")", **kwargs)

def tdist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TDIST` - **Compatibility:** Returns the Student's t-distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TDIST(", *args, ")", **kwargs)``
	"""
	return Func("TDIST(", *args, ")", **kwargs)

def text(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TEXT` - **Text:** Formats a number and converts it to text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TEXT(", *args, ")", **kwargs)``
	"""
	return Func("TEXT(", *args, ")", **kwargs)

def textafter(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TEXTAFTER` - **Text:** Returns text that occurs after given character or string

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TEXTAFTER(", *args, ")", **kwargs)``
	"""
	return Func("TEXTAFTER(", *args, ")", **kwargs)

def textbefore(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TEXTBEFORE` - **Text:** Returns text that occurs before a given character or string

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TEXTBEFORE(", *args, ")", **kwargs)``
	"""
	return Func("TEXTBEFORE(", *args, ")", **kwargs)

def textjoin(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TEXTJOIN` - **Text:** Combines the text from multiple ranges and/or strings

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TEXTJOIN(", *args, ")", **kwargs)``
	"""
	return Func("TEXTJOIN(", *args, ")", **kwargs)

def textsplit(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TEXTSPLIT` - **Text:** Splits text strings by using column and row delimiters

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TEXTSPLIT(", *args, ")", **kwargs)``
	"""
	return Func("TEXTSPLIT(", *args, ")", **kwargs)

def time(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TIME` - **Date and time:** Returns the serial number of a particular time

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TIME(", *args, ")", **kwargs)``
	"""
	return Func("TIME(", *args, ")", **kwargs)

def timevalue(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TIMEVALUE` - **Date and time:** Converts a time in the form of text to a serial number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TIMEVALUE(", *args, ")", **kwargs)``
	"""
	return Func("TIMEVALUE(", *args, ")", **kwargs)

def t_inv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`T.INV` - **Statistical:** Returns the t-value of the Student's t-distribution as a function of the probability and the degrees of freedom

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("T.INV(", *args, ")", **kwargs)``
	"""
	return Func("T.INV(", *args, ")", **kwargs)

def t_inv_2t(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`T.INV.2T` - **Statistical:** Returns the inverse of the Student's t-distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("T.INV.2T(", *args, ")", **kwargs)``
	"""
	return Func("T.INV.2T(", *args, ")", **kwargs)

def tinv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TINV` - **Compatibility:** Returns the inverse of the Student's t-distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TINV(", *args, ")", **kwargs)``
	"""
	return Func("TINV(", *args, ")", **kwargs)

def tocol(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TOCOL` - **Lookup and reference:** Returns the array in a single column

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TOCOL(", *args, ")", **kwargs)``
	"""
	return Func("TOCOL(", *args, ")", **kwargs)

def torow(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TOROW` - **Lookup and reference:** Returns the array in a single row

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TOROW(", *args, ")", **kwargs)``
	"""
	return Func("TOROW(", *args, ")", **kwargs)

def today(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TODAY` - **Date and time:** Returns the serial number of today's date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TODAY(", *args, ")", **kwargs)``
	"""
	return Func("TODAY(", *args, ")", **kwargs)

def transpose(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TRANSPOSE` - **Lookup and reference:** Returns the transpose of an array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TRANSPOSE(", *args, ")", **kwargs)``
	"""
	return Func("TRANSPOSE(", *args, ")", **kwargs)

def trend(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TREND` - **Statistical:** Returns values along a linear trend

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TREND(", *args, ")", **kwargs)``
	"""
	return Func("TREND(", *args, ")", **kwargs)

def trim(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TRIM` - **Text:** Removes spaces from text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TRIM(", *args, ")", **kwargs)``
	"""
	return Func("TRIM(", *args, ")", **kwargs)

def trimmean(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TRIMMEAN` - **Statistical:** Returns the mean of the interior of a data set

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TRIMMEAN(", *args, ")", **kwargs)``
	"""
	return Func("TRIMMEAN(", *args, ")", **kwargs)

def true(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TRUE` - **Logical:** Returns the logical value TRUE

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TRUE(", *args, ")", **kwargs)``
	"""
	return Func("TRUE(", *args, ")", **kwargs)

def trunc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TRUNC` - **Math and trigonometry:** Truncates a number to an integer

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TRUNC(", *args, ")", **kwargs)``
	"""
	return Func("TRUNC(", *args, ")", **kwargs)

def t_test(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`T.TEST` - **Statistical:** Returns the probability associated with a Student's t-test

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("T.TEST(", *args, ")", **kwargs)``
	"""
	return Func("T.TEST(", *args, ")", **kwargs)

def ttest(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TTEST` - **Compatibility:** Returns the probability associated with a Student's t-test

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TTEST(", *args, ")", **kwargs)``
	"""
	return Func("TTEST(", *args, ")", **kwargs)

def type(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`TYPE` - **Information:** Returns a number indicating the data type of a value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("TYPE(", *args, ")", **kwargs)``
	"""
	return Func("TYPE(", *args, ")", **kwargs)

def unichar(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`UNICHAR` - **Text:** Returns the Unicode character that is references by the given numeric value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("UNICHAR(", *args, ")", **kwargs)``
	"""
	return Func("UNICHAR(", *args, ")", **kwargs)

def unicode(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`UNICODE` - **Text:** Returns the number (code point) that corresponds to the first character of the text

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("UNICODE(", *args, ")", **kwargs)``
	"""
	return Func("UNICODE(", *args, ")", **kwargs)

def unique(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`UNIQUE` - **Lookup and reference:** Returns a list of unique values in a list or range

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("UNIQUE(", *args, ")", **kwargs)``
	"""
	return Func("UNIQUE(", *args, ")", **kwargs)

def upper(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`UPPER` - **Text:** Converts text to uppercase

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("UPPER(", *args, ")", **kwargs)``
	"""
	return Func("UPPER(", *args, ")", **kwargs)

def value(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VALUE` - **Text:** Converts a text argument to a number

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VALUE(", *args, ")", **kwargs)``
	"""
	return Func("VALUE(", *args, ")", **kwargs)

def valuetotext(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VALUETOTEXT` - **Text:** Returns text from any specified value

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VALUETOTEXT(", *args, ")", **kwargs)``
	"""
	return Func("VALUETOTEXT(", *args, ")", **kwargs)

def var(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VAR` - **Compatibility:** Estimates variance based on a sample

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VAR(", *args, ")", **kwargs)``
	"""
	return Func("VAR(", *args, ")", **kwargs)

def var_p(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VAR.P` - **Statistical:** Calculates variance based on the entire population

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VAR.P(", *args, ")", **kwargs)``
	"""
	return Func("VAR.P(", *args, ")", **kwargs)

def var_s(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VAR.S` - **Statistical:** Estimates variance based on a sample

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VAR.S(", *args, ")", **kwargs)``
	"""
	return Func("VAR.S(", *args, ")", **kwargs)

def vara(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VARA` - **Statistical:** Estimates variance based on a sample, including numbers, text, and logical values

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VARA(", *args, ")", **kwargs)``
	"""
	return Func("VARA(", *args, ")", **kwargs)

def varp(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VARP` - **Compatibility:** Calculates variance based on the entire population

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VARP(", *args, ")", **kwargs)``
	"""
	return Func("VARP(", *args, ")", **kwargs)

def varpa(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VARPA` - **Statistical:** Calculates variance based on the entire population, including numbers, text, and logical values

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VARPA(", *args, ")", **kwargs)``
	"""
	return Func("VARPA(", *args, ")", **kwargs)

def vdb(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VDB` - **Financial:** Returns the depreciation of an asset for a specified or partial period by using a declining balance method

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VDB(", *args, ")", **kwargs)``
	"""
	return Func("VDB(", *args, ")", **kwargs)

def vlookup(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VLOOKUP` - **Lookup and reference:** Looks in the first column of an array and moves across the row to return the value of a cell

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VLOOKUP(", *args, ")", **kwargs)``
	"""
	return Func("VLOOKUP(", *args, ")", **kwargs)

def vstack(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`VSTACK` - **Look and reference:** Appends arrays vertically and in sequence to return a larger array

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("VSTACK(", *args, ")", **kwargs)``
	"""
	return Func("VSTACK(", *args, ")", **kwargs)

def webservice(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`WEBSERVICE` - **Web:** Returns data from a web service.

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("WEBSERVICE(", *args, ")", **kwargs)``
	"""
	return Func("WEBSERVICE(", *args, ")", **kwargs)

def weekday(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`WEEKDAY` - **Date and time:** Converts a serial number to a day of the week

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("WEEKDAY(", *args, ")", **kwargs)``
	"""
	return Func("WEEKDAY(", *args, ")", **kwargs)

def weeknum(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`WEEKNUM` - **Date and time:** Converts a serial number to a number representing where the week falls numerically with a year

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("WEEKNUM(", *args, ")", **kwargs)``
	"""
	return Func("WEEKNUM(", *args, ")", **kwargs)

def weibull(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`WEIBULL` - **Compatibility:** Calculates variance based on the entire population, including numbers, text, and logical values

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("WEIBULL(", *args, ")", **kwargs)``
	"""
	return Func("WEIBULL(", *args, ")", **kwargs)

def weibull_dist(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`WEIBULL.DIST` - **Statistical:** Returns the Weibull distribution

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("WEIBULL.DIST(", *args, ")", **kwargs)``
	"""
	return Func("WEIBULL.DIST(", *args, ")", **kwargs)

def workday(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`WORKDAY` - **Date and time:** Returns the serial number of the date before or after a specified number of workdays

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("WORKDAY(", *args, ")", **kwargs)``
	"""
	return Func("WORKDAY(", *args, ")", **kwargs)

def workday_intl(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`WORKDAY.INTL` - **Date and time:** Returns the serial number of the date before or after a specified number of workdays using parameters to indicate which and how many days are weekend days

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("WORKDAY.INTL(", *args, ")", **kwargs)``
	"""
	return Func("WORKDAY.INTL(", *args, ")", **kwargs)

def wrapcols(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`WRAPCOLS` - **Look and reference:** Wraps the provided row or column of values by columns after a specified number of elements

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("WRAPCOLS(", *args, ")", **kwargs)``
	"""
	return Func("WRAPCOLS(", *args, ")", **kwargs)

def wraprows(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`WRAPROWS` - **Look and reference:** Wraps the provided row or column of values by rows after a specified number of elements

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("WRAPROWS(", *args, ")", **kwargs)``
	"""
	return Func("WRAPROWS(", *args, ")", **kwargs)

def xirr(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`XIRR` - **Financial:** Returns the internal rate of return for a schedule of cash flows that is not necessarily periodic

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("XIRR(", *args, ")", **kwargs)``
	"""
	return Func("XIRR(", *args, ")", **kwargs)

def xlookup(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`XLOOKUP` - **Lookup and reference:** Searches a range or an array, and returns an item corresponding to the first match it finds. If a match doesn't exist, then XLOOKUP can return the closest (approximate) match. 

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("XLOOKUP(", *args, ")", **kwargs)``
	"""
	return Func("XLOOKUP(", *args, ")", **kwargs)

def xmatch(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`XMATCH` - **Lookup and reference:** Returns the relative position of an item in an array or range of cells. 

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("XMATCH(", *args, ")", **kwargs)``
	"""
	return Func("XMATCH(", *args, ")", **kwargs)

def xnpv(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`XNPV` - **Financial:** Returns the net present value for a schedule of cash flows that is not necessarily periodic

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("XNPV(", *args, ")", **kwargs)``
	"""
	return Func("XNPV(", *args, ")", **kwargs)

def xor(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`XOR` - **Logical:** Returns a logical exclusive OR of all arguments

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("XOR(", *args, ")", **kwargs)``
	"""
	return Func("XOR(", *args, ")", **kwargs)

def year(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`YEAR` - **Date and time:** Converts a serial number to a year

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("YEAR(", *args, ")", **kwargs)``
	"""
	return Func("YEAR(", *args, ")", **kwargs)

def yearfrac(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`YEARFRAC` - **Date and time:** Returns the year fraction representing the number of whole days between start_date and end_date

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("YEARFRAC(", *args, ")", **kwargs)``
	"""
	return Func("YEARFRAC(", *args, ")", **kwargs)

def yield(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`YIELD` - **Financial:** Returns the yield on a security that pays periodic interest

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("YIELD(", *args, ")", **kwargs)``
	"""
	return Func("YIELD(", *args, ")", **kwargs)

def yielddisc(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`YIELDDISC` - **Financial:** Returns the annual yield for a discounted security; for example, a Treasury bill

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("YIELDDISC(", *args, ")", **kwargs)``
	"""
	return Func("YIELDDISC(", *args, ")", **kwargs)

def yieldmat(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`YIELDMAT` - **Financial:** Returns the annual yield of a security that pays interest at maturity

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("YIELDMAT(", *args, ")", **kwargs)``
	"""
	return Func("YIELDMAT(", *args, ")", **kwargs)

def z_test(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`Z.TEST` - **Statistical:** Returns the one-tailed probability-value of a z-test

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("Z.TEST(", *args, ")", **kwargs)``
	"""
	return Func("Z.TEST(", *args, ")", **kwargs)

def ztest(*args: Any, **kwargs: Any) -> Func:
	"""
	:meth:`ZTEST` - **Compatibility:** Returns the one-tailed probability-value of a z-test

	Returns
	-------
	:class:`Func <excelbird.func>`
		Equivalent to ``Func("ZTEST(", *args, ")", **kwargs)``
	"""
	return Func("ZTEST(", *args, ")", **kwargs)


