from .models import CaUser, Album  # Import your model
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaUser
        fields = '__all__'


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        # not using '__all__' because it doesn't serialize id, there is probably a better way to do this
        fields = ['id', 'albumArt', 'albumName', 'artist', 'description', 'genre', 'price', 'releaseDate']
