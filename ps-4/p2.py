import numpy as np
import matplotlib.pyplot as plt


def func_rescale(xp=None, a=0, range=None):
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
    return(weight * f(x=x, a=a))

def f(x, a):
    return 1/np.sqrt(a**4-x**4)

def T(a):
    N = 20

    xs, ws = np.polynomial.legendre.leggauss(N)

    return np.sqrt(8) * np.sum(ws * func_rescale(xs, a, (0, a)))

As = np.linspace(0, 2, 100)
Ts = []

for a in As:
    Ts.append(T(a))

plt.plot(As, Ts)
plt.xlabel("a")
plt.ylabel("T")
plt.show()
