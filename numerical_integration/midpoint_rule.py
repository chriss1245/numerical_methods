import numpy as np
def midpointIntegration(f, a, b, m):
	return ((b-a)/m)*np.sum([f(x_k) for x_k in np.linspace(a,b,m)])

