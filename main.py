import numpy as np
import math
import sounddevice as sd

frequency = 440
sample_rate = 44100
duration = 5
volume = 0.05

t = np.arange(int(sample_rate * duration))
raw_data = np.sin(2 * np.pi * frequency * (t**(1/1.2)) / sample_rate) * volume

print(raw_data[:10])

sd.play(raw_data, sample_rate)
sd.wait()
