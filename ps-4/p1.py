import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """The Integrand"""
    return x**4 * np.exp(x) / ((np.exp(x) - 1)**2)

def cv(T, N = 20):
    """Computes Cv(T) with N points"""
    V = 0.001 #m^3   1000cc
    rho = 6.022*10**(28) #m^3
    DebyeT = 428 #K
    kB = 1.4*10**(-23)

    xs, ws = np.polynomial.legendre.leggauss(N)

    integral = np.sum(ws * func_rescale(xs, (0, DebyeT/T)))

    prefactor = 9 * V * rho * kB * (T/DebyeT)**3

    return prefactor * integral
    

def func_rescale(xp=None, range=None):
    """
    From Blanton's Jupyter Notebook
    Rescaled function for new limits of -1 to 1
    
    Parameters
    ----------
    
    xp : np.float32 or np.float64
        input parameter (in new limits' coordinates)
        
    range : list or np.array
        [2] low and high limits of range to map to -1 to 1
        
    Returns
    -------
    
    fn : np.float32 or np.float64
        output of rescaled function
    """
    weight = (range[1] - range[0]) * 0.5
    x = range[0] + 0.5 * (range[1] - range[0]) * (xp + 1.)
    return(weight * f(x=x))

Ts = np.linspace(0, 500, 100)

Ns = np.arange(10, 80, 10)

for N in Ns:
    cvs = []

    for T in Ts:
        cvs.append(cv(T, N))

    plt.plot(Ts, cvs)

plt.legend(Ns)
plt.xlabel("T")
plt.ylabel("Cv")
plt.show()

T = 5
for N in Ns:

    plt.scatter(N, cv(T, N))

plt.xlabel("N")
plt.ylabel("Cv @ T = 5K")
plt.show()
