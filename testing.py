import numpy as np
import sounddevice as sd

def generate_audio(frequency, duration, sample_rate):
    t = np.arange(int(sample_rate * duration), dtype=float64) / sample_rate
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

def play_audio(stream, data):
    stream.write(data)


sample_rate = 44100  # You can adjust this based on your requirements
duration = 1.0
frequency = 440.0

stream = sd.OutputStream(channels=1, callback=lambda *args: None, samplerate=sample_rate)
stream.start()

try:
    while True:
        # Get the new frequency from your variable
        frequency = 440

        # Generate audio with the updated frequency
        audio_data = generate_audio(frequency, duration, sample_rate)

        # Play the audio
        play_audio(stream, audio_data)
except KeyboardInterrupt:
    print("Exiting...")
