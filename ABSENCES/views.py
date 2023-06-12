from .models import GroupeEtu, Enseignant, Cours
from .forms import GroupeEtuForm, CoursForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse


# Create your views here.

def add_groupe(request):
    if request.method == 'POST':
        form = GroupeEtuForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'MAIN/mp.html', {'form': form})
    else:
        form = GroupeEtuForm()
    
    return render(request, 'registration/login.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return home(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return home(request)
        else:
            msg = 'Erreur de connection'
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
    
    
def profile_ens(request, id):
    enseignant = Enseignant.objects.get(id=id)

    return render(request, 'MAIN/profil.html', {'enseignant':enseignant})

def update_mail_ens(request, id):
    enseignant = Enseignant.objects.get(id=id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            new_email = request.POST.get('new_email')
            enseignant.mail = new_email
            enseignant.save()
        else:
            msg = 'Vous ne pouvez pas effectuer cette action sans être connecté !'
            form = AuthenticationForm(request.POST)
            return render(request, 'registration/login.html', {'form': form, 'msg': msg})

    return render(request, 'MAIN/profil.html', {'enseignant':enseignant})


def home(request): 
    return render(request, 'MAIN/mp.html')



def Afficher_groupes(request):
    groupes = GroupeEtu.objects.all()
    return render(request, 'MAIN/groupes/Afficher_groupes.html', {'groupes': groupes})


def ajout_groupe(request):


    return home(request)

def ajout_cour(request):
    if request.user.is_authenticated:
        form = CoursForm()  # Create an instance of the form
        if request.method == 'POST':
            form = CoursForm(request.POST)  # Bind form data from the request
            if form.is_valid():
                form.save()  # Save the form data to the database
                # Redirect or perform other actions upon successful form submission
            return render(request, 'MAIN/cours/Ajouter_cours.html', {'form': form})
    else:
        msg = 'Vous ne pouvez pas effectuer cette action sans être connecté !'
        form = AuthenticationForm(request.POST)
        return render(request, 'registration/login.html', {'form': form, 'msg': msg})

    