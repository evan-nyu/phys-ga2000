import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#Likelihood function
#Covariance is inverse of hessian
#standard error is sqrt of diagonals terms of covariance

data = np.genfromtxt('survey.csv', delimiter=',')[1::]
ages = np.transpose(data)[0]
answers = np.transpose(data)[1]

def p(x, b0, b1):
    return 1/(1+np.exp(-(b0+b1*x)))

def nlogL(b):
    b0, b1 = b
    ps = p(ages, b0, b1)
    return -np.sum(answers * np.log(ps) + (1-answers) * np.log(1-ps))

result = sp.optimize.minimize(nlogL, [-50, 1])

print("B0, B1", result.x)

print("Inverse Hessian", result.hess_inv)

print("B0 error", np.sqrt(result.hess_inv[0][0]))
print("B1 error", np.sqrt(result.hess_inv[1][1]))

print("Min Log Liklihood", result.fun)

plt.plot(np.sort(ages), p(np.sort(ages), result.x[0], result.x[1]), color="orange")
plt.scatter(ages, answers)
plt.legend(['Model', 'Data'])
plt.xlabel('Age')
plt.ylabel('Probability')
plt.show()

