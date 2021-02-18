from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.register, name="register"),
    path('all_albums/', views.all_albums, name="all_albums"),
    path('single_album/<int:albumid>', views.single_album, name="single_album"),
    path('album_form/', views.album_form, name="album_form"),
]