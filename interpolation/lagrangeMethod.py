import os, sys
sys.path.insert(1, os.getcwd())
from assets import Polynomial
import numpy as np

def nodalPolynomial(X,i):
	P = Polynomial(1)
	j = 0
	while j < len(X):
		if j != i:
			P *= Polynomial(-X[j], 1)*(1/(X[i]-X[j]))
		j +=1
	
	return P

def lagrangeMethod(X,Y):
	"""
	Interpolates using the lagrange method. 
	The points do not need to be equispaced

	Args:
	-------------------------------------
	X: list containing the x points
	Y: list containing the f(x) points

	Returns:
	--------------------------------------
	A object type Polynomial
	"""
	P = Polynomial(0)
	n = len(X)
	i = 0
	while i < n:
		P += nodalPolynomial(X, i)*Y[i]
		i+=1
		
	return P