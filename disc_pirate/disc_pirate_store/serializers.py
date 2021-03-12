from django.urls import path, include
from .models import CaUser, Album # Import your model
from rest_framework import serializers, viewsets
from .serializers import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=CaUser
        fields = '__all__'


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Album
        fields = '__all__'