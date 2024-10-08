import jax.numpy as jnp
from jax import grad
import matplotlib.pyplot as plt

def f(x):
    return 1 + 1/2 * jnp.tanh(2*x)

def diff_central(func=None, x=None, dx=None):
    '''From Blanton's Notebook'''
    return((func(x + 0.5 * dx) - func(x - 0.5 * dx)) / dx)

def analytic_dfdx(x):
    return 1/(jnp.cosh(2*x))**2

#Create x values
xs = jnp.linspace(-2, 2, 100)

#Plot Central difference derivative
plt.scatter(xs, diff_central(f, xs, 0.1))

#plot analytic derivative
plt.plot(xs, analytic_dfdx(xs))

#Get Jax derivative
jax_dfdx = grad(f)
dfdxs = []
for x in xs:
    dfdxs.append(jax_dfdx(x))

#plot jax derivative
plt.plot(xs, dfdxs)
plt.legend(["Central Difference", "Analytic", "JAX"])
plt.ylabel("Derivative of 1+1/2 tanh(2x)")
plt.xlabel("x")
plt.show()
