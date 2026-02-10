import os
import numpy as np
from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt

os.makedirs("data", exist_ok=True)
os.makedirs("plots", exist_ok=True)

FS = 44100
nyq = 0.5 * FS
FC2 = 12000
ORDER = 200

try:
    fs, y_total = wavfile.read("data/y_total.wav")
except FileNotFoundError:
    exit("Error: y_total.wav not found.")

low, high = 9000, 15000

b_bp = signal.firwin(ORDER + 1, [low/nyq, high/nyq], pass_zero=False)

extracted_y2 = signal.lfilter(b_bp, 1, y_total)

wavfile.write("data/extracted_y2.wav", FS, extracted_y2.astype(np.float32))

plt.figure(figsize=(10, 5))
y_fft = np.fft.fft(extracted_y2)
freq = np.fft.fftfreq(len(extracted_y2), 1/FS)
half_n = len(extracted_y2) // 2

plt.plot(freq[:half_n], np.abs(y_fft)[:half_n])
plt.title("Spectrum after Band-pass Filtering")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.xlim(0, FS/2)

plt.savefig("plots/plot_filtered_spectrum.png")
plt.close()

t = np.arange(len(y_total)) / FS

demod_raw = extracted_y2 * np.cos(2 * np.pi * FC2 * t) * 2

lpf_cutoff = 4000
b_lp = signal.firwin(ORDER + 1, lpf_cutoff/nyq)

recovered_audio2 = signal.lfilter(b_lp, 1, demod_raw)

wavfile.write("data/recovered_audio2.wav", FS, recovered_audio2.astype(np.float32))

try:
    _, audio_original = wavfile.read("data/audio_2.wav")
    
    if audio_original.dtype == np.int16:
        audio_original = audio_original.astype(np.float32) / 32768.0
    else:
        audio_original = audio_original.astype(np.float32)

    min_len = min(len(audio_original), len(recovered_audio2))
    t_plot = t[:min_len]
    
    plt.figure(figsize=(12, 6))
    
    plt.plot(t_plot, audio_original[:min_len], color='red', alpha=0.7, label="Original (Audio 2)")
    
    plt.plot(t_plot, recovered_audio2[:min_len], color='blue', alpha=0.7, label="Recovered (From Receiver)")
    
    plt.title("Time Domain Comparison: Original vs. Recovered Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    
    plt.savefig("plots/plot_time_comparison.png")
    plt.close()

except FileNotFoundError:
    pass