from rest_framework import serializers
from .models import *

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'firstName', 'lastName', 'userName', 'emailAddress')

class instrumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instrument
        fields = ('name', 'family')
