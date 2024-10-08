
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dish/<str:slug>/', views.dish_details, name='dish_details'),
    path('dish/<str:slug>/add-to-card/', views.add_to_card, name='add_to_card'),
    path('get_dish/', views.getApi, name='getApi'),
    # path('', views.cart, name='cart'),
]