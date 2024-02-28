from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    passWord = models.CharField(max_length=255)
    emailAddress = models.CharField(max_length=255)

class Instrument(models.Model):
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)

class Sheet_Music(models.Model):
    title = models.CharField(max_length=255)
    difficulty = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class User_Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sheet_music = models.ForeignKey(Sheet_Music, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Feedback (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sheet_music = models.ForeignKey(Sheet_Music, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

# class Rhythm (models.Model): do we need this? we will have a rhythm api already

class Practice_Session (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField()