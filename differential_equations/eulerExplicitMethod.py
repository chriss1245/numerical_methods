import numpy as np
import matplotlib.pyplot as plt

def euler(t_0, u_0, f, h=0.1, N=10):

	"""
	Also known as forward euler's method
	Uses the equation u_{n+1} = u_{n} + h*f(t_{n}, u_{n}), where u_{n+1} 

	Args
	--------------------------------------------------------------------
	t_0: initial condition point for our equation
	u_0: image of t_0
	f: derivative of y
	h: discretization stepsize
	N: number of steps
	
	Returns
	--------------------------------------------------------------------
	A numpy array of points which approximate y(t), with t= t_0 + ih, i from 0 to N
	"""
	u_n = u_0
	u = np.zeros(shape=(N,1))
	for n in range(N):
		t_n = t_0 + n*h
		u_n = u_n + h*f(t_n, u_n)
		u[n] = u_n
	return u


def recursiveEuler(t_n, u_n, f, h=0.1,N = 1):

	if N == 1:
		#Base case
		return u_n+h*f(t_n, u_n)

	#Recursive case
	return [u_n+h*f(t_n, u_n), *recursiveEuler(t_n+h, u_n+h*f(t_n, u_n ), f, h, N-1)]

	
#----------------------------------------------------------------------------------------
#Testing
def f(t_n, u_n): 
	return 2*t_n*u_n #u_n = exp(t_n^2)

def F(t): return np.exp(t**2)

t_0 = 1
u_0 = F(t_0)
h = 0.1
N = 10
u = recursiveEuler(t_0, u_0, f, h, N) # Approximation of F

t = np.arange(t_0, t_0+N*h, h) # Interval
y = F(t).reshape([N,1]) # Theorethical F
e = np.subtract(y,u) # Error 

fig, ax = plt.subplots()
ax.plot(t, u, 'b', marker='o')
ax.plot(t, y, 'g', marker='o')
ax.plot(t, e, 'r', marker='o')
plt.show()











	
