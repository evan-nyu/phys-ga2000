import re
import numpy as np
import matplotlib.pyplot as plt

with open('signal.dat', 'r') as file:
    #Convert raw data into a list of string containing no white space or |
    #The regex took me longer than I want to admit to get right
    strData = str.split(re.sub("\\||\n", " ", file.read()))

    #convert from string to double
    data = np.asarray(strData)[2::].astype('d')

    #reshape to get separate signal and time arrays
    times, signals = np.transpose(data.reshape((-1, 2)))

    plt.scatter(times, signals)
    plt.xlabel("Time (time units)")
    plt.ylabel("Signal (signal units)")
    plt.show()


def fit(t, s, terms, type='l'):
    '''fit s as a function of t with terms terms in the series and l for standard linear and f for fourier like fit'''

    #Rescele time
    tp = (t - t.mean())/t.std()

    #Setup fit
    A = np.zeros((len(tp), terms +1))
    A[:, 0] = 1
    
    if type == "l":
        for i in range(1, terms+1):
            A[:, i] = tp**i

    if type == 'f':
        #Setup sin fit
        P = (np.max(tp)-np.min(tp))/2
        for i in range(1, terms):
            if(i%2==0):
                A[:, i] = np.sin(2*np.pi*(i//2)/P*tp)
            else:
                A[:, i] = np.cos(2*np.pi*(i//2+1)/P*tp)

    #Numpy do magic
    u, w, vt = np.linalg.svd(A, full_matrices=False)
    #replace 0 with infty so no errors
    w = np.where(w != 0, w, np.inf)
    #print c
    c = w.max() / w.min()
    print(c)
    #more numpy magic
    ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
    x = ainv.dot(s)
    s_fit = A.dot(x)

    return s_fit

def residuals(data, fit):
    return data - fit

plt.scatter(times, signals)
fit = fit(times, signals, 20, 'f')
plt.scatter(times, fit)
plt.scatter(times, residuals(signals, fit), marker=".")
plt.xlabel("time")
plt.ylabel("signal")
plt.legend(["Data", "Fit", "Residuals"])
plt.show()

