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