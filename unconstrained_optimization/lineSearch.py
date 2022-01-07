import numpy as np
import sys
import os

sys.path.insert(1, os.getcwd())


def lineSearch(f, x_n, d_n, delta_alpha=0.01, convergence_threshold=0.001):
    """
    Given a function, a point x and a descent direction d It computes the alpha such that minimizes f(x + alpha*d)
    Args:
    -----------------------------------------------
    f: function we want to maximize the minimization step
    x_n: the point from which we want to start
    d_n: the direction we want to go
    delta_alpha: the increase in alpha
    convergence_threshol: if the computed minimun does not change more than this threshold, the alpha is returned	
    """
    current_min = np.Inf
    alpha = 0
    while True:
        alpha += delta_alpha
        new_min = f(x_n+d_n*alpha)

        if np.abs(current_min - new_min) == np.nan:
            raise ValueError()

        if np.abs(current_min - new_min) < convergence_threshold:
            return alpha - delta_alpha

        if new_min > current_min:
            return alpha - delta_alpha

        current_min = new_min
