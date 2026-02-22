# Multi-Channel FDM Communication System

A Python implementation of a complete Frequency Division Multiplexing (FDM) telecommunication chain. This project simulates the process of transmitting multiple audio signals simultaneously over a single channel by modulating them onto distinct carrier frequencies, and subsequently recovering a specific target signal using digital filters.

## Features & Technical Implementation

* **Quantization Analysis:** Reads the raw `.wav` files, normalizes the amplitude to a float32 range of [-1.0, 1.0], and implements a custom quantization function. The script mathematically maps the continuous audio values to discrete levels to simulate 8-bit depth for transmission and 3-bit depth to calculate and visualize quantization noise.
* **FDM Modulation (Transmitter):** Implements Double Sideband Suppressed Carrier (DSB-SC) modulation using numpy array operations. The script generates time arrays based on the 44.1kHz sample rate, creates cosine wave arrays for the 5kHz, 12kHz, and 19kHz carriers, multiplies them element-wise with the 8-bit audio data, and sums them to create the single composite signal.
* **Nyquist Theorem & Aliasing:** Uses the `scipy.signal.resample` function to intentionally downsample the composite signal from 44.1kHz to 22.05kHz. It then computes the Fast Fourier Transform using `np.fft.fft` and `fftfreq` to visually and mathematically demonstrate frequency folding when the sampling rate drops below the required Nyquist limit.
* **Signal Recovery (Receiver):** Utilizes `scipy.signal.firwin` to design a 200th-order FIR bandpass filter (9kHz–15kHz) and applies it to the composite signal using `scipy.signal.lfilter` to isolate the 12kHz channel. Synchronous demodulation is achieved by multiplying the extracted array by the local carrier, followed by passing the result through a 4kHz FIR lowpass filter to reconstruct the original baseband audio.

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
