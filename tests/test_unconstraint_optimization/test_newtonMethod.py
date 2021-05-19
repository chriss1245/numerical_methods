import os, sys, pytest
sys.path.insert(1, os.getcwd())
from unconstrained_optimization import newtonOptimization

def test_RNScalarFunction():
	f = lambda X: X[0]**2 + X[1]**2
	Df = lambda X: [2*X[0], 2*X[1]]
	Hf = lambda X: [[2,0],[0,2]]
	x_n = [10,25]

	min_x = newtonOptimization(x_n, f, Df, Hf)

	assert 0.0 == round(min_x[0],1) == round(min_x[1],1)

def test_RScalarFunction():
	f = lambda x: x**2
	df = lambda x: 2*x
	Hf = lambda x: 2
	x_n = 10

	min_x = newtonOptimization(x_n, f, df, Hf)
	
	assert 0.0 == round(min_x, 1)
