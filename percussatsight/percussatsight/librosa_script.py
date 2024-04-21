import librosa
import numpy as np
import pandas as pd

# extracting notes from audio file
def extract_notes(audio_file):
    y, sr = librosa.load(audio_file)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    notes = np.argmax(chroma, axis=0)
    return notes

# our audio files
correct_audio_file = 'music_sample.wav'
incorrect_audio_file = 'Incorrectly_Played_Sample.wav'

# extracting notes from the audio files
correct_notes = extract_notes(correct_audio_file)
incorrect_notes = extract_notes(incorrect_audio_file)

# note names
note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# converting notes to note names
correct_note_names = [note_names[note] for note in correct_notes]
incorrect_note_names = [note_names[note] for note in incorrect_notes]

# storing notes in tables (Pandas DataFrames)
correct_notes_df = pd.DataFrame({'Notes': correct_note_names})
incorrect_notes_df = pd.DataFrame({'Notes': incorrect_note_names})

# printing extracted notes
print("Correctly Played Example:")
print(correct_note_names)
print("\nIncorrectly Played Example:")
print(incorrect_note_names)