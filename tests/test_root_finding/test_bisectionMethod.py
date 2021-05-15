import sys, os, pytest 
import numpy as np

sys.path.insert(1, os.getcwd())
from root_finding import bisectionMethod

tolerance = 0.0001
def test_polynomials():
	f = lambda x: x**3 + 1
	a0 = -9
	b0 = 3
	assert f(bisectionMethod(a0, b0, f, tolerance))<=tolerance

def test_trigonomectrycs():
	f = lambda theta: np.cos(theta)
	a0 = np.pi
	b0 = 2*np.pi
	assert f(bisectionMethod(a0, b0, f, tolerance))<=tolerance

def test_raiseValueError():
	f = lambda x:x**3+1
	a0, b0 = -1, 's'
	tolerance = 'carlitos'

	with pytest.raises(ValueError, match=f'b_0: {b0} is not a valid input'):
		bisectionMethod(a0,b0,f,tolerance)

	b0 = 1
	with pytest.raises(ValueError, match=f'tolerance: {tolerance} is not a valid input'):
		bisectionMethod(a0,b0,f, tolerance)