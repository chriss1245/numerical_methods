import os, sys
sys.path.insert(1, os.getcwd())
from assets import Polynomial

import numpy as np

def linearMethod(X, Y):
	"""
	This method tries to solve a matrix equation Ax=b where x are the coefficients
	of the polynomial P(x) = ax^4+bx^3... (this is an example, works with any number of points)

	Args:
	------------------------------------------
	X: list of points in the x axis
	Y: list of points in the y axis
	
	Returns:
	------------------------------------------
	Polynomial which interpolates all the lines
	"""
	n = len(X)
	A = [] 
	b = []
	for i in range(n):
		row = [X[i]**j for j in range(n)] # [a (x^0), b (x^1)] coefficients of the ith equation given by the ith point
		b.append(Y[i])
		A.append(row)

	A = np.matrix(A)
	b = np.matrix(b).T

	x = np.linalg.solve(A,b)

	x = np.squeeze(np.asarray(x)).tolist()
	
	return Polynomial(*x)
