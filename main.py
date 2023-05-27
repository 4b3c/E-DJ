import numpy as np
import math
import sounddevice as sd

frequency = 440
sample_rate = 44100
duration = 2
volume = 0.003

t = np.arange(int(sample_rate * duration))

print(t.shape)

raw_data = np.sin(2 * np.pi * frequency * t / sample_rate) * volume
bop = (np.sin((2 * np.pi * frequency * (t[0:20000] - 5000)) / sample_rate) * (10000 / ((t[0:20000] - 5000)**0.56))) / 17.915
print(bop.shape)

raw_data[20000:20000 + bop.shape[0]] += bop
print(raw_data[25000])

sd.play(raw_data, sample_rate)
sd.wait()

