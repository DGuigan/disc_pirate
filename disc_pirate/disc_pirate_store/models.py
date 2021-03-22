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
    user = models.OneToOneField(CaUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=200)
    cardNumber = models.IntegerField()

    def cost(self):
        total = 0.0
        for item in OrderItem.objects.filter(order=self):
            total += item.cost()
        return total


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def cost(self):
        return self.album.price * self.quantity


#  Shopping Basket
class ShoppingBasket(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CaUser, on_delete=models.CASCADE)

    def cost(self):
        total = 0.0
        for item in ShoppingBasketItems.objects.filter(basket=self):
            total += item.cost()
        return total


class ShoppingBasketItems(models.Model):
    id = models.AutoField(primary_key=True)
    basket = models.ForeignKey(ShoppingBasket, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def cost(self):
        return self.album.price * self.quantity
