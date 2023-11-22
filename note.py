import numpy as np
import sounddevice as sd

frequency = 440
sample_rate = 44100
duration = 3
volume = 0.03

t = np.arange(int(sample_rate * duration))

col_input = 2 * np.pi * frequency * t / sample_rate
raw_data = np.sin(col_input) * volume

# (np.cos(col_input) * np.e**np.sin(col_input))
# (abs(np.sin(col_input) / np.cos(col_input / 5)**2))


sd.play(raw_data, sample_rate)
sd.wait()
