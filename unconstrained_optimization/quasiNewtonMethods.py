import numpy as np
import sys, os
sys.path.insert(1, os.getcwd())
from assets import checkType
from .lineSearch import lineSearch

def quasiNewtonOptimization(x_n, f, Df, hessianAproximation= 'BFGS', convergence_threshold = 0.0001):
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
	checkType(x_n, tuple, np.ndarray, list)
	
	# Checking which matrix approximation use
	# Using unicode symbols in order to make more readable the formulas
	if hessianAproximation == 'Broyden':
		G = lambda G_k, δ, γ:  G_k + ((G_k/(δ.dot(G_k.dot(γ))))*np.outer((δ - G_k.dot(γ)),δ.T))
	elif hessianAproximation == 'BFGS':
		G = lambda G_k, δ, γ: G_k - ((np.outer(δ,γ).dot(G_k) + G_k.dot(np.outer(γ,δ)))/δ.dot(γ)) + (np.outer(δ,δ))*(1 + γ.dot(G_k).dot(δ)/δ.dot(γ))
	elif hessianAproximation == 'Steepest': # Steepset descent
		G = lambda G_k, δ, γ: G_k
	else:
		raise ValueError('Hessian approximation matrix not recognized')
	
	G_n = np.identity(len(x_n))
	x_n = x_n.astype(float)
	new_min = np.Inf
	while True:
		# Update the x_{n-1} and current_min to the new values
		x_m = np.copy(x_n)
		current_min = new_min
		new_min = f(x_n)

		# Descent direction 
		d_n = (-np.linalg.inv(G_n)).dot(Df(x_n))
		if type(d_n ) == np.matrix:
			d_n = np.array(d_n.A1)
		#Line search
		alpha_n = lineSearch(f, x_n, d_n)
		x_n	= x_n+d_n*alpha_n

		# Checking convergence and that the minimun be non increasing
		if current_min < new_min or abs(current_min - new_min) < convergence_threshold:
			return x_n
		
		# computing G_n
		delta_n = x_n - x_m
		gamma_n = Df(x_n)-Df(x_m)
		
		G_n = G(G_n, delta_n, gamma_n)