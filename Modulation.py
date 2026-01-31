from scipy.io import wavfile
from matplotlib import pyplot as plt 
import numpy as np

plt.figure()

fs = 0
fs, audio1 = wavfile.read("audio_1_8bit.wav")
fs, audio2 = wavfile.read("audio_2_8bit.wav")
fs, audio3 = wavfile.read("audio_3_8bit.wav")

t = np.arange(len(audio1)) / fs

fc1, fc2, fc3 = 5000, 12000, 19000

audio1_shifted = audio1 * np.cos(2 * np.pi * fc1 * t)
audio2_shifted = audio2 * np.cos(2 * np.pi * fc2 * t)
audio3_shifted = audio3 * np.cos(2 * np.pi * fc3 * t)

fft1 = np.fft.fft(audio1_shifted)
freq = np.fft.fftfreq(len(audio1_shifted), 1/fs)
#plt.stem(freq, np.abs(X1), linefmt='r-', markerfmt='ro', basefmt='k-')


fft2 = np.fft.fft(audio2_shifted)
#plt.stem(freq, np.abs(X), linefmt='g-', markerfmt='go', basefmt='k-')

fft3 = np.fft.fft(audio3_shifted)
#plt.stem(freq, np.abs(X), linefmt='b-', markerfmt='bo', basefmt='k-')

fft_sum = fft1 + fft2 + fft3

#plt.stem(freq, np.abs(fft_sum), linefmt='b-', markerfmt='bo', basefmt='k-')
plt.plot(freq, np.abs(fft_sum))

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT of a sinusoid")
plt.grid(True)
plt.show()