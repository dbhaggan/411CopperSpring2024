import librosa
import numpy as np

# Function to extract notes from audio file
def extract_notes(audio_file):
    y, sr = librosa.load(audio_file)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    notes = np.argmax(chroma, axis=0)
    return notes

# Function to filter out incorrect notes and replace equivalent notes
def filter_notes(notes):
    # Define the set of correct notes
    correct_note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    # Replace 'Db' with 'C#' and filter out incorrect notes
    filtered_notes = [correct_note_names[note % 12] for note in notes]
    return filtered_notes

# Function to format notes as a string
def format_notes(note_names):
    return ' '.join(note_names)

# Example audio files
#correct_audio_file = 'music_sample.wav'
#incorrect_audio_file = 'Incorrectly_Played_Sample.wav'

# Extract notes from audio files
#correct_notes = extract_notes(correct_audio_file)
#incorrect_notes = extract_notes(incorrect_audio_file)

# Filter and replace notes
#correct_notes_filtered = filter_notes(correct_notes)
#incorrect_notes_filtered = filter_notes(incorrect_notes)

# Format notes as strings
#correct_notes_str = format_notes(correct_notes_filtered)
#incorrect_notes_str = format_notes(incorrect_notes_filtered)

# Print final output
#print("Final Output:\n")
#print("For Correctly Played Example:\n")
#print(correct_notes_str)
#print("\nFor Incorrectly Played Example:\n")
#print(incorrect_notes_str)
