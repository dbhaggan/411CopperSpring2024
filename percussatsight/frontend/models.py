from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    passWord = models.CharField(max_length=255)
    emailAddress = models.CharField(max_length=255)

class User_Progress(models.Model):

class Sheet_Music(models.Model):

class Feedback (models.Model):

class Rhythm (models.Model):

class Practice_SEssion (models.Model):