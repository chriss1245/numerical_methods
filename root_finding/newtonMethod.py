import numpy as np
def newtonMethod(x0, f, tolerance):
    """
    This function applies the newtons method for root finding
    The derivative of f is approximated trought the definition of limit with h = 0.0000001
    More info: https://en.wikipedia.org/wiki/Newton%27s_method

    Args:
    ---------------
    x0: Initial point where to start
    f: function we want to find the root of
    tolerance: maximun value the function can take for returning xn

    Returns:
    ---------------
    x0: root of the function
    """
    # Checking input type
    if not any(map(lambda x: isinstance(x0, x), [int, float])):
        raise ValueError(f'x0: {x0} is not a valid input')

    if not any(map(lambda x: isinstance(tolerance, x), [int, float])):
        raise ValueError(f'tolerance: {tolerance} is not a valid input')

    if not callable(f):
        raise ValueError('f is not a function')

	# Checking the slope is not 0
    h = 0.0000001
    error = np.Inf
    steps = 0

    while error > tolerance:
        y0 = f(x0)
        dy0 = (f(x0+h)-f(x0))/h
        x0 = x0 - y0/dy0
        error = np.abs(f(x0))
        steps +=1

    return x0