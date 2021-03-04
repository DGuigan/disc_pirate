from django.contrib import admin
from .models import *

admin.site.register(Album)

admin.site.register(ShoppingBasket)
admin.site.register(ShoppingBasketItems)

admin.site.register(Order)
admin.site.register(OrderItem)
