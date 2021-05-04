import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.insert(1, os.getcwd())
from assets import secantMethod

#--------------------------------------------------------------------------------------------------------------------
def trapezoidal(u_0, t_0, f, h, N):
	"""
	Also known as Crank-Nicolson method: it applies the equation u_{n+1} = u_{n} + 0.5*h*(f_{n}+f_{n+1})
	Which is interpreted as a root finding problem where we want to optain u_{n+1} using the secant method
	
	REMARK: At the function our u_{n+1} = u_n and our u_{n} = u_m. Analogously with t_{n+1} and t_{n}
	Args:
	-------------------------------------------------
	t_0: initial condition point
	u_0: image of t_0
	f: derivative of F such that f depends on F
	h: discretization stepsize
	N: Number of steps

	Returns:
	u: the images of F at the points t_n
	"""
	u_m = u_0 # u_{n-1}
	u = np.zeros(shape=(N,1))
	for n in range(N):
		t_m = t_0 + h*(n-1)  # t_{n-1}
		t_n = t_m + h # t_{n}
		

		#Crank nicolson described as a rootfinding problem we look for u_{n} such that(g(u_{n}))=0
		g = lambda u_n: 2*u_n - h*(f(t_m, u_m)+f(t_n,u_n))-2*u_m

		u_n = secantMethod(u_m, g)
		#u_n = (1+t_m*h)*u_m/(1-h*t_n)
		u_m = u_n
		u[n] = u_n
	return u


	
#------------------------------------------------------------------------------------------------------------
#Testing
def f(t_n, u_n): 
	return 2*t_n*u_n #u_n = exp(t_n^2)

def F(t): return np.exp(t**2)

t_0 = 21
u_0 = F(t_0)
h = 0.10
N = 10
u = trapezoidal(t_0, u_0, f, h, N) # Approximation of F

t = np.arange(t_0, t_0+N*h, h) # Interval
y = F(t).reshape([len(t),1]) # Theorethical F
e = np.abs(np.subtract(y,u)) # Error 

fig, ax = plt.subplots()
ax.plot(t, u, 'b', marker='o')
ax.plot(t, y, 'g', marker='o')
ax.plot(t, e, 'r', marker='o')
plt.show()

"NOt working"