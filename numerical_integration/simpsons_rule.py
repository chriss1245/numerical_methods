import numpy as np
def simpsonIntegration(f, a, b, m) -> float :
	"""
	Takes a function and returns its definite integral betwen two points a and b with a stepsize m
	using simpsons one third rule.
	More info: https://en.wikipedia.org/wiki/Simpson%27s_rule
	
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
	x = np.linspace(a,b,m)
	scaled_h = (b-a)/(3*m)
	evenPart= 2*np.sum([f(x[k]) for k in range(2,len(x)//2, 2)])
	oddPart = 4*np.sum([f(x[k]) for k in range(1, len(x)//2,2)])
	return scaled_h*(f(x[0])+f(x[-1]) + evenPart + oddPart)
