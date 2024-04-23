from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from subprocess import check_output
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from . import serializers
from . import models

from percussatsight.librosa_script import format_notes, filter_notes, extract_notes
# Create your views here.

class userViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.userSerializer

class instrumentViewSet(viewsets.ModelViewSet):
    queryset = models.Instrument.objects.all()
    serializer_class = serializers.instrumentSerializer

#class feedbackAPIView(APIView):
#    def get(self, request, format=None):
#        output = check_output(["python", "../librosa_script.py"])
#
#        serialized_output = {"result": output.decode("utf-8")}
#
#       return Response(serialized_output)

def feedback_api(request):
    correct_audio_file = "/usr/src/app/percussatsight/music_sample.wav"
    incorrect_audio_file = "/usr/src/app/percussatsight/Incorrectly_Played_Sample.wav"

    correct_notes = extract_notes(correct_audio_file)
    incorrect_notes = extract_notes(incorrect_audio_file)

    correct_notes_filtered = filter_notes(correct_notes)
    incorrect_notes_filtered = filter_notes(incorrect_notes)

    correct_notes_str = format_notes(correct_notes_filtered)
    incorrect_notes_str = format_notes(incorrect_notes_filtered)

    data = {
        "correct_notes": correct_notes_str,
        "incorrect_notes": incorrect_notes_str,
    }

    return JsonResponse(data)