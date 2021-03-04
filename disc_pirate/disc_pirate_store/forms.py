from django.forms import ModelForm
from .models import Album, CaUser
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['albumName', 'artist', 'genre', 'releaseDate', 'description', 'price']


class CASignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CaUser

    @transaction.atomic
    def save(self):
        #  create object in memory, but don't add to db yet
        user = super().save(commit=False)
        user.is_admin = False
        user.save()
        return user
