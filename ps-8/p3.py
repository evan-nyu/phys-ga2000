import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('dow.txt', delimiter='\n')
x = np.arange(0, len(data), 1)
N = len(data)

plt.plot(x, data)
plt.xlabel('Day')
plt.ylabel('Closing Value')
plt.show()

fft = np.fft.rfft(data)

f = np.linspace(0, 1/2, N//2+1)

plt.plot(f, fft)
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Amplitude')
plt.xlabel('Frequency')
plt.show()

fft10 = np.copy(fft)
fft10[len(fft)//10:] = 0

data10 = np.fft.irfft(fft10)

fft2 = np.copy(fft)
fft2[len(fft)//50:] = 0

data2 = np.fft.irfft(fft2)

plt.plot(x, data)
plt.plot(x, data10)
plt.plot(x, data2)
plt.legend(['Original Data', '10% of Fourier Coefficients', '2% of Fourier Coefficients'])
plt.xlabel('Days')
plt.ylabel('Daily Closing Value')
plt.show()
