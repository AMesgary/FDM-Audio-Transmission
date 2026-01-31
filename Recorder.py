import sounddevice as sd
from scipy.io import wavfile

fs = 44100
duration = 10
print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
wavfile.write("audio_3.wav", fs, audio)
print("Finished!")