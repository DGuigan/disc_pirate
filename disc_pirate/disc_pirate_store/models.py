from django.db import models


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    format = models.CharField(max_length=50)  # cd, vinyl, digital, etc...
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Merch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # shirt, hoodie, stickers, pins, etc..
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class ShoppingBasket(models.Model):
    id = models.AutoField(primary_key=True)
    customerId = models.IntegerField()


class ShoppingBasketItem(models.Model):
    basketId = models.IntegerField()
    productId = models.IntegerField()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customerId = models.IntegerField()
    shippingAddr = models.CharField(max_length=200)
    date = models.DateField()


class OrderItem(models.Model):
    orderId = models.IntegerField()
    productId = models.IntegerField()
