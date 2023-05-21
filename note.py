import numpy as np
import math
import sounddevice as sd

frequency = 440
sample_rate = 44100
duration = 3
volume = 0.03

t = np.arange(int(sample_rate * duration))
raw_data = np.sin(2 * np.pi * frequency * t / sample_rate) * volume


sd.play(raw_data, sample_rate)
sd.wait()
