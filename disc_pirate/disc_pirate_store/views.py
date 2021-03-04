from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import login


# class CaUserSignupView(CreateView):
#     model = CaUser
#     form_class = CASignupForm
#     template_name = 'causer_signup.html'
#
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/')


def index(request):
    return render(request, 'index.html')


def register(request):
    return HttpResponse('Hello from the registration page')

