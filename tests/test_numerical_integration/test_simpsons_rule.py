import sys
import os
sys.path.insert(1, os.getcwd())
from numerical_integration import simpsonIntegration
from tests.test_numerical_integration.templeate_numerical_integration_test import *

def test_quadratic_funcitons():
	assert abs(f1 - simpsonIntegration(f, a, b, m)) < m**4 # The result should have a precision of order forth

def test_sinosoidal_function():
	assert abs(g1 - simpsonIntegration(g, a, c, m)) < m**4

def test_constant_function():
	assert abs(h1 - simpsonIntegration(g, a, b, m)) < m**4 

def test_linear_function():
	assert abs(i1 - simpsonIntegration(i, a, b, m)) < m**4 