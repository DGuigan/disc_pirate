from . import views
from .views import *
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)  # when we go to /api/users, load the users json
router.register(r'albums', AlbumViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('all_albums/', views.all_albums, name="all albums"),
    path('single_album/<int:album_id>', views.single_album, name="single album"),
    path('album_form/', views.album_form, name="album form"),
    path('causer_signup/', views.CaUserSignupView.as_view(), name="register"),
    path('admin_signup/', views.AdminSignupView.as_view(), name="register admin"),
    path('login/', views.Login.as_view(template_name="login.html", authentication_form=UserLoginForm), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('add_to_basket/<int:album_id>', views.add_to_basket, name="add_to_basket"),
    path('remove_from_basket/<int:album_id>', views.remove_from_basket, name="remove_from_basket"),
    path('view_basket', views.view_basket, name="your_basket"),
    path('order_form/', views.order_form, name="order_form"),
    path('admin_page/', views.admin_page, name="admin_page"),
    path('user_page/', views.user_page, name="admin_page"),
    path('view_orders/', views.view_orders, name="view_orders"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),  # localhost api will be entrypoint to our REST api
    path('token/', obtain_auth_token, name="api_token_auth"),
]
