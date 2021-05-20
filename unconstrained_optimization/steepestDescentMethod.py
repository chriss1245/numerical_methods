#REMARK:The steepest descent is an special case of a quasi newton method
import numpy as np
import sys, os
sys.path.insert(1, os.getcwd())
from assets import checkType
from .lineSearch import lineSearch
### REQUIRES LINE SEARCH.PY FOR WORKING

def steepestDescent(x_n, Df,f, convergence_threshold = 0.0001): 
	"""
	Returns a minimun of f using the steepest Descent method https://en.wikipedia.org/wiki/Method_of_steepest_descent
	
	Args:
	------------------------------------
	x_n: point form which we want to start
	Df: derivative of f 
	f: target function
	convergence_threshold: maximun variation in the minimun in order to return a solution

	Returns:
	------------------------------------
	x_n: such that minimizes f

	"""
	# Rises an Exception if x_n is not one of these types
	checkType(x_n, int, float, np.ndarray, list, tuple)

	current_min = np.Inf
	while True:
		new_min = f(x_n)

		# Checking convergence and that the minimun be non increasing
		if current_min < new_min or abs(current_min - new_min) < convergence_threshold:
			return x_n
	
		d_n = -np.array(Df(x_n))
		alpha = lineSearch(f, x_n, d_n)
		x_n	+= alpha*d_n
		current_min = new_min