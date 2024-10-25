import numpy as np
import scipy as sp
import math
import matplotlib.pyplot as plt

def func(x):
    return (x - 0.3)**2*np.exp(x)

x = np.linspace(-1, 1, 100)
plt.plot(x, func(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

def golden(a, b, c, f, tol, step):
    w = 0.382
    # Split the larger interval
    if((b - a) > (c - b)):
        x = b
        b = b - w * (b - a)
    else:
        x = b + w * (c - b)
    step = (step[1], np.absolute(x - b))
    fb = f(b)
    fx = f(x)
    if(fb < fx):
        c = x
    else:
        a = b
        b = x
    return brent(a, b, c, f, tol, step)

def brent(a, b, c, f, tol = 0.01, step = (np.inf, np.inf)):

    # Get the min of the parabola
    bottom  =  2*((b-a) * (f(b)-f(c)) - (b-c) * (f(b)-f(a)))
    top = ((b - a)**2 * (f(b)-f(c)) - (b-c)**2 * (f(b)-f(a)))
    minimum = b - top/bottom
    
    if math.isnan(minimum):
        return 0

    # Get the indices that sort x by f(x)
    x = [a, b, c]
    fx = np.argsort([f(a), f(b), f(c)])

    if (np.absolute(x[fx[0]] - minimum) <= tol):
        return minimum
    step = (step[1], np.absolute(minimum - a))

    if minimum < np.min(x):
        return golden(minimum, b, c, f, tol, step)
    elif minimum > np.max(x):
        return golden(a, b, minimum, f, tol, step)

    elif minimum - a > step[0]:
        return golden(a, b, minimum, f, tol, step)
    # Check if the difference between the new min a
    # Keep Brenting
    else:
        return brent(x[0], minimum, x[1], f, tol, step)

myBrent = brent(0, 0.5, 1, func, 0.0001)
scipyBrent = sp.optimize.brent(func, brack = (0, 0.5, 1), tol=0.0001)

print('My Brent:', myBrent)
print('scipy Brent:', scipyBrent)
print('Difference:', np.absolute(myBrent-scipyBrent))
