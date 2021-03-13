from django.db import models
from django.contrib.auth.models import AbstractUser


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    albumName = models.CharField(max_length=70)
    albumArt = models.FileField(upload_to='album_art', blank=True)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    releaseDate = models.DateField()
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class CaUser(AbstractUser):
    is_admin = models.BooleanField(default=False)


#  Orders
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    address = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)


class OrderItem(models.Model):
    orderId = models.AutoField(primary_key=True)
    productId = models.IntegerField()
    product = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def price(self):
        return self.product.price * self.quantity


#  Shopping Basket
class ShoppingBasket(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.OneToOneField(CaUser, on_delete=models.CASCADE)


class ShoppingBasketItems(models.Model):
    id = models.AutoField(primary_key=True)
    basket_id = models.ForeignKey(ShoppingBasket, on_delete=models.CASCADE)
    product = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
