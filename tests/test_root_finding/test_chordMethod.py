import sys, os, pytest 
import numpy as np

sys.path.insert(1, os.getcwd())
from root_finding import newtonMethod

tolerance = 0.0001
def test_polynomials():
	f = lambda x: x**3 + 1
	a0 = -9
	assert f(newtonMethod(a0, f, tolerance))<=tolerance

def test_trigonomectrycs():
	f = lambda theta: np.cos(theta)
	a0 = np.pi
	assert f(newtonMethod(a0, f, tolerance))<=tolerance

def test_raiseValueError():
	f = lambda x:x**3+1
	a0 = 's'
	tolerance = 0.1
	with pytest.raises(ValueError, match=f'x0: {a0} is not a valid input'):
		newtonMethod(a0, f,tolerance)
		
	a0 = 0.1
	tolerance = 'carlitos'
	with pytest.raises(ValueError, match=f'tolerance: {tolerance} is not a valid input'):
		newtonMethod(a0, f, tolerance)