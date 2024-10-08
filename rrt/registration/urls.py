

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.client_login, name='client_login'),  # URL et nom pour la vue de connexion
    path('signup/', views.client_signup, name='client_signup'),  # URL et nom pour la vue d'inscription
    path('logout/', views.client_logout, name='client_logout'),  # URL et nom pour la vue de déconnexion
]
