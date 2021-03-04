from django.forms import ModelForm
from .models import Album
from .models import CaUser
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['albumName', 'artist', 'genre','releaseDate', 'description', 'price']



# class CASignupForm(UserCreationForm):
#         model = CaUser
#
#     @transaction.atomic
#     def save(self):
#         #  create object in memory, but don't add to db
#         user = super().save(commit=False)
#
#         user.is_admin = False
#         user.save()
#         return user
