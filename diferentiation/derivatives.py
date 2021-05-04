import numpy as np
import matplotlib.pyplot as plt

def forwardDifference(f, x_0, h = 0.00001):
	"""
	Applies the second order forward Difference for the approximation of the derivative

	Args:
	------------
	f: Function we want to get the derivative from
	x_0: point
	h: the discretization stepsize
	"""
	return (4*f(x_0+h)-f(x_0+2*h)-3*f(x_0))/h

def backwardDifference(f, x_0, h = 0.00001):
	"""
	Applies the second order backward Difference for the approximation of the derivative

	Args:
	------------
	f: Function we want to get the derivative from
	x_0: point
	h: the discretization stepsize
	"""
	return (-4*f(x_0-h)+f(x_0-2*h)+3*f(x_0))/h

def centralDifference(f, x_0, h=0.000001):
	"""
	Applies the second order central Difference for the approximation of the derivative

	Args:
	------------
	f: Function we want to get the derivative from
	x_0: point
	h: the discretization stepsize
	"""

	return (f(x_0+h)-f(x_0-h))/(2*h)

#--------------------------------------------------------------------
#Testing
H = np.linspace(0.001,1,25)
X = np.linspace(-5,5,25)

y = lambda x: x**2
dy = lambda x:2*x

d1y = d2y = d3y = np.zeros_like(H)
i = 0
for h in H:
	d1y[i] = np.linalg.norm(dy(X)-forwardDifference(y, X, h))
	d2y[i] = np.linalg.norm(dy(X)-backwardDifference(y, X, h))
	d3y[i] = np.linalg.norm(dy(X)-centralDifference(y, X, h))

plt.plot(H, d1y, d2y, d3y)
plt.show()
