import sys
import os
sys.path.insert(1, os.getcwd())
from numerical_integration import midpointIntegration
from tests.test_numerical_integration.templeate_numerical_integration_test import *

def test_quadratic_funcitons():
	assert abs(f1 - midpointIntegration(f, a, b, m)) < m**2 # The result should have a precision of order almost three

def test_sinosoidal_function():
	assert abs(g1 - midpointIntegration(g, a, c, m)) < m**2

def test_constant_function():
	assert abs(h1 - midpointIntegration(g, a, b, m)) < m**2

def test_linear_function():
	assert abs(i1 - midpointIntegration(i, a, b, m)) < m**2