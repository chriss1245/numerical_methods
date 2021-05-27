import numpy as np

def secondOrderRK(f,x_0, y_0, x_n, h):
	N = len(np.arange(x_0, x_n, h))
	Y = [y_0]

	for n in range(N):
		k1 = f(x_0 + h*n, Y[n])
		k2 = f(x_0+h*(n+1), Y[n]+h*k1)
		Y.append(Y[n]+ 0.5*h*(k1+k2))
		
	return Y