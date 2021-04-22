import numpy as np

def biesctionMethod(a_0, b_0, f, tolerance):
	"""
	The function applies the chord  or bisection method for rootfinding
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
	if f(a_0)*f(b_0) > 0:
		print('Error: insert values such that f(a_0)*f(b_0) < 0')
		return None

	a_n = a_0
	b_n = b_0
	error = np.Inf
	while error > tolerance:
		c_n = 0.5*(a_n+b_n)
		
		if f(c_n) < 0:
			a_n = c_n
		else:
			b_n = c_n
		
		error = np.abs(f(c_n))

	return c_n

#-------------------------------------------------------------------------------------------
#Testing
f = lambda x: x**3+3
a0 = -9
b0 = 3
tol = 0.001
print("Method's root:", biesctionMethod(a0, b0, f, tol), "Actual root:", -3**(1/3))
