from rest_framework import serializers
from .models import *

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'userName', 'passWord', 'emailAddress')

class instrumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instrument
        fields = ('name', 'family')


