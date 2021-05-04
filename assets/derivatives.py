def derivative(f, x_0, h=0.000001):
	"""
	Applies the second order central Difference for the approximation of the derivative

	Args:
	------------
	f: Function we want to get the derivative from
	x_0: point
	h: the discretization stepsize
	"""
	return (f(x_0+h)-f(x_0-h))/(2*h)