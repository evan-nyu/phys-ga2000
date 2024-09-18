import numpy as np
import matplotlib.pyplot as plt

#number of points
N = 1000

#max iterations
max_iter = 100


def iterate(x, y):
    c = x + y
    z = 0
    for _ in range(max_iter):
        #Used where to only preform recursive equation when |z| < 2
        z = np.square(z, where=(np.absolute(z) < 2)) + c
    return np.absolute(z) > 2

xs, ys = np.meshgrid(np.linspace(-2, 2, N, dtype=np.float64), 1j*np.linspace(-2, 2, N, dtype=np.float64))

zs = iterate(xs, ys)

plt.imshow(zs)
plt.xticks([0, N/2, N], ['-2', '0', '2'])
plt.xlabel("Real")
plt.yticks([0, N/2, N], ['-2', '0', '2'])
plt.ylabel("Imaginary")
plt.show()
