import math
import sounddevice as sd
import numpy as np

notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
durations = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.7]

frequency = 440
sample_rate = 44100
volume = 0.1
fade_duration = 0.01

fade_samples = int(sample_rate * fade_duration)

t = np.arange(int(sample_rate * durations[0]))
raw_data = np.sin(2 * np.pi * notes[0] * t / sample_rate) * volume

for frequency, duration in zip(notes[1:], durations[1:]):
	t = np.arange(int(sample_rate * duration))
	new_note = np.sin(2 * np.pi * frequency * t / sample_rate) * volume
	raw_data[-fade_samples:] *= np.linspace(1, 0, fade_samples)
	new_note[:fade_samples] *= np.linspace(0, 1, fade_samples)
	raw_data = np.concatenate((raw_data, new_note))

sd.play(raw_data, sample_rate)
sd.wait()