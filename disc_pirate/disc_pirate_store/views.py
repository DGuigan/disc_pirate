from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')


def register(request):
    return HttpResponse(request, "Hello from reg")


def all_albums(request):
    all_a = Album.objects.all()
    return render(request, 'all_albums.html', {'albums': all_a})


def single_album(request, albumid):
    album = Album.objects.get(id=albumid)
    return render(request, 'single_album.html', {'album': album})
