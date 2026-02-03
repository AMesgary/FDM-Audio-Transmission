from scipy import signal
from scipy.io import wavfile
from matplotlib import pyplot as plt 
import numpy as np

plt.figure()

fs, y_total = wavfile.read("y_total.wav")

nyq = 0.5 * fs
low, high = 9000, 15000
order = 200
b_bp = signal.firwin(order+1, [low/nyq, high/nyq], pass_zero=False)
extracted_y2 = signal.lfilter(b_bp, 1, y_total)

wavfile.write("extracted_y2.wav", fs, extracted_y2.astype(np.float32))

fc2 = 12000
t = np.arange(len(y_total)) / fs
demod_raw = extracted_y2 * np.cos(2 * np.pi * fc2 * t) * 2
b_lp = signal.firwin(201, 4000/nyq)
recovered_audio2 = signal.lfilter(b_lp, 1, demod_raw)

wavfile.write("recovered_audio2.wav", fs, recovered_audio2.astype(np.float32))

