import numpy as np
import matplotlib.pyplot as plt
import time

def slowMult(A, B):
    """slow matrix multiplication method from the textbook"""
    # Example from book
    N = len(A)
    C = np.zeros([N, N], float)

    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]

def timeit(N):
    """returns the times it takes for the fast and slow methods to multiply two random NxN matrices"""
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    initial = time.time()
    slowMult(A, B)
    slowMultTime = time.time() - initial

    initial = time.time()
    np.dot(A, B)
    dotTime = time.time() - initial

    return (slowMultTime, dotTime)

#Test with matrices of size 10x10 to size 200x200 in increments of 10
Ns = np.arange(10, 200, 10, dtype='i')
slowMultTimes = np.zeros(len(Ns))
dotTimes = np.zeros(len(Ns))

for i, N in enumerate(Ns):
    slowMultTimes[i], dotTimes[i] = timeit(N)

print(slowMultTimes)
print(dotTimes)


#time vs N
plt.plot(Ns, slowMultTimes, label="Slow Method")
plt.plot(Ns, dotTimes, label="Numpy Dot")
plt.xlabel("N")
plt.ylabel("Time Taken")
plt.legend()
plt.show()

#Plot cube root of time vs N - should be linear since matrix stuff happens in N^3
plt.plot(Ns, np.power(slowMultTimes, 1/3), label="Slow Method")
plt.plot(Ns, np.power(dotTimes, 1/3), label="Numpy Dot")
plt.xlabel("N")
plt.ylabel("Cube Root of Time Taken")
plt.legend()
plt.show()
