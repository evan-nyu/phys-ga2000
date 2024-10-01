import numpy as np
import matplotlib.pyplot as plt
import math

def H(n, x):
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return 2 * x
    return 2 * x * H(n-1, x) - 2 * (n-1) * H(n-2, x)

def psi(n, x):
    return H(n, x) * np.exp(-(x**2)/2) / np.sqrt(2**n * math.factorial(n) * np.sqrt(np.pi))

xs = np.linspace(-4, 4, 100)

ns = [0, 1, 2, 3]

for n in ns:
    psis = (psi(n, xs))
    plt.plot(xs, psis)
plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.legend(ns)
plt.show()

#Part b
def n30():
    xs = np.linspace(-10, 10, 500)

    psis = psi(30, xs)

    plt.plot(xs, psis)
    plt.xlabel("x")
    plt.ylabel("ψ(x)")
    plt.show()

n30()

#Part c
def f(n, x):
    return x**2 * np.abs(psi(n, x))**2

def func_rescale(xp=None, n=0, q=None):
    """Rescaling function for remapping 0..infinity to -1..1
    
    Parameters
    ----------
     
    xp : np.float32 or np.float64
         position to evaluate function at 
         
    q : np.float32 or np.float64
         remapping pivot point
         
    Returns
    -------
    
    f : np.float32 or np.float64
         value of function
    """
    x = q * (1. + xp) / (1. - xp)
    weight = 2. * q / (1. - xp)**2
    return (weight * f(n, x=x))

def uncertainty(n, N):
    xs, ws = np.polynomial.legendre.leggauss(N)

    #since integrand is symmetric, only need to integrate from 0 to inf
    #use 2.3 for q
    integral = 2 * np.sum(ws * func_rescale(xs, n, 2.3))
    return np.sqrt(integral)

print("Uncertainty for n=5:", uncertainty(5, 100))

#Part D
def hermiteF(n, x):
    return x**2 * np.abs(H(n, x) / np.sqrt(2**n * math.factorial(n) * np.sqrt(np.pi)))**2


def hermiteUncertainty(n, N):
    xs, ws = np.polynomial.hermite.hermgauss(N)

    integral = np.sum(ws * hermiteF(n, xs))
    return np.sqrt(integral)
print("Hermite Uncertainty for n=5", hermiteUncertainty(5, 100))
