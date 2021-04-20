from .models import Album, CaUser, Order, ShoppingBasket
from django import forms
from django.forms import ModelForm
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'albumName': forms.TextInput(attrs={'class': 'form-control'}),
            'albumArt': forms.FileInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'releaseDate': forms.DateInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'contactNumber']

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contactNumber': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CASignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CaUser

    @transaction.atomic
    def save(self):
        #  create object in memory, but don't add to db yet
        user = super().save(commit=False)
        user.is_admin = False
        user.save()
        ShoppingBasket(user=user).save()
        Token.objects.create(user=user)
        return user


class AdminSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CaUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        ShoppingBasket(user=user).save()
        Token.objects.create(user=user)
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': '',
                                                                 }))
