import numpy as np
def simpsonIntegration(f, a, b,m):
	x = np.linspace(a,b,m)
	return (1/3*m)*(b-a)*(f(x[0])+f(x[-1])+2*np.sum([f(x[k]) for k in range(2,len(x)/2, 2)])+4*np.sum([f(x[k] for k in range(1, len(x)/2),2)]))


