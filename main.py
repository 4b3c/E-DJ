import sounddevice as sd
from pydub import AudioSegment
import numpy as np

# Read the audio file
audio = AudioSegment.from_file('C:/Users/Abram P/Desktop/Programming/Python_scripts/sound/E-DJ/MeizongHelios.wav', format='wav')

# Split from 3 to 8 seconds of the audio
sliced_audio = audio[3000:10000]

# Adjust the playback speed
adjusted_audio = sliced_audio.speedup(playback_speed=1.2)

# Convert the adjusted audio to raw data
raw_data = np.array(adjusted_audio.get_array_of_samples())

# Play the edited audio in real-time
sd.play(raw_data, adjusted_audio.frame_rate)
sd.wait()
