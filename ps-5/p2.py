import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math

def f(x, a):
    '''Original Integrand of delta function'''
    return x**(a - 1) * np.exp(-x)

def plotIntegrand(a, range, n=100):
    '''plot the original integrand'''
    xs = np.linspace(range[0], range[1], 100)
    plt.plot(xs, f(xs, a))

# Part a plot integrands on the same plot
plotIntegrand(2, (0, 5))
plotIntegrand(3, (0, 5))
plotIntegrand(4, (0, 5))
plt.legend(["a=2", "a=3", "a=4"])
plt.xlabel("x")
plt.ylabel("x^(a-1) * e^(-x)")

plt.show()

#Part b
def newIntegrand(z, a):
    '''Scaled integrand'''
    c = a - 1
    x = - c * z/(z-1) 
    dx = c / ((z-1)**2)
    return np.exp((a-1)*np.log(x)-x) * dx

def gamma(a):
    '''integrate the scaled integrand using scipy'''
    return sp.integrate.quad(newIntegrand, 0, 1, args=(a))[0]

print('Γ(3/2) =', gamma(3/2))

def printGammaFactorial(a):
    '''Print Gamma(a) and (a-1)! for comparison'''
    print(f"Γ({a}) = {gamma(a)},  {(a-1)}! = {math.factorial(a-1)}")

printGammaFactorial(4)
printGammaFactorial(6)
printGammaFactorial(10)


