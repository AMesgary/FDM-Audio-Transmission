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

y_total = audio1_shifted + audio2_shifted + audio3_shifted

y_total_fft = np.fft.fft(y_total)

plt.plot(freq, np.abs(y_total_fft))



wavfile.write("y_total.wav", fs, y_total.astype(np.float32))

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()