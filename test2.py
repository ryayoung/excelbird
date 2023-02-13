







def chiinv(*args: str | Any, **kwargs: Any) -> Func:
	"""
	``CHIINV`` - **Compatibility**: Returns the inverse of the one-tailed probability of the chi-squared distribution
	"""
	return Func("CHIINV(", *args, ")", **kwargs)

def chitest(*args: str | Any, **kwargs: Any) -> Func:
	"""
	``CHITEST`` - **Compatibility**: Returns the test for independence
	"""
	return Func("CHITEST(", *args, ")", **kwargs)

def chisq_dist(*args: str | Any, **kwargs: Any) -> Func:
	"""
	``CHISQ.DIST`` - **Statistical**: Returns the cumulative beta probability density function
	"""
	return Func("CHISQ.DIST(", *args, ")", **kwargs)

def chisq_dist_rt(*args: str | Any, **kwargs: Any) -> Func:
	"""
	``CHISQ.DIST.RT`` - **Statistical**: Returns the one-tailed probability of the chi-squared distribution
	"""
	return Func("CHISQ.DIST.RT(", *args, ")", **kwargs)

