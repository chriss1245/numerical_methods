
def chordMethod(x_0, x_1, f, tolerance):
	"""
	Applies the chord method for rootfinding of non-linear equations
	It is simmilar to the bisection method.. but we do not change the slope at the iterations
	More info: https://en.wikipedia.org/wiki/Secant_method

	Args:
	-----------------------------------------------------------------------
	x_0: initial point
	x_1: another initial point
	f: function
	tolerance: the maximun value that abs(f(x_n)) can take in order to have a valid solution

	Returns:
	------------------------------------------------------------------------
	x_n a point such that abs(f(x_n))<tolerance
	"""

	# Checking input type
	if not any(map(lambda x: isinstance(x_0, x), [int, float])):
		raise ValueError(f'x_0: {x_0} is not a valid input')
	
	if not any(map(lambda x: isinstance(x_1, x), [int, float])):
		raise ValueError(f'x_1: {x_1} is not a valid input')

	if not any(map(lambda x: isinstance(tolerance, x), [int, float])):
		raise ValueError(f'tolerance: {tolerance} is not a valid input')

	if not callable(f):
		raise ValueError('f is not a function')

	# Checking the slope is not 0
	if f(x_1)-f(x_0) == 0:
		raise ZeroDivisionError('The slope is 0')

	# Calling the chord method
	m_ = (x_1-x_0)/(f(x_1)-f(x_0))
	return _chordMethod(x_1, m_, f, tolerance)

def _chordMethod(x_m, m_, f, tolerance):
	x_n = x_m - m_*f(x_m)

	# Base case
	if abs(f(x_n)) < tolerance:
		return x_n
	
	# Recursive case
	return _chordMethod(x_n, m_, f, tolerance)