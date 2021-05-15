import sys, os
sys.path.insert(1, os.getcwd())
from root_finding import biesctionMethod
import numpy as np

def test_polynomials():
	f = lambda x: x**3 + 1
	tolerance = 0.001
	a0 = -9
	b0 = 3
	assert f(biesctionMethod(a0, b0, f, tolerance))<=tolerance
