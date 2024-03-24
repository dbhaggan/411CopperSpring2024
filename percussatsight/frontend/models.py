from django.db import models

# Create your models here.
class User(models.Model):
    # sign up info
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    passWord = models.CharField(max_length=255)
    emailAddress = models.CharField(max_length=255)

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
    name = models.CharField(max_length = 2)
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
