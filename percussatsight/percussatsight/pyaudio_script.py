# this is the script with the code to use the pyaudio api
import pyaudio
import wave

# Define audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
FILE_PATH = "input.wav"

# Initialize pyaudio
p = pyaudio.PyAudio()

# Open the audio file
wf = wave.open(FILE_PATH, 'rb')

# Open stream
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

print("* Playing audio...")

# Read data from file and play
data = wf.readframes(CHUNK)
while data:
    stream.write(data)
    data = wf.readframes(CHUNK)

print("* Finished playing")

# Stop stream
stream.stop_stream()
stream.close()
p.terminate()