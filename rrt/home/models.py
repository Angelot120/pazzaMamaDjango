from django.db import models

from rrt.settings import AUTH_USER_MODEL


# from rrt.rrt.settings import AUTH_USER_MODEL


# Create your models here.

class Dish(models.Model):

    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='flats', blank=True, null=True)
    isAvailable = models.BooleanField(default=True)


    def __str__(self):
        return self.name


# Order = Article

class Order(models.Model):
    client = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.CASCADE) # Supprimer toutes les données liés à l'utilisateur
    flat = models.ForeignKey(Dish, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False) # Article commendé par défaut
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.flat} - ({self.quantity})"


class Card(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE) # Or user = models.ForeignKey(unique=True)
    orders = models.ManyToManyField(Order)


    def __str__(self):
        return f"{self.user.username}"