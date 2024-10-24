import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def func(x):
    return (x - 0.3)**2*np.exp(x)

x = np.linspace(-1, 1, 100)
plt.plot(x, func(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

def brent(a, b, c, f, tol = 0.01):
    '''Brents Method, a b c must bracket the minimum'''

    # Get the min of the parabola
    bottom  =  2*((b-a) * (f(b)-f(c)) - (b-c) * (f(b)-f(a)))
    top = ((b - a)**2 * (f(b)-f(c)) - (b-c)**2 * (f(b)-f(a)))
    minimum = b - top/bottom

    # Get the indices that sort x by f(x)
    x = [a, b, c]
    fx = np.argsort([f(a), f(b), f(c)])

    # Check if the difference between the new min and the old min is within the tolerance
    if (np.absolute(x[fx[0]] - minimum) <= tol):
        return minimum
    # Keep Brenting
    else:
        return brent(minimum, x[0], x[1], f, tol)

myBrent = brent(0, 0.5, 1, func)
scipyBrent = sp.optimize.brent(func, brack = (0, 0.5, 1), tol=0.01)

print('My Brent:', myBrent)
print('scipy Brent:', scipyBrent)
print('Difference:', np.absolute(myBrent-scipyBrent))
