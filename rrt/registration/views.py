from django.contrib.auth import get_user_model, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Clients


def client_signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Vérifier si l'utilisateur existe déjà
        if Clients.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà utilisé.")
            return render(request, 'signup/index.html')
        else:
            # Créer un nouvel utilisateur s'il n'existe pas encore
            user = Clients.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, "Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter.")
            return redirect('home')

    else:
        return render(request, 'signup/index.html')


def client_login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirection vers la page d'accueil après connexion
        else:
            # Gérer l'échec d'authentification ici
            error_message = "Nom d'utilisateur ou mot de passe incorrect. Veuillez réessayer."
            return render(request, 'login/index.html', {'error_message': error_message})
    return render(request, 'login/index.html')


def client_logout(request):
    logout(request)
    return redirect('home')



'''def client_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rediriger vers la page d'accueil ou une autre page après l'authentification réussie
            return redirect('index')
        else:
            # Si l'authentification échoue, vous pouvez afficher un message d'erreur
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            # Ou renvoyer simplement la page de connexion avec un message d'erreur
            return render(request, 'login/index.html')
    else:
        return render(request, 'login/index.html')
        
        
        
user = get_user_model()
 
def client_signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # email = request.POST.get("email")
        user.objects.create_user(username=username,
                                   password=password)
                                   # email=email)
        login(request, user)
        return redirect('index')
    return render(request, 'signup/index.html') 
    
    
    
    def client_login(request):
        return render(request, 'login/index.html')
'''

