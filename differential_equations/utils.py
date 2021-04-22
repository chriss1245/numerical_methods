"""
Auxiliar functions needed for analysis and implementetation of any method
"""

import numpy as np

# Root finding method
def secantMethod(x_0, f, tolerance=0.0001):
	"""
	Applies the secant method for rootfinding of non-linear equations

	Args:
	-----------------------------------------------------------------------
	x_0: initial point
	f: function
	tolerance: the maximun value that abs(f(x_n)) can take in order to have a valid solution

	Returns:
	------------------------------------------------------------------------
	x_n a point such that abs(f(x_n))<tolerance
	"""
	x_l = x_0-1 # x_{n-2}
	x_m = 2*x_0 + 1 # x_{n-1}
	error = np.Inf
	while error > tolerance:
		if (f(x_m)-f(x_l)) <= tolerance*0.1: 
			print('Warning: slope is 0, tolerance: ', tolerance)
			return x_m
		x_n = x_m - f(x_m)*(x_m-x_l)/(f(x_m)-f(x_l))
		x_l = x_m
		x_m = x_n
		error = abs(f(x_n))
	return x_n

#Plotting method
def analyseGraphically(method, h=0.01, N=10):
	"""
	Auxiliary funciton for comparing graphically the methods' results and the actual results
	of  the following differential equations



	Args:
	-----------------------------------------------------------------------------------------
	method: callable that solves a differential equation
	h: discretization stepsize
	N: number of steps
	"""



	pass

