import pygame
import os
os.environ["PYGAME_MIDI"] = "alsa"

def play_midi(midi_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()

if __name__ == "__main__":
    midi_file = "percussatsight/Correctly_Played_Example.mid"
    play_midi(midi_file)