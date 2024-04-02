import pygame
import pygame.midi

# initializing pygame
pygame.init()

#initializing the midi module
pygame.midi.init()

# creating a fluidsynth synthesizer instance
fs = pygame.midi.FluidSynth()

# loading a soundfont file
soundfont = "path_to_soundfont.sf2"  # later replace with the path to actual soundfont file
fs.load_soundfont(soundfont)

#loading midi file
midi_file = "path_to_midi_file.mid"  # later replace with the path to actual midi file

# open midi file
midi = pygame.midi.Midi(midi_file)

# play midi file through fluidsynth as audio
fs.play_midi(midi)