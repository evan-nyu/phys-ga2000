import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

N=1000 #Amount of sum for each y
M=10000 #How many y in ys

#Get a single y value from N xs from an exponential distribution
def get_y(N):
    return 1/N * np.sum(np.random.exponential(size = N))

#Get the sum of M y values
def get_ys(N, M):
    return [get_y(N) for _ in range(M)]


#empty arrays to hold to stuff
means = []
variances = []
skewnesses = []
kurtosises =[]

#List of Ns to loop through
Ns = np.arange(1, 1000, 2)
#Loop through Ns
for N in Ns:
    #Get ys and stats stuff for each N
    ys = get_ys(N, M)
    means.append(np.mean(ys))
    variances.append(np.var(ys))
    skewnesses.append(sp.stats.skew(ys))
    kurtosises.append(sp.stats.kurtosis(ys))

#Test Central Limit Theorem
#Generate ys with N=1000
ys = get_ys(1000, M)
#Setup an x axis for the gaussian
gaussian_xs = np.linspace(np.min(ys), np.max(ys), 100)
#Calculate the standard deviation from the ys
sigma = np.sqrt(np.var(ys))
#Get the y values of a gaussain
gaussian_ys = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(gaussian_xs - 1)**2 / (2 * sigma**2))

#plot a gaussian and a histogram of ys
plt.plot(gaussian_xs, gaussian_ys)
plt.hist(ys, bins = 50, density = True)
plt.show()

#Plottoing for the stats stuff as a function of N
figure, axis = plt.subplots(2, 2)
axis[0, 0].plot(Ns, means)
axis[0, 0].set_title("Mean")

axis[0, 1].plot(Ns, variances)
axis[0, 1].set_title("Variance")

axis[1, 0].plot(Ns, skewnesses)
axis[1, 0].set_title("Skewness")

axis[1, 1].plot(Ns, kurtosises)
axis[1, 1].set_title("Kurtosis")

plt.show()

#get where skewness is 0.01 of its original value
print("First N where Skewness < 0.01 of original value", Ns[skewnesses < 0.01 * skewnesses[0]][0])

#get where kurtosis is 0.01 of its original value
print("First N where Kurtosis < 0.01 of original value", Ns[kurtosises < 0.01 * kurtosises[0]][0])
