from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import serializers
from . import models

# Create your views here.

class userViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.userSerializer

class instrumentViewSet(viewsets.ModelViewSet):
    queryset = models.Instrument.objects.all()
    serializer_class = serializers.instrumentSerializer
