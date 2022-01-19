def richardsonDerivative(f, x, h,δ, order):
	"""
	Computes the an approximation of the derivative following the finite difereces method of order
	and stepsize given.
	
	-----------------------------------------------------------------------------------------------
	Args
	f: callable
	x: point to be evaluated
	h: precision
	δ: scaler of h
	
	-----------------------------------------------------------------------------------------------
	Returns the derivative of f evaluated at x
	
	"""
	A = [(f((δ**k)*h + x)-f(x))/(δ*h) for k in range(order)]
	return finiteDiferences(A, δ, 1)


def finiteDiferences(A, δ, k):
	if len(A) == 2:
		return (A[1]-(δ**k)*A[0])/(1-δ**k)
	
	return finiteDiferences([(A[i]-(δ**k)*A[i-1])/(1-δ**k) for i in range(len(A)-1,0,-1)], δ, k+1)
