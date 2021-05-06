import sys, os
sys.path.insert(1, os.getcwd())
from assets import Polynomial
import numpy as np

def splineInterpolation(X,Y):
	"""
	Applies 3rd degree splineInterpolation

	Args:
	----------------------------------
	X: Points at the x axis (ordered from less to more)
	Y: Images of the X

	Returns:
	----------------------------------
	A Polynomial_by_parts object composed by different polynomials of order 3
	"""
	# Sorting X and its images
	indexes = np.argsort(np.array(X))
	X = np.take_along_axis(np.array(X), indexes, 0).astype(float)
	Y = np.take_along_axis(np.array(Y), indexes, 0).astype(float)

	n = len(X) # Number of equations gotten with the condition 1: P_{k}(x_{i}) = y_{i} for all i
	p = n-1 # Number of interpolating 3rd degree polynomials
	dimension = p*4 # A third degree polynomial needs 4 coeffitients to be determined (ax^3+bx^2+cx+d).
	A = np.zeros((dimension, dimension)) # Polynomials coefficients Matrix (Equations)
	b = np.zeros(dimension) # Answers of the system Ax=b
	eq = 0 # Index of the equation
	j = 0 # Index of the coefficient of the equation

	# For each polynomial we are going to obtain 2 equations from each pair of points
	i = 0
	while i < p:
		"""
		1st set of conditions 2p equations
		2nd set of conditions p-1 equations
		3rd set of conditions p-1 equations

		In total we have 4p-2 equations for determining our 4p coefficients of our p polynomials
		"""
		j = i*4 # j will vary among i*4 and (i+1)*4 which are the possitions that the coefficient of the i-th polynomial should take

		# FIRST SET OF CONDITONS: GRANT CONTINUITY
		#------------------------------------------

		# Equation given by evaluating the  current polynomial at the point x_{i}
		while j < i*4+3: 
			A[eq][j] = X[i]**(3-(j%4))
			j += 1
		A[eq][j] = 1
		b[eq] = Y[i]
		eq +=1
		j = i*4

		# Equation given by evaluating the current polynomial at the point x_{i+1}
		while j < i*4+3:
			A[eq][j] = X[i+1]**(3-(j%4))
			j += 1
		A[eq][j] = 1
		b[eq] = Y[i+1]
		eq +=1

		if i < p-1:

			# SECOND SET OF CONDITIONS: GRANT DIFFERENTIABILITY
			#--------------------------------------------------

			# Equation gotten by equating the images of the derivatives
			# of two consecutive polinomials at the point they have in common
			#P'_{i}(x_{k+1})-P'_{i+1}(x_{k+1}) = 0
			j = i*4
			while j < i*4 + 3: # P'_{i}: 3*x_{k+1}^2 + 2*x_{k+1} + 1
				A[eq][j] = (3-(j%4))*X[i+1]**(2-(j%4))
				j += 1

			while j < (i+1)*4 + 3: # P'_{i}: 3*x_{k+1}^2 + 2*x_{k+1} + 1
				A[eq][j] = -1*(3-(j%4))*X[i+1]**(2-(j%4))
				j += 1
			eq += 1
			

			# THRID SET OF CONDITIONS: GRANT SMOTHNESS
			#------------------------------------------

			#Equation gotten by equating the images of the second order derivatives
			#of two consecutive polynomials at their point in commom
			# P''_{i}(x_{k+1})-P''_{i+1}(x_{k+1}) = 0
			j = i*4
			#P''_{i}(x_{k}): 6*X_{k+1} +2
			A[eq][j] = 6*X[i+1]
			A[eq][j+1] = 2

			#-P''_{i}(x_{k}): -6*X_{k+1} -2
			A[eq][j+4] = -A[eq][j]
			A[eq][j+5] = -2
			eq += 1

		i +=1

	#FORTH SET OF CONDITIONS: GRANT SMOTHNESS AT THE BOUNDARIES (2 equations more)
	#--------------------------------------------

	# Equation gotten from equating P''_{1}(x_{0}) = 0
	A[eq][0] = 6*X[0]
	A[eq][1] = 2
	eq +=1
	# Equation gotten from equating P''_{p}(x_{n}) = 0
	A[eq][-4] = 6*X[0]
	A[eq][-3] = 2


	# Getting the coefficients of the polynomials (A*coefficients = b)
	coefficients = np.split(np.linalg.solve(A,b), p)

	# Creating the Polynomials
	polynomials = [Polynomial(*np.flip(c)) for c in coefficients]
	
	# Creating the function by parts
	def f(x):
		# Recursive part if we are evaluating a set of points
		if isinstance(x ,list):
			return np.array([f(point) for point in x])

		# Base case for one point
		i = 0
		if x <= X[0]:
			return polynomials[0](x) # The polynomial is defined so that it could be used as a function (__call__(self,x) method of Polynomial class)

		if x >= X[-1]:
			return polynomials[-1](x)

		while i < len(polynomials):
			if  X[i] <= x and x <= X[i+1]:
				return polynomials[i](x)
			i += 1

	return f

f = splineInterpolation([9,2,6,7,1], [0,4,8, 9,3])

print(f([1,2,6,7,9, 1.3]))
