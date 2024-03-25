from django.contrib import admin
# from .models import User, SheetMusic, Note, SheetMusicNote, UserProgress, Feedback, Instrument, InstrumentNote, PracticeSession
from .models import Instrument, InstrumentNote


# admin.site.register(User)
# admin.site.register(SheetMusic)
# admin.site.register(Note)
# admin.site.register(SheetMusicNote)
# admin.site.register(UserProgress)
# admin.site.register(Feedback)
admin.site.register(Instrument)
admin.site.register(InstrumentNote)
# admin.site.register(PracticeSession)

timpani = Instrument.objects.create(name='Timpani', family='Percussion', pitched=True)
marimba = Instrument.objects.create(name='Marimba', family='Percussion', pitched=True)
bells = Instrument.objects.create(name='Bells (Glockenspiel)', family='Percussion', pitched=True)
snare_drum = Instrument.objects.create(name='Snare Drum', family='Percussion', pitched=False)
drumset = Instrument.objects.create(name='Drumset', family='Percussion', pitched=False)


InstrumentNote.objects.create(instrument=timpani, note='C', octave='4', duration='Quarter Note')
InstrumentNote.objects.create(instrument=marimba, note='G', octave='3', duration='Eighth Note')
InstrumentNote.objects.create(instrument=bells, note='C#', octave='5', duration='Half Note')
InstrumentNote.objects.create(instrument=snare_drum, note='Snare', octave='', duration='Sixteenth Note')
InstrumentNote.objects.create(instrument=drumset, note='Kick Drum', octave='', duration='Whole Note')
