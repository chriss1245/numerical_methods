import numpy as np
def midpointIntegration(f, a, b, m):
	"""
	Takes a function and returns its definite integral betwen two points a and b with a stepsize m
	using midpoint rule
	More info: https://en.wikipedia.org/wiki/Riemann_sum
	
	Args:
	-------------------------------
	f: Funtion we want to integrate
	a: lower bound
	b: upper bound
	m: stepsize

	Returns:
	-------------------------------
	Integral of f evaluated 
	"""
	return ((b-a)/m)*np.sum([f(x_k) for x_k in np.linspace(a,b,m)])

