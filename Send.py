import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

FS = 44100
FC = [5000, 12000, 19000]

def normalize(data):
    if data.dtype == np.int16:
        return data.astype(np.float32) / 32768.0
    return data.astype(np.float32)

def quantize_signal(audio, bits):
    Q = 2**(bits-1) - 1
    audio_q = np.round(audio * Q) / Q
    return audio_q

_, audio1 = wavfile.read("audio_1.wav")
_, audio2 = wavfile.read("audio_2.wav")
_, audio3 = wavfile.read("audio_3.wav")

audio1 = normalize(audio1)
audio2 = normalize(audio2)
audio3 = normalize(audio3)


# ========== Quantization ==========

audio1_3bit = quantize_signal(audio1, 3)

wavfile.write("audio_1_3bit.wav", FS, audio1_3bit.astype(np.float32))

peak_indx = np.argmax(np.abs(audio1))
half_window = int(0.1 * FS)
lower_bound = max(0, peak_indx - half_window)
upper_bound = min(len(audio1), peak_indx + half_window)

t = np.arange(len(audio1)) / FS
sample_time = t[lower_bound : upper_bound]

plt.figure(figsize=(10, 5))
plt.plot(sample_time, audio1[lower_bound : upper_bound], color="b", alpha=0.5, label="Original")
plt.plot(sample_time, audio1_3bit[lower_bound : upper_bound], color="r", alpha=0.5, label="3-bit Quantized")
plt.title("Quantization Effect (200ms Window)")
plt.legend()
plt.grid(True)
plt.savefig("plot_quantization_compare.png")
plt.close()

audio1_8bit = quantize_signal(audio1, 8)
audio2_8bit = quantize_signal(audio2, 8)
audio3_8bit = quantize_signal(audio3, 8)

audio_signals_8bit = [audio1_8bit, audio2_8bit, audio3_8bit]

# ========== Modulation ==========

t = np.arange(len(audio1)) / FS
y_total = np.zeros(len(audio1))

for i in range(3):
    carrier = np.cos(2 * np.pi * FC[i] * t)
    y_total += audio_signals_8bit[i] * carrier


plt.figure(figsize=(10, 4))
y_total_fft = np.fft.fft(y_total)
freq = np.fft.fftfreq(len(y_total), 1/FS)

half_n = len(y_total) // 2
plt.plot(freq[:half_n], np.abs(y_total_fft)[:half_n])
plt.title("Spectrum of FDM Signal (y_total)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.savefig("plot_fdm_spectrum.png")
plt.close()

wavfile.write("y_total.wav", FS, y_total.astype(np.float32))