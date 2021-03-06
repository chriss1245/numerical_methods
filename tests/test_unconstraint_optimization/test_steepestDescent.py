import os, sys, pytest
sys.path.insert(1, os.getcwd())
from unconstrained_optimization import steepestDescent

def test_RNScalarFunction():
	f = lambda X: X[0]**2 + X[1]**2
	Df = lambda X: [2*X[0], 2*X[1]]
	x_n = [10,25]

	min_x = steepestDescent(x_n, Df, f)

	assert 0.0 == round(min_x[0],1) == round(min_x[1],1)

def test_RScalarFunction():
	f = lambda x: x**2
	df = lambda x: 2*x
	x_n = 10

	min_x = steepestDescent(x_n, df, f)
	
	assert 0.0 == round(min_x, 1)

