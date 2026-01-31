import numpy as np
import matplotlib.pyplot as plt

fs = 1000
f0 = 50
T = 1

t = np.arange(0, T, 1/fs)
x = np.sin(2 * np.pi * f0 * t)

X = np.fft.fft(x)
freq = np.fft.fftfreq(len(x), 1/fs)

plt.figure()
plt.stem(freq, np.abs(X))
plt.xlim(-100, 100)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT of a sinusoid")
plt.grid(True)
plt.show()
