import numpy as np
import matplotlib.pyplot as plt

#Half-life in seconds
tau = 3.053 * 60
mu = np.log(2)/tau

#get a list of 1000 decay times using eq 10.10 from Newman
decayTimes = - 1/mu * np.log(1 - np.random.rand(1000))

# Generate an array of time values
tmax = np.max(decayTimes)
times = np.arange(0, tmax, 5)

#empty python list to hold the number of remaining atoms at each time
remaining = []

for t in times:
    #for each time, append the number of remaining atoms (with decay time > t) to remaining
    remaining.append(len(np.extract(decayTimes > t, decayTimes)))

#Plot
plt.plot(times, remaining)
plt.xlabel("Times")
plt.ylabel("Remaining Atoms")
plt.show()
