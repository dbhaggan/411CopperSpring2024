from django.db import models

class GeneratorSetting(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    picked_instrument = models.CharField(max_length=255)
    number_of_measures = models.IntegerField()
    clef_choice = models.CharField(max_length=10, choices=[('treble', 'Treble'), ('bass', 'Bass'), ('percussion', 'Percussion')])
    octaves = models.CharField(max_length=10, choices=[('/4', '4th Octave'), ('/5', '5th Octave')])
    additional_instruments = models.ManyToManyField('Instrument', related_name='generator_settings')
    randomize_sticking = models.BooleanField(default=False)
    rudiments = models.ManyToManyField('Rudiment', related_name='generator_settings')

class Rudiment(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    # sign up info
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    passWord = models.CharField(max_length=255)
    emailAddress = models.CharField(max_length=255)
    instruments = models.ManyToManyField('Instrument', related_name='users')

class Instrument(models.Model):
    # instrument name
    name = models.CharField(max_length=255)
    # created this if there are intricate percussion families
    family = models.CharField(max_length=255)
    # Whether the instrument is pitched or not
    pitched = models.BooleanField(default=False)


class InstrumentNote(models.Model):
    # Instrument linked
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    # Note of the instrument
    note = models.CharField(max_length=255)
    # Octave of the note
    octave = models.CharField(max_length=255)
    # Duration of the note
    duration = models.CharField(max_length=255)

class SheetMusic(models.Model):
    # song/sheet music name
    title = models.CharField(max_length=255)
    # difficulty scale (1-5?)
    difficulty = models.IntegerField()

class Note(models.Model):
    # name of note
    name = models.CharField(max_length=2)
    # octave number
    octave = models.IntegerField()  
    # duration time
    duration = models.FloatField()

class SheetMusicNote(models.Model):
    # sheet music played
    sheet_music = models.ForeignKey(SheetMusic, on_delete = models.CASCADE)
    # notes played
    note = models.ForeignKey(Note, on_delete = models.CASCADE)

class UserProgress(models.Model):
    # user name
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # music played
    sheet_music = models.ForeignKey(SheetMusic, on_delete=models.CASCADE)
    # music completed
    completed = models.BooleanField(default=False)
    # scores from practice sessions
    score = models.IntegerField()
    # total amount of time played
    timestamp = models.DateTimeField(auto_now_add=True)

class Feedback (models.Model):
    # user name
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # music just played
    sheet_music = models.ForeignKey(SheetMusic, on_delete=models.CASCADE)
    # algorithmic feedback
    feedback_text = models.TextField()
    # overall rating (1-100?)
    rating = models.IntegerField()
# class Rhythm (models.Model): do we need this? we will have a rhythm api already

class PracticeSession (models.Model):
    # user name
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # time session started
    start_time = models.DateTimeField()
    # time session ended
    end_time = models.DateTimeField()
    # time taken for session
    duration = models.DurationField()


class MIDIFile(models.Model):
    type = models.CharField(max_length=50)  # Either "correct" or "incorrect"
    name = models.CharField(max_length=255)  # Identifier for the MIDI file

    def __str__(self):
        return f"{self.name} ({self.type})"
        
        
class MIDINote(models.Model):
    midi_file = models.ForeignKey(MIDIFile, on_delete=models.CASCADE, related_name='notes')
    node_id = models.CharField(max_length=50)
    note = models.CharField(max_length=10)  # Note including accidentals
    octave = models.CharField(max_length=10)  # Octave of the note
    duration = models.DecimalField(max_digits=10, decimal_places=2)  # Duration of the note
    correct = models.BooleanField(default=True)  # True if played correctly

    def __str__(self):
        return f"{self.note} at {self.timing}s - {'Correct' if self.correct else 'Incorrect'}"

    class Meta:
        indexes = [
            models.Index(fields=['node_id']),
            models.Index(fields=['note']),
            models.Index(fields=['octave']),
            models.Index(fields=['duration']),
        ]


class AudioFile(models.Model):
    type = models.CharField(max_length=50)  # "correct" or "incorrect"
    name = models.CharField(max_length=255)  # Identifier for the audio file

    def __str__(self):
        return f"{self.name} ({self.type})"



class AudioNote(models.Model):
    audio_file = models.ForeignKey(AudioFile, on_delete=models.CASCADE, related_name='notes')
    node_id = models.CharField(max_length=50)
    note = models.CharField(max_length=10)  # Note including accidentals
    octave = models.CharField(max_length=10)  # Octave of the note
    duration = models.DecimalField(max_digits=10, decimal_places=2)  # Duration of the note
    correct = models.BooleanField(default=True)  # True if played correctly

    def __str__(self):
        return f"{self.note} at {self.timing}s - {'Correct' if self.correct else 'Incorrect'}"

    class Meta:
        indexes = [
            models.Index(fields=['node_id']),
            models.Index(fields=['note']),
            models.Index(fields=['octave']),
            models.Index(fields=['duration']),
        ]

