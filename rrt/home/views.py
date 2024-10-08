from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Dish, Card, Order


# from rrt.home.models import Flat


# Create your views here.

def index(request):
    # return HttpResponse("Hollo world !")
    dishes = Dish.objects.all()
    return render(request, 'home/index.html', context={'dishes': dishes})


def dish_details(request, slug):
    dish_info = get_object_or_404(Dish, slug=slug)
    print(f" Voici votre slug ici {slug}")
    return render(request, 'home/details.html', {'dish_info': dish_info})


def add_to_card(request, slug):
    # print(f" Voici votre nouveau slug ici {slug}")
    client = request.user
    dishes = get_object_or_404(Dish, slug=slug)
    cart, _ = Card.objects.get_or_create(user=client)
    order, created = Order.objects.get_or_create(client=client, flat=dishes)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse('dish_details', kwargs={'slug': slug}))


def cart(request):

    cart = get_object_or_404(Card, user=request.user)

    return render(request, 'home/cart.html', context={'orders': cart.orders.all()})

def delete_cart(request):
    if cart := request.user.card:
        cart.orders.all().delete()
        cart.delete()
    return redirect('home')

def buy(request):

    return render(request, 'home/buy.html')

def getApi(request):

    dishes = Dish.objects.all()
    dish_json = serializers.serialize('json', dishes)
    return HttpResponse(dish_json)

'''def delete_cart(request):
    
    Une possibilitée
    cart = request.user.cart
    if cart:
        cart.orders.all().delete()
        cart.delete()

 if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()
    return redirect('home')

from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .models import Flat, Card, Order

def add_to_card(request, slug):
    client = request.user
    flat = get_object_or_404(Flat, slug=slug)
    cart, _ = Card.objects.get_or_create(user=client)
    order, created = Order.objects.get_or_create(user=client, flat=flat, cart=cart)

    if not created:
        order.quantity += 1
        order.save()

    return redirect(reverse('flat_details', kwargs={'slug': slug}))

'''