from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')


def register(request):
    return HttpResponse('Hello from the registration page')