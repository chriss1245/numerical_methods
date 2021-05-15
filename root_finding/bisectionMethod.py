
def bisectionMethod(a_0, b_0, f, tolerance=0.001):
	"""
	The function applies the method for rootfinding
	More info: https://en.wikipedia.org/wiki/Bisection_method

	Args:
	-------------------------------------------------------
	a_0: point such that f(a_0) < 0
	b_0: point such that f(b_0) > 0
	f: function we want to find the root from
	tolerance: maximun value f(c_n) has.

	Returns:
	-------------------------------------------------------
	c_n: the root of the function
	"""

	# Exceptions handler
	if not any(map(lambda x: isinstance(a_0, x), [int, float])):
		raise ValueError(f'a_0: {a_0} is not a valid input')
	
	if not any(map(lambda x: isinstance(b_0, x), [int, float])):
		raise ValueError(f'b_0: {b_0} is not a valid input')

	if not any(map(lambda x: isinstance(tolerance, x), [int, float])):
		raise ValueError(f'tolerance: {tolerance} is not a valid input')

	if not callable(f):
		raise ValueError('f is not a function')

	return _bisectionMehtod(a_0, b_0, f, tolerance)


def _bisectionMehtod(a_n, b_n, f, tolerance):
	"""
	Recursive method
	"""

	#Base case
	c_n = 0.5*(a_n+b_n)
	if abs(f(c_n)) < tolerance:
		return c_n
	
	#Recursive case
	if f(c_n) < 0:
		return _bisectionMehtod(c_n, b_n, f, tolerance)
	return _bisectionMehtod(a_n, c_n, f, tolerance)
