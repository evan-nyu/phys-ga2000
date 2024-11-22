import numpy as np
import matplotlib.pyplot as plt

def f(r, t, args):
    x = r[0]
    xp = r[1]
    y = r[2]
    yp = r[3]

    B = args[0]
    
    dxdt = xp
    dydt = yp

    dxpdt = -np.pi/2*B*xp*np.sqrt(xp**2+yp**2)
    dypdt = -1 -np.pi/2*B*yp*np.sqrt(xp**2+yp**2)
    
    return np.array([dxdt, dxpdt, dydt, dypdt], float)


def solve(f, r0, args, t0=1, tf=50, N=10000):

    h = (tf - t0)/N

    tpoints = np.arange(t0, tf, h)
    xpoints = []
    ypoints = []

    r = np.array(r0, float)

    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[2])
    
        k1 = h*f(r, t, args)
        k2 = h*f(r+0.5*k1,t+0.5*h, args)
        k3 = h*f(r+0.5*k2, t+0.5*h, args)
        k4 = h*f(r+k3, t+h, args)
        r += (k1 + 2*k2 + 2*k3 + k4)/6

        if r[2] < 0:
            break
    
    return (tpoints, xpoints, ypoints)

def partB():
    R = 0.08
    rho = 1.22
    C = 0.47
    g = 9.8
    T = 1
    m = 1

    B = R**2 * rho * C * g * T**2/m

    v0 = 100
    theta = 30
    r0 = [0, v0*np.cos(theta * np.pi/180), 0, v0*np.sin(theta*np.pi/180)]

    ts, xs, ys = solve(f, r0, [B])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(xs, ys)
    plt.show()

partB()

def partC():
    Bs = [1, 1/2, 1/4, 1/8]
    v0=1
    theta = 30
    r0 = [0, v0*np.cos(theta * np.pi/180), 0, v0*np.sin(theta*np.pi/180)]
    for B in Bs:
        ts, xs, ys = solve(f, r0, [B])
        plt.plot(xs, ys)
    plt.legend(Bs)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

partC()