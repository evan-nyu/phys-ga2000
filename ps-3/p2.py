import numpy as np
import matplotlib.pyplot as plt

class isotope:
    """Create a class to hold all of the info about each isotope"""
    def __init__(self, N, halfLife, product = None, product2 = None, product2Probability = 0):
        """Initialize an isotope class with a population number, half life, decay product, optional second decay product, and second decay product probability"""
        self.number = N
        self.decayP = 1 - 2**(-1 / (60*halfLife))
        self.product = product
        self.product2 = product2
        self.product2Probability = product2Probability / 100
        self.populationRecord = [] #using a python list for fast appending

    def decay(self):
        #Loop through every atom
        for i in range(self.number):
            #Check if it decays
            if np.random.rand() < self.decayP:
                #decrease self population
                self.number -= 1
                #Check if the decay has two possible products
                if self.product2 is not None:
                    #Check if product2 will be the choosen product
                    if np.random.rand() < self.product2Probability:
                        #Add an atom to product2
                        self.product2.add()
                        continue
                #Add an atom to the product
                self.product.add()

    def record(self):
        """Record the current population number and add it to the population record"""
        self.populationRecord.append(self.number)

    def add(self):
        self.number += 1

#Create a Bi209 isotope object with 0 population and a half life that will never be used
Bi209 = isotope(0, 1)

#create a Pb isotope with an initial population of 0, half life of 3.3 minutes, and a decay product of Bi209
Pb = isotope(0, 3.3, Bi209)

#Create Ti isotope with half life of 2.2 minutes, Pb decay product
Ti = isotope(0, 2.2, Pb)

#Create 213 Bi isotope with an inital population of 10000, half life of 46 minutes, decay product of Pb, second decay product of Ti, probability of 2nd decay product of 2.09%
Bi213 = isotope(10000, 46, Pb, Ti, 2.09)

time = 20000

for i in range(time):
    #Have each isotope decay
    Pb.decay()
    Ti.decay()
    Bi213.decay()

    #Record the numbers of each isotope
    Bi209.record()
    Pb.record()
    Ti.record()
    Bi213.record()

#Plot
plt.plot(Bi213.populationRecord, label="213 Bi")
plt.plot(Ti.populationRecord, label="209 Ti")
plt.plot(Pb.populationRecord, label="209 Pb")
plt.plot(Bi209.populationRecord, label="209 Bi")
plt.xlabel("Time (s)")
plt.ylabel("Population")
plt.legend()
plt.show()
