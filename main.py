import numpy as np
import math
import sounddevice as sd

frequency = 200
sample_rate = 44100
duration = 0.7
volume = 0.003

t = np.arange(int(sample_rate * duration))
raw_data = np.sin(2 * np.pi * frequency * t / sample_rate) * volume
raw_data += np.where(raw_data > 0, 1, -1)

sd.play(raw_data, sample_rate)
sd.wait()
