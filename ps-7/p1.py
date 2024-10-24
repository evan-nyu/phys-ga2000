from jax import grad
import numpy as np

m_earth = 5.974*10**24 #kg
m_moon = 7.384*10**22 #kg
m_sun = 1.988475*10**30 #kg from wikipedia
m_jupiter = 1.898*10**27 #kg from wikipedia
r_moon = 3.844*10**8 #m
r_earth = 149.60 * 10**9 #m from wikipedia

def f(r, m):
    return m/((1-r)**2) + r - 1/r

fp = grad(f)

def newton(r, m, tol = 0.01):
    if np.absolute(f(r, m)) < tol:
        return r
    else:
        return newton(r - f(r, m)/fp(r, m), m, tol)

print('r for Moon and Earth', np.format_float_scientific(r_moon * newton(0.001, m_moon/m_earth, 0.0001)))
print('r for Earth and Sun', np.format_float_scientific(r_earth * newton(0.001, m_earth/m_sun, 0.0001)))
print('r for Jupiter in Earth Orbit', np.format_float_scientific(r_earth * newton(0.001, m_jupiter/m_sun, 0.0001)))
