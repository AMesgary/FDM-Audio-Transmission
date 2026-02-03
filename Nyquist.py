import os
import numpy as np
import scipy.signal as signal
from scipy.io import wavfile
import matplotlib.pyplot as plt

os.makedirs("data", exist_ok=True)
os.makedirs("plots", exist_ok=True)

FS = 44100
TARGET_FS_LOW = 22050

try:
    fs, y_total = wavfile.read("data/y_total.wav")
except FileNotFoundError:
    exit("Error: y_total.wav not found. Run Sender first.")

num_samples_low = int(len(y_total) * TARGET_FS_LOW / FS)

y_aliased = signal.resample(y_total, num_samples_low)

def get_fft_data(sig, sample_rate):
    N = len(sig)
    yf = np.fft.fft(sig)
    xf = np.fft.fftfreq(N, 1/sample_rate)
    half_n = N // 2
    return xf[:half_n], np.abs(yf)[:half_n]

f_orig, mag_orig = get_fft_data(y_total, FS)

f_alias, mag_alias = get_fft_data(y_aliased, TARGET_FS_LOW)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(f_orig, mag_orig, color='blue')
ax1.set_title(f"Original Signal Spectrum (FS={FS} Hz) - No Aliasing")
ax1.set_xlabel("Frequency (Hz)")
ax1.set_ylabel("Magnitude")
ax1.grid(True)

ax2.plot(f_alias, mag_alias, color='red')
ax2.set_title(f"Undersampled Signal Spectrum (FS={TARGET_FS_LOW} Hz) - Aliasing Visible")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude")
ax2.grid(True)

plt.tight_layout()

plt.savefig("plots/plot_nyquist_analysis.png")
plt.close()