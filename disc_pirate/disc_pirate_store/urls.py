from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.register, name="register"),
    path('all_albums/', views.all_albums, name="all albums"),
]