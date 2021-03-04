from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView


def index(request):
    return render(request, 'index.html')


def register(request):
    return HttpResponse('Hello from the registration page')


def all_albums(request):
    albums = Album.objects.all()
    return render(request, 'all_albums.html', {'albums': albums})


def single_album(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'single_album.html', {'album': album})


def album_form(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            new_album = form.save()
            return render(request, 'single_album.html', {'album': new_album})
    elif request.method == 'GET':
        form = AlbumForm()
        return render(request, 'album_form.html', {'form': form})


class CaUserSignupView(CreateView):
    model = CaUser
    form_class = CASignupForm
    template_name = 'causer_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class AdminSignupView(CreateView):
    model = CaUser
    form_class = AdminSignupForm
    template_name = 'admin_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class Login(LoginView):
    template_name = 'login.html'


def logout_view(request):
    logout(request)
    return redirect('/')
