import sys, os, pytest 
import numpy as np
sys.path.insert(1, os.getcwd())
from unconstrained_optimization import lineSearch



def test_scalar_function():
	f = lambda x: x**2
	
	# X = 1
	x_n = 1
	d_n = -2
	# if tje direction is -2 and we are in 
	assert round(lineSearch(f, x_n, d_n),1) == 0.5
	# x = 0
	x_n = 0
	d_n = 0
	assert round(lineSearch(f, x_n, d_n),0) == 0
	# x = 2
	x_n = 2
	d_n = -4
	assert round(lineSearch(f, x_n, d_n), 1) == 0.5



def test_vector_function():
	f = lambda X: X[0]**2 + X[1]**2

	x_n = 1
	d_n = np.array([-2.,-2.])
	assert round(lineSearch(f, x_n, d_n),1) == 0.5

	x_n = 0
	d_n = np.array([0,0])
	assert round(lineSearch(f, x_n, d_n),0) == 0

	x_n = 2
	d_n = np.array([-4.0,-4.0])
	assert round(lineSearch(f, x_n, d_n),1) == 0.5