import sys, os, pytest
sys.path.insert(1, os.getcwd())
import numpy as np
from unconstrained_optimization import quasiNewtonOptimization

F = lambda X: X[0]**2+X[1]**2
df = lambda X: [2*X[0], 2*X[1]]
x_n = [30,100]

def test_Steepest():
	minimun = quasiNewtonOptimization(x_n, F, df, hessianAproximation= 'Steepest')
	assert 0.0 == round(minimun[0]) == round(minimun[1])
def test_BFGS():
	minimun = quasiNewtonOptimization(x_n, F, df)
	assert 0.0 == round(minimun[0]) == round(minimun[1])

def test_Broyden():
	minimun = quasiNewtonOptimization(x_n, F, df, hessianAproximation= 'Broyden')
	assert 0.0 == round(minimun[0]) == round(minimun[1])


