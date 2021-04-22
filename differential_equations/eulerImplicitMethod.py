import matplotlib.pyplot as plt
import numpy as np

#------------------------------------------------------------------------------------------------------------------------------
# Auxiliary function needed for the method. It is better described at the rootfinding section
def secantMethod(x_0, f, tolerance):
	"""
	Applies the secant method for rootfinding of non-linear equations

	Args:
	-----------------------------------------------------------------------
	x_0: initial point
	f: function
	tolerance: the maximun value that abs(f(c_n)) can take

	Returns:
	------------------------------------------------------------------------
	x_n a point such that abs(f(x_n))<tolerance
	"""
	x_l = x_0 # x_{n-2}
	x_m = 2*x_0 + 1 # x_{n-1}
	error = np.Inf
	while error > tolerance:
		x_n = x_m - f(x_m)*(x_m-x_l)/(f(x_m)-f(x_l))
		x_l = x_m
		x_m = x_n
		error = abs(f(x_n))

	return x_n


#-------------------------------------------------------------------------------------------------------------------------------
#Actual method
def euler(t_0, u_0, f, h, N):
	"""
	Also known as backward euler's method
	Uses the formula u_{n+1} = u_{n} + h*f_{n+1} which can be saw as a rootfinding problem u_{n+1} - h*f_{n+1} - u_{n}=0 solved with the secant method
	Args:
	-------------------------------------------------------------------------
	t_0: initial condition point for our equation
	u_0: image of t_0
	f: derivative of y
	h: discretization stepsize
	N: number of steps

	Returns:
	--------------------------------------------------------------------------
	A numpy array which approximates the value of y (F) at the points given by t_0 +n*h, with n a Natural number
	"""
	u_m = u_0 # u_{n-1}
	u = np.zeros(shape=(N,1))
	for n in range(N):
		t_n = t_0 + h*n
		g = lambda u_n: u_n - f(t_n,u_n) - u_m
		u[n] = secantMethod(u_m, g, 0.0001)
	
	return u
	
#------------------------------------------------------------------------------------------------------------
#Testing
def f(t_n, u_n): 
	return 2*t_n*u_n #u_n = exp(t_n^2)

def F(t): return np.exp(t**2)

t_0 = 1
u_0 = F(t_0)
h = 0.05
N = 25
u = euler(t_0, u_0, f, h, N) # Approximation of F

t = np.arange(t_0, t_0+N*h, h) # Interval
y = F(t).reshape([N,1]) # Theorethical F
e = np.subtract(y,u) # Error 

fig, ax = plt.subplots()
ax.plot(t, u, 'b', marker='o')
ax.plot(t, y, 'g', marker='o')
ax.plot(t, e, 'r', marker='o')
plt.show()