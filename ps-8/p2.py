import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

sample_rate = 44100 #hz
delta = 1/sample_rate
piano = np.genfromtxt("piano.txt", delimiter="\n")
trumpet = np.genfromtxt("trumpet.txt", delimiter="\n")

def plotFFt(data, label):
    t = np.linspace(0, len(data)/sample_rate, len(data))

    plt.plot(t, data)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(label)
    plt.show()

    fft = np.fft.rfft(data)
    f = np.linspace(0, sample_rate/2, len(data)//2+1)

    print(f"{label} Dominant Frequeny", f[np.argmax(fft)])

    plt.plot(f, fft*delta)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.title(label)
    plt.show()

plotFFt(piano, 'Piano')
plotFFt(trumpet, 'Trumpet')

sd.play(piano/np.max(piano), sample_rate)
sd.wait()

sd.play(trumpet/np.max(trumpet), sample_rate)
sd.wait()
