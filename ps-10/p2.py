import numpy as np
from dcst import dst, idst
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  


sigma = 10**(-10)
kappa = 5 * 10**10
L = 10**(-8)
x0 = L/2
N=1000
a = L/N
h = 10**(-18)
hb = 1*10**(-34)
M = 9.109 * 10**(-31)

xs = np.linspace(0, L, N)

def psi0(x):
    return np.exp(- (x-x0)**2/(2 * sigma**2))*np.exp(1j*kappa*x)

a = dst(psi0(xs).real)
eta = -dst(psi0(xs).imag)

def psi(t):
    k = np.arange(1, N+1)
    stuff = np.pi**2 * hb * k**2 * t/ (2*M*L**2)
    var = a * np.cos(stuff) - eta * np.sin(stuff)
    return idst(var)

plt.plot(xs, psi(10**(-16)))
plt.xlabel('$x$ (m)')
plt.ylabel('$\psi(x)$  $(1/\sqrt{m})$')
plt.show()

fig, ax = plt.subplots()
line, = ax.plot(xs, psi(0))
ax.set_xlabel('$x$ (m)')
ax.set_ylabel('$\psi(x)$  $(1/\sqrt{m})$')

def frame(i):
   line.set_data(xs, psi(i*h))
   return line,

ani = FuncAnimation(fig, frame, frames = 10000, interval=10, blit=True)
#ani.save('p2.gif', fps=30)
plt.show()

