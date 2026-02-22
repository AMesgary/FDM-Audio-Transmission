# Multi-Channel FDM Communication System

A Python implementation of a complete Frequency Division Multiplexing (FDM) telecommunication chain. This project simulates the process of transmitting multiple audio signals simultaneously over a single channel by modulating them onto distinct carrier frequencies, and subsequently recovering a specific target signal using digital filters.

## Features

* **Quantization Analysis:** Compares the effect of bit-depth on signal quality (8-bit vs. 3-bit) and visualizes quantization noise.
* **FDM Modulation:** Modulates three separate audio channels onto 5kHz, 12kHz, and 19kHz carrier frequencies.
* **Nyquist Theorem & Aliasing:** Demonstrates frequency folding and signal distortion by intentionally undersampling the composite signal.
* **Signal Recovery:** Uses a custom FIR bandpass filter to isolate a specific channel, followed by synchronous demodulation and lowpass filtering to reconstruct the original audio.

## Requirements

To run the scripts, you will need Python 3 and the following libraries installed:

```bash
pip install numpy scipy matplotlib sounddevice

```

## Workflow and Usage

The system is divided into four main standalone scripts. Running them will automatically create `data/` and `plots/` directories to store the outputs.

**1. Prepare Audio Data**
Use `Recorder.py` to record three 10-second audio samples. Ensure they are saved as `audio_1.wav`, `audio_2.wav`, and `audio_3.wav` inside the `data/` directory.

**2. Transmit (Modulation)**
Run `Send.py`. This script quantizes the audio inputs, modulates them onto their respective carriers, and sums them into a single composite signal (`y_total.wav`). It also generates time-domain and frequency spectrum plots.

**3. Receive (Demodulation)**
Run `Receive.py`. This acts as the receiver targeting the 12kHz channel (Audio 2). It applies a bandpass filter to isolate the signal, demodulates it, and applies a lowpass filter. The recovered audio is saved as `recovered_audio2.wav` alongside a plot comparing it to the original input.

**4. Aliasing Analysis**
Run `Nyquist.py`. This script reads the composite signal and downsamples it to 22050 Hz (below the Nyquist rate) to visualize how high frequencies fold back and corrupt the lower frequencies.
