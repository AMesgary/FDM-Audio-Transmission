import os
import sounddevice as sd
from scipy.io import wavfile

os.makedirs("data", exist_ok=True)

fs = 44100
duration = 10
print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
wavfile.write("data/audio_1.wav", fs, audio)
print("Finished!")