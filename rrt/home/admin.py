from django.contrib import admin

from .models import Dish, Order, Card

# Register your models here.

admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(Card)