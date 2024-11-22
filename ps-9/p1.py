import numpy as np
import matplotlib.pyplot as plt

def f_harmonic(r, t, args): 
    x = r[0]
    y = r[1]
    omega = args[0]
    dxdt = y
    dydt = -x*omega**2

    return np.array([dxdt, dydt], float)

def f_anharmonic(r, t, args): 
    x = r[0]
    y = r[1]
    omega = args[0]
    dxdt = y
    dydt = -x**3*omega**2

    return np.array([dxdt, dydt], float)

def f_vanderPol(r, t, args): 
    x = r[0]
    y = r[1]
    omega = args[0]
    mu = args[1]
    dxdt = y
    dydt = mu*(1-x**2)*y - x*omega**2

    return np.array([dxdt, dydt], float)

def solve(f, x0, y0, args = [1], t0=1, tf=50, N=1000):

    h = (tf - t0)/N

    tpoints = np.arange(t0, tf, h)
    xpoints = []
    ypoints = []

    r = np.array([x0, y0], float)

    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
    
        k1 = h*f(r,t, args)
        k2 = h*f(r+0.5*k1,t+0.5*h, args)
        k3 = h*f(r+0.5*k2, t+0.5*h, args)
        k4 = h*f(r+k3, t+h, args)
        r += (k1 + 2*k2 + 2*k3 + k4)/6
    
    return (tpoints, xpoints, ypoints)

# Harmonic Oscillator
sol = solve(f_harmonic, 1, 0)
sol1 = solve(f_harmonic, 2, 0)

plt.plot(sol[0],sol[1])
plt.plot(sol1[0], sol1[1])
plt.title('Harmonic Oscillator')
plt.legend(['x0 = 1', 'x0 = 2'])
plt.xlabel('t')
plt.ylabel('x')
plt.show()

# Anharmonic Oscillator
sol = solve(f_anharmonic, 1, 0)
sol1 = solve(f_anharmonic, 2, 0)

plt.plot(sol[0],sol[1])
plt.plot(sol1[0], sol1[1])
plt.title('Anharmonic Oscillator')
plt.legend(['x0 = 1', 'x0 = 2'])
plt.xlabel('t')
plt.ylabel('x')
plt.show()

# Harmonic Oscillator
sol = solve(f_harmonic, 1, 0)
sol1 = solve(f_harmonic, 2, 0)

plt.plot(sol[1],sol[2])
plt.plot(sol1[1], sol1[2])
plt.title('Harmonic Oscillator')
plt.legend(['x0 = 1', 'x0 = 2'])
plt.xlabel('x')
plt.ylabel('dx/dt')
plt.show()

# Anharmonic Oscillator
sol = solve(f_anharmonic, 1, 0)
sol1 = solve(f_anharmonic, 2, 0)

plt.plot(sol[1],sol[2])
plt.plot(sol1[1], sol1[2])
plt.title('Anharmonic Oscillator')
plt.legend(['x0 = 1', 'x0 = 2'])
plt.xlabel('x')
plt.ylabel('dx/dt')
plt.show()

# Van der Pol Oscillator
sol = solve(f_vanderPol, 1, 0, tf=20, args=[1, 1])
sol1 = solve(f_vanderPol, 1, 0, tf=20, args=[1, 2])
sol2 = solve(f_vanderPol, 1, 0, tf=20, args=[1, 4])


plt.plot(sol[1],sol[2])
plt.plot(sol1[1], sol1[2])
plt.plot(sol2[1], sol2[2])
plt.title('van der Pol Oscillator')
plt.legend(['$\mu = 1$', '$\mu = 2$', '$\mu = 4$'])
plt.xlabel('x')
plt.ylabel('dx/dt')
plt.show()