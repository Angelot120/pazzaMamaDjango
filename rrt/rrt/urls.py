"""
URL configuration for rrt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home.views import cart, delete_cart, buy
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('cart/', cart, name='cart'),
    path('cart/delete-cart', delete_cart, name='delete-cart'),
    path('accounts/', include('registration.urls'), name='registration'),
    path('app/', include('home.urls')),
    path('buy/', buy, name="buy"),
    path('api/', include('home.urls'), name="getApi"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)