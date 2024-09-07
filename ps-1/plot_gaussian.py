import matplotlib.pyplot as plt
import numpy as np

sigma = 3
mu = 0
min = -10
max = 10
num = 100

x = np.linspace(min, max, num)

def normal(x, sigma, mu):
    return 1/(sigma * np.sqrt(2 * np.pi)) * np.e**(-1/2*((x - mu)/sigma)**2)

y = normal(x, sigma, mu)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gaussian")
plt.show()
