import numpy as np
import sys, os
sys.path.insert(1, os.getcwd)
from .lineSearch import lineSearch
from assets import checkType



def newtonOptimization(x_n, f, Df, Hf, convergence_threshold = 0.0001):
	"""
	Returns a minimun of f using the newton method https://en.wikipedia.org/wiki/Method_of_steepest_descent
	
	Args:
	------------------------------------
	x_n: point form which we want to start
	Df: derivative of f 
	f: target function
	Hf: hessian of f
	convergence_threshold: maximun variation in the minimun in order to return a solution

	Returns:
	------------------------------------
	x_n: such that minimizes f
	"""
	# Rises an Exception if x_n is not one of these types
	checkType(x_n, int, float, np.ndarray, list, tuple)

	# Direction
	# One dimensional case:
	if any(map(lambda t: isinstance(x_n,t), [int, float])):
		d = lambda x_n: -f(x_n)/Hf(x_n)
	# N dimensional case:
	else:
		d = lambda x_n: -np.linalg.solve(Hf(x_n), Df(x_n))

	current_min = np.Inf
	while True:
		new_min = f(x_n)

		# Checking convergence and that the minimun be non increasing
		if current_min < new_min or abs(current_min - new_min) < convergence_threshold:
			return x_n
		
		d_n = d(x_n)
		alpha = lineSearch(f, x_n, d_n)
		x_n	+= alpha*d_n
		current_min = new_min