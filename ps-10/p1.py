import numpy as np
from banded import banded
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
m = 9.109 * 10**(-31)

a1 = 1 + h * 1j * hb/ (2 * m * a**2)
a2 = -h * 1j * hb / (4 * m * a**2)
b1 = 1 - h * 1j * hb / (2 * m * a**2)
b2 = h * 1j * hb / (4 * m * a**2)


def psi0(x):
    return np.exp(- (x-x0)**2/(2 * sigma**2))*np.exp(1j*kappa*x)

psi = psi0((1+np.arange(0, N))*a)

def get_v(i, psi):
    return b1 * psi[i] + b2*(np.take(psi, i+1, mode='clip') + np.take(psi, i-1, mode='clip'))

xs = np.linspace(0, L, N)

bands = np.zeros((3, N), dtype=complex)
bands[0] = a2
bands[1] = a1
bands[2] = a2

T = 5000
psis = np.zeros((T, N))

for i in range(T):
    v = (get_v(np.arange(0, N), psi))
    psi = banded(bands, v, 1, 1)
    psis[i] = psi

fig, ax = plt.subplots()
line, = ax.plot(xs, psis[0])
ax.set_xlabel('$x$ (m)')
ax.set_ylabel('$\psi(x)$  $(1/\sqrt{m})$')

def frame(i):
   line.set_data(xs, psis[i])
   return line,

ani = FuncAnimation(fig, frame, frames = T, interval=10, blit=True)
#ani.save('p1.gif', fps=30)
plt.show()

