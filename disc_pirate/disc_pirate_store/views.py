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
from random import choice


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


@login_required
def add_to_basket(request, album_id):
    user = request.user
    shopping_basket = ShoppingBasket.objects.get(user=user)

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

    return redirect("/view_basket")


@login_required
def remove_from_basket(request, album_id):
    user = request.user
    shopping_basket = ShoppingBasket.objects.get(user=user)

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


@login_required
def view_basket(request):
    shopping_basket = ShoppingBasket.objects.get(user=request.user)

    basket_items = ShoppingBasketItems.objects.filter(basket=shopping_basket)
    if len(basket_items) == 0:
        basket_items = None

    return render(request, 'view_basket.html', {'basket': shopping_basket, 'basket_items': basket_items})


@login_required
def order_form(request):
    user = request.user
    shopping_basket = ShoppingBasket.objects.filter(user=user).first()

    if shopping_basket is None:
        shopping_basket = ShoppingBasket(user=user).save()

    basket_items = ShoppingBasketItems.objects.filter(basket=shopping_basket)

    if len(basket_items) == 0:
        return redirect('/')

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
