"""
This is a bit advanced mnethod since I employ my knowledge about data structures and recurssion
I employ a self crafted polynomial class
I employ a function that returns the backward or forward differences of the order 0,1...n-1
I employ a funciton that returns the product of the m first polynomials
"""

import numpy as np
import math
from assets import Polynomial

def _finiteDifferences(Y, forward):
	if len(Y)==2:
		return [Y[1]-Y[0]]
	else:
		if forward:
			difference = [Y[i+1]-Y[i] for i in range(len(Y)-1)]
			return [difference[0],*_finiteDifferences(difference, forward)]
		
		difference = [Y[i]-Y[i-1] for i in range(len(Y)-1,0,-1)]
		return [difference[-1],*_finiteDifferences(difference, forward)]

def finiteDifferences(Y, forward = True):
	if len(Y)==1:
		return [1]
	else:
		return [0,*_finiteDifferences(Y, forward)]

def progressivePolynomialProduct(X):
	n = len(X)
	if n == 0:
		return 0
	P = Polynomial(1)
	for i in range(0,n):
		P = P*Polynomial(-X[i], 1)
	return P


def gregoryNewtonInterpolation(X, Y):
	"""
	This method applies the newton gregory interolation

	Args:
	------------------------
	X: set of points which are known 
	Y: set of images corresponding to the points

	Returns:
	P: a Polynomial data structure that represents the interpolation polynomial
	"""
	h = abs(X[0]-X[1])

	P = Polynomial(Y[0])
	forwardD = finiteDifferences(Y)[1:]

	for i in range(1,len(X)):
		q = progressivePolynomialProduct(X[:i])*(forwardD[i-1]/(math.factorial(i)*(h**(i))))
		P = P + q

	return P