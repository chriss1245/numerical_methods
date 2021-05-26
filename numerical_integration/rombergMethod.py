import numpy as np
def rombergIntegration(f, a, b, m):
	h = lambda n: (b-a)/(2**(n+1))

	A = [_trapezoid(f,a,b,h(k)) for k in range(m)]

	return _rombergRecursive(A, 1)

	for i in range(m-1):
		A.append(A[0])


def _trapezoid(f,a,b,m):
	x = np.linspace(a,b, m)
	return ((a-b)/(2*m))*np.sum([f(x[i])+f(x[i+1]) for i in range(m-1)])

def _rombergRecursive(A,k):
	if len(A) == 2:
		return ((4**k)*A[1]-A[0])/((4**k)-1)

	return _rombergRecursive([((4**k)*A[i]-A[i-1])/((4**k)-1) for i in range(len(A)-1,-1, 1)], k+1)