import sys
import os
import numpy as np
sys.path.insert(1, os.getcwd())
#from assets import conjugateGradientOptimization


def test_RNScalar():
	A = [[1,0],[0,1]]
	b = [1,1]
	threshold = 0.001
	possible_sol = np.linalg.solve(A,[0,0])
	print(possible_sol)
	print(np.linalg.norm(np.array([0,0]) - 0.5* np.dot(possible_sol, np.dot(A, possible_sol))+ np.array(b) ))




	
	
def test_RScalar():
	A = 3
	b = 20


test_RNScalar()