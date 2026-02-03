from scipy.io import wavfile
from matplotlib import pyplot as plt 
import numpy as np

bits = 8

fs, audio = wavfile.read("audio_1.wav")
t = np.arange(len(audio)) / fs

plt.figure()

peak_indx = np.argmax(audio)
lower_bound = peak_indx - (int)(0.1*fs)
upper_bound = peak_indx + (int)(0.1*fs)
peak_sample = audio[lower_bound : upper_bound]
sample_time = t[lower_bound : upper_bound]

Q = 2**(bits-1)-1
audioq = np.round(audio * Q) / Q

plt.plot(sample_time, peak_sample, color="b", alpha=0.5)
plt.plot(sample_time, audioq[lower_bound : upper_bound], color="r", alpha=0.5)
plt.grid(True)
plt.show()

wavfile.write(f"audio_1_{bits}bit.wav", fs, audioq.astype(np.float32))
