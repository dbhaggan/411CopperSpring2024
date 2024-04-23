from django.contrib import admin
# from .models import User, SheetMusic, Note, SheetMusicNote, UserProgress, Feedback, Instrument, InstrumentNote, PracticeSession
from .models import Instrument, InstrumentNote, User
from .models import MIDIFile, MIDINote, AudioFile, AudioNote

#admin.site.register(MIDIFile)
#admin.site.register(MIDINote)
#admin.site.register(AudioFile)
#admin.site.register(AudioNote)

# admin.site.register(User)
# admin.site.register(SheetMusic)
# admin.site.register(Note)
# admin.site.register(SheetMusicNote)
# admin.site.register(UserProgress)
# admin.site.register(Feedback)
#admin.site.register(Instrument)
#admin.site.register(InstrumentNote)
# admin.site.register(PracticeSession)

#timpani = Instrument.objects.create(name='Timpani', family='Percussion', pitched=True)
#marimba = Instrument.objects.create(name='Marimba', family='Percussion', pitched=True)
#bells = Instrument.objects.create(name='Bells (Glockenspiel)', family='Percussion', pitched=True)
#snare_drum = Instrument.objects.create(name='Snare Drum', family='Percussion', pitched=False)
#drumset = Instrument.objects.create(name='Drumset', family='Percussion', pitched=False)


#InstrumentNote.objects.create(instrument=timpani, note='C', octave='4', duration='Quarter Note')
#InstrumentNote.objects.create(instrument=marimba, note='G', octave='3', duration='Eighth Note')
#InstrumentNote.objects.create(instrument=bells, note='C#', octave='5', duration='Half Note')
#InstrumentNote.objects.create(instrument=snare_drum, note='Snare', octave='', duration='Sixteenth Note')
#InstrumentNote.objects.create(instrument=drumset, note='Kick Drum', octave='', duration='Whole Note')

# Creating MIDI Files
#correct_midi = MIDIFile.objects.create(type='correct', name='Mozart Sonata No. 11')
#incorrect_midi = MIDIFile.objects.create(type='incorrect', name='Mozart Sonata No. 11 with Mistakes')

# Adding notes to the MIDI Files
#MIDINote.objects.create(midi_file=correct_midi, note='Bb', timing=1.00, correct=True)
#MIDINote.objects.create(midi_file=incorrect_midi, note='B', timing=1.00, correct=False)

# Creating Audio Files
#correct_audio = AudioFile.objects.create(type='correct', name='Beethoven Symphony No. 5')
#incorrect_audio = AudioFile.objects.create(type='incorrect', name='Beethoven Symphony No. 5 with Mistakes')

# Adding notes to the Audio Files
#AudioNote.objects.create(audio_file=correct_audio, note='G', timing=2.00, correct=True)
#AudioNote.objects.create(audio_file=incorrect_audio, note='G#', timing=2.00, correct=False)




#john = User.objects.create(firstName='John', lastName='Doe', userName='johndoe', passWord='password', emailAddress='john@example.com')

# Adding instruments to the user
#john.instruments.add(timpani)
#john.instruments.add(marimba)

# Accessing instruments associated with the user
#instruments_of_john = john.instruments.all()
#for instrument in instruments_of_john:
#    print(instrument.name)
