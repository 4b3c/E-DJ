import numpy as np
import math
import sounddevice as sd

frequency = 20
sample_rate = 44000
duration = 1
volume = 0.05

t = np.arange(int(sample_rate * duration))
raw_data = np.sin(2 * np.pi * frequency * t / sample_rate) * volume

print(raw_data[:10])

sd.play(raw_data, sample_rate)
sd.wait()
