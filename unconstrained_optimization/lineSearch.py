import numpy as np

def lineSearch(f, x_n, d_n, delta_alpha=0.01, convergence_threshold = 0.001):
	current_min = np.Inf
	alpha = 0
	while True:
		alpha += delta_alpha
		new_min = f(x_n+alpha*d_n)
		
		if abs(current_min -new_min) < convergence_threshold:
			return alpha - delta_alpha

		if new_min > current_min:
			return alpha - delta_alpha
		
		current_min = new_min

		