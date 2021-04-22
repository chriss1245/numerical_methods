import matplotlib.pyplot as plt
import numpy as np


from utils import secantMethod # rootfinding auxiliar algorithm

#-------------------------------------------------------------------------------------------------------------------------------
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
	u_l = u_m
	u = np.zeros(shape=(N,1))
	for n in range(N):
		t_n = t_0 + h*n
		g = lambda u_n: u_n - h*f(t_n,u_n) - u_m
		u_m = secantMethod(u_m, g, 0.0001)
		u[n] = u_m

	return u
	
#------------------------------------------------------------------------------------------------------------
#Testing
def f(t_n, u_n): 
	return 2*t_n*u_n #u_n = exp(t_n^2)

def F(t): return np.exp(t**2)

t_0 = 1
u_0 = F(t_0)
h = 0.1
N = 10
u = euler(t_0, u_0, f, h, N) # Approximation of F

t = np.arange(t_0, t_0+N*h, h) # Interval
y = F(t).reshape([len(t),1]) # Theorethical F
e = np.abs(np.subtract(y,u)) # Error 

fig, ax = plt.subplots()
ax.plot(t, u, 'b', marker='o')
ax.plot(t, y, 'g', marker='o')
ax.plot(t, e, 'r', marker='o')
plt.show()

"It works worse than the explicit method... we need to make more research"