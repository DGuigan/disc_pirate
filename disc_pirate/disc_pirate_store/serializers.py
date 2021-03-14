from .models import CaUser, Album  # Import your model
from django.urls import path, include
from rest_framework import serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaUser
        fields = '__all__'


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
