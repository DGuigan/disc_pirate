from .models import *
from .forms import *
from .decorators import admin_required
from .serializers import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from random import choice
import json


def index(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'random_album': choice(albums)})


def register(request):
    return HttpResponse('Hello from the registration page')


def all_albums(request):
    f = request.GET.get("format", "")

    if f == "json":
        albums_serialized = serializers.serialize("json", Album.objects.all())
        return HttpResponse(albums_serialized, content_type="application/json")
    else:
        albums = Album.objects.all()
        return render(request, 'all_albums.html', {'albums': albums})


def single_album(request, album_id):

    # if album does not exist redirect to all_albums view
    try:
        album = Album.objects.get(pk=album_id)
    except ObjectDoesNotExist:
        return redirect("/all_albums")

    return render(request, 'single_album.html', {'album': album})


@login_required
@admin_required
def album_form(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
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


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_to_basket(request, album_id):
    user = request.user
    if user.is_anonymous :
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]
        user = Token.objects.get(key=token).user
    shopping_basket = ShoppingBasket.objects.get(user=user)

    # if album does not exist redirect to view_basket page without modifying basket
    try:
        album = Album.objects.get(pk=album_id)
    except ObjectDoesNotExist:
        return redirect("/view_basket")

    sbi = ShoppingBasketItems.objects.filter(basket=shopping_basket, album=album).first()
    if sbi is None:
        sbi = ShoppingBasketItems(basket=shopping_basket, album=album)
        sbi.save()
    else:
        sbi.quantity += 1
        sbi.save()

    flag = request.GET.get('format', '')
    if flag == "json":
        status_serialized = json.dumps({"status": "success"})
        return HttpResponse(status_serialized, content_type="application/json")
    else:
        return redirect("/view_basket")


@login_required
def remove_from_basket(request, album_id):
    user = request.user
    shopping_basket = ShoppingBasket.objects.get(user=user)

    # if album does not exist redirect to view_basket page without modifying basket
    try:
        album = Album.objects.get(pk=album_id)
    except ObjectDoesNotExist:
        return redirect("/view_basket")

    sbi = ShoppingBasketItems.objects.filter(basket=shopping_basket, album=album).first()

    if sbi is None:
        return redirect("/view_basket")
    elif sbi.quantity > 1:
        sbi.quantity -= 1
        sbi.save()
    elif sbi.quantity == 1:
        sbi.delete()

    return redirect("/view_basket")


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def view_basket(request):
    user = request.user

    if user.is_anonymous:
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]
        user = Token.objects.get(key=token).user

    shopping_basket = ShoppingBasket.objects.get(user=user)

    basket_items = ShoppingBasketItems.objects.filter(basket=shopping_basket)
    if len(basket_items) == 0:
        basket_items = None

    flag = request.GET.get("format", "")
    # if json request serialize basket info and send back, probably a better way to do this
    if flag == "json":
        if basket_items:
            basket_items_serialized = json.dumps([{"albumName": item.album.albumName,
                                                   "artist": item.album.artist,
                                                   "quantity": item.quantity} for item in basket_items])
        else:
            basket_items_serialized = json.dumps([])
        return HttpResponse(basket_items_serialized, content_type="application/json")
    else:
        return render(request, 'view_basket.html', {'basket': shopping_basket, 'basket_items': basket_items})


@login_required
def order_form(request):
    user = request.user
    shopping_basket = ShoppingBasket.objects.get(user=user)

    basket_items = ShoppingBasketItems.objects.filter(basket=shopping_basket)

    # if basket is empty redirect to view_basket page
    if len(basket_items) == 0:
        return redirect('/view_basket')

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = user
            order.save()

            for basket_item in basket_items:
                order_item = OrderItem.objects.create(order=order,
                                                      album=basket_item.album,
                                                      quantity=basket_item.quantity)
                order_item.save()
                basket_item.delete()

            return redirect('/')
    elif request.method == 'GET':
        form = OrderForm()
        return render(request, 'order_form.html', {'form': form})


@login_required
@admin_required
def admin_page(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            new_album = form.save()
            return render(request, 'single_album.html', {'album': new_album})
    elif request.method == 'GET':
        form = AlbumForm()
        orders = Order.objects.all()
        return render(request, 'admin_page.html', {'orders': orders, 'form': form})


@login_required
def user_page(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user_page.html', {'orders': orders})


class UserViewSet(viewsets.ModelViewSet):
    queryset = CaUser.objects.all()
    serializer_class = UserSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = []
    permission_classes = []
