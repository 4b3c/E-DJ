import numpy as np
import math
import sounddevice as sd

sample_rate = 44100
duration = 3
volume = 0.03

t = np.arange(int(sample_rate * duration))
raw_data = np.sin(2 * np.pi * 261.63 * t / sample_rate) * volume
raw_data += np.sin(2 * np.pi * 329.63 * t / sample_rate) * volume
raw_data += np.sin(2 * np.pi * 392.00 * t / sample_rate) * volume


sd.play(raw_data, sample_rate)
sd.wait()

#https://www.desmos.com/calculator/qvqjpurbp1