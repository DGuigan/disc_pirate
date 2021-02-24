from django.db import models
from django.contrib.auth.models import AbstractUser


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    albumName = models.CharField(max_length=70)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    releaseDate = models.DateField()
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)


#  Orders
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customerId = models.IntegerField()
    address = models.CharField(max_length=200)
    date = models.DateField()
    courier = models.CharField(max_length=50)


class OrderItem(models.Model):
    orderId = models.IntegerField()
    productId = models.IntegerField()


#  Shopping Basket
class ShoppingBasket(models.Model):
    id = models.AutoField(primary_key=True)
    customerId = models.IntegerField()


class ShoppingBasketItems(models.Model):
    customerId = models.IntegerField()
    productId = models.IntegerField()


class CaUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
