import numpy as np
# Exactly eulers method
def zeroOrderAdamsBasforth(f, x_0, F_0, x_n, N):
	h = (x_n-x_0)/2
	F = [F_0] # One initial given point
	for i in range(N):
		# F_{i+1} = F_{i} +h*f(x_{i+1}, F_{i})
		F.append(F[i]+h*f(x_0+h*i, F[i])) 
	return np.array(F)

def fisrtOrderAdamsBasfoth(f, x_0, F_0, x_n, N):
	h = (x_n-x_0)/2
	F=[F_0, F_0 + h*f(x_0+h, F_0)] # Two initial points, calculated by euler, not the best approach

	for i in range(1,N):

		# F_{i+1} = F_{i} + 0.5*h*(3*F_{i}-F_{i-1})
		F_j = F[i] + 0.5*h*(3*f(x_0+i*h, F[i])-f(x_0+(i-1)*h, F[i-1]))
		F.append(F_j)
	return np.array(F)

