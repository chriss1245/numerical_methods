import numpy as np

def secantMethod(x_0, x_1, f, tolerance):
	"""
	Applies the secant method for rootfinding of non-linear equations
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
	if not any(map(lambda x: isinstance(x_0, x), [int, float])):
		raise ValueError(f'x_0: {x_0} is not a valid input')
	
	if not any(map(lambda x: isinstance(x_1, x), [int, float])):
		raise ValueError(f'x_1: {x_1} is not a valid input')

	if not any(map(lambda x: isinstance(tolerance, x), [int, float])):
		raise ValueError(f'tolerance: {tolerance} is not a valid input')

	if not callable(f):
		raise ValueError('f is not a function')

	x_l = x_0 # x_{n-2}
	x_m = x_1 # x_{n-1}
	error = np.Inf
	while error > tolerance:
		x_n = x_m - f(x_m)*(x_m-x_l)/(f(x_m)-f(x_l))
		x_l = x_m
		x_m = x_n
		error = abs(f(x_n))
	return x_n