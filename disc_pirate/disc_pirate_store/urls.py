from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('all_albums/', views.all_albums, name="all_albums"),
    path('single_album/<int:album_id>', views.single_album, name="single_album"),
    path('album_form/', views.album_form, name="album_form"),
    path('causer_signup/', views.CaUserSignupView.as_view(), name="register"),
]
