import pygame

# initializing pygame
pygame.init()

# loading soundfont
pygame.mixer.init()
soundfont = "C:\\Users\\imism\\411CopperSpring2024\\percussatsight\\percussatsight\\Marimba.sf2"
pygame.mixer.music.load(soundfont)

# loading midi file
midi_file = "C:\\Users\\imism\\411CopperSpring2024\\percussatsight\\percussatsight\\Correctly_Played_Example.mid"

# playing midi file through mixer
pygame.mixer.music.load(midi_file)
pygame.mixer.music.play()
