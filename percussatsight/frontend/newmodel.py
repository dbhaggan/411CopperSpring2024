# newmodels.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    app_settings = models.ForeignKey('AppSettings', on_delete=models.CASCADE)
    instrument = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    password_hashed = models.CharField(max_length=255)

class UserType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_student = models.CharField(max_length=255)
    type_teacher = models.CharField(max_length=255)
    type_individual = models.CharField(max_length=255)

class SchoolProfile(models.Model):
    school_id = models.AutoField(primary_key=True)
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    enrollment_type = models.CharField(max_length=255)
    course_id = models.IntegerField()
    num_teachers = models.IntegerField()
    num_students = models.IntegerField()

class SchoolUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE)
    enrollment_type = models.BooleanField()
    course_id = models.IntegerField()

class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE)

class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=255)
    subscription_duration = models.CharField(max_length=255)
    subscription_cost = models.FloatField()

class SchoolInformation(models.Model):
    school = models.ForeignKey('SchoolProfile', on_delete=models.CASCADE)
    courses = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number_students = models.IntegerField()
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE)

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    card_num = models.CharField(max_length=255)
    card_holder = models.CharField(max_length=255)

class AppSettings(models.Model):
    app_settings_id = models.AutoField(primary_key=True)
    instrument = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sheet = models.ForeignKey('Sheet', on_delete=models.CASCADE)
    difficulty = models.FloatField()
    mode_10 = models.IntegerField()
    metronome = models.BooleanField()
    microphone = models.BooleanField()
    midi = models.BooleanField()

class Sheets(models.Model):
    sheet_id = models.AutoField(primary_key=True)
    instrument = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    creation_date = models.CharField(max_length=255)
    difficulty = models.FloatField()
    tempo = models.FloatField()

class Performances(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    sheet = models.ForeignKey('Sheet', on_delete=models.CASCADE)
    score = models.FloatField()
    midi_data = models.TextField()
    audio_data = models.TextField()

class Instruments(models.Model):
    instrument_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    pitched = models.BooleanField()
    keys = models.TextField()

class Engagements(models.Model):
    engagement_id = models.AutoField(primary_key=True)
    login_count = models.IntegerField()
    system_status = models.BooleanField()
    practice_plan = models.TextField()

class Feedbacks(models.Model):
    report_id = models.AutoField(primary_key=True)
    assignment = models.ForeignKey('Performance', on_delete=models.CASCADE)
    comments = models.TextField()
    all_feedback = models.TextField()
    practice_plan = models.TextField()