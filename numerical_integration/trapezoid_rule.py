import numpy as np
def trapezoidalIntegration(f,a,b, m=1):
	x = np.linspace(a,b,m)
	return ((b-a)/2*m)*np.sum([f(x[k])+f(x[k+1]) for k in range(len(x))])

