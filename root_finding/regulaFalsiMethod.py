import numpy as np

def regulaFalsiMethod(a,b,f,tolerance):
    """
    Implements the regula fali method for rootfinding with an optimized formula
    More info: https://en.wikipedia.org/wiki/Regula_falsi

    Args:
    -------------------------------
    a: value such that f(a) <0
    b: value such that f(b) > 0
    f: funciton we want to find the root from
    tolerance: maximun value f(x) can take for returning x

    Returns:
    -------------------------------
    x: root of f
    """
    if not any(map(lambda x: isinstance(a, x), [int, float])):
        raise ValueError(f'a: {a} is not a valid input')
	
    if not any(map(lambda x: isinstance(b, x), [int, float])):
        raise ValueError(f'b: {b} is not a valid input')

    if not any(map(lambda x: isinstance(tolerance, x), [int, float])):
        raise ValueError(f'tolerance: {tolerance} is not a valid input')

    if not callable(f):
        raise ValueError('f is not a function')

    error = np.Inf
    while error > tolerance:
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
    
        if f(c) < 0:
            a = c
        else:
            b = c  
        error = abs(f(c)) 
    return c