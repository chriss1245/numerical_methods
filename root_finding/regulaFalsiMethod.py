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
    error = np.Inf
    while error > tolerance:

        
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
    
        if f(c) < 0:
            a = c

        else:
            b = c
            
        error = abs(f(c))
        
    return c

#-------------------------------------------------------------------------------------------
#Testing
f = lambda x: x**3+3
a0 = -9
b0 = 3
tol = 0.001
print("Method's root:", regulaFalsiMethod(a0, b0, f, tol), "Actual root:", -3**(1/3))