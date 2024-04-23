import pyaudio
import wave

# defining audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
FILE_PATH = "music_sample.wav"

# initializing pyaudio
p = pyaudio.PyAudio()

# opening the audio file
wf = wave.open(FILE_PATH, 'rb')

# opening stream
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

print("* Playing audio...")

# reading data from file and playing
data = wf.readframes(CHUNK)
while data:
    stream.write(data)
    data = wf.readframes(CHUNK)

print("* Finished playing")

# stopping stream
stream.stop_stream()
stream.close()
p.terminate()