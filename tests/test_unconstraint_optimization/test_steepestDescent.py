from decimal import DivisionByZero
import os, sys, pytest
from numpy import minimum
sys.path.insert(1, os.getcwd())

from unconstrained_optimization import steepestDescent

def test_RScalarFunction():
	f = lambda X: X[0]**2 + X[1]**2
	Df = lambda X: [2*X[0], 2*X[1]]
	x_n = [10,25]

	min_x, min_y = steepestDescent(x_n, Df, f)

	assert 0.0 == round(min_x[0],1)  and 0.0 == round(min_x[1],1)  and 0.0 == round(min_y,1)

def test_RNscalarFunction():
	f = lambda x: x**2
	df = lambda x: 2*x
	x_n = 10

	min_x, min_y = steepestDescent(x_n, df, f)
	
	assert 0.0 == round(min_x, 1) and 0.0 == round(min_y)

