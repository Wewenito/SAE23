from .models import GroupeEtu, Enseignant, Cours, Etudiants, Absences
from .forms import GroupeEtuForm, CoursForm, EtudiantsForm, EnseignantForm, AbsenceForm
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.urls import reverse
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def signin(request):
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


def home(request): 
    return render(request, 'MAIN/mp.html')



def Afficher_groupes(request):
    groupes = GroupeEtu.objects.all()
    return render(request, 'MAIN/groupes/Afficher_Groupe.html', {'groupes': groupes})


def ajout_groupe(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = GroupeEtuForm(request.POST)

            if form.is_valid():
                form.save()
                return Afficher_groupes(request)
        else:
            form = GroupeEtuForm()
        return render(request, 'MAIN/groupes/Ajout_groupe.html', {'form': form})
    else:
        msg = 'Vous ne pouvez pas ajouter de groupe sans être connecté..'
        form = AuthenticationForm(request.POST)
        return render(request, 'registration/login.html', {'form': form, 'msg': msg})



def Afficher_enseignants(request):
    enseignant = Enseignant.objects.all()
    return render(request, 'MAIN/enseignants/Afficher_enseignants.html', {'enseignant':enseignant})

def Ajouter_enseignants(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EnseignantForm(request.POST)
            if form.is_valid():
                enseignant = form.save(commit=False)
                enseignant.save()

                user = User.objects.create_user(username=enseignant.mail, password='toto')
                enseignant.user = user
                enseignant.save()

                enseignant_groupe = Group.objects.get(name='ENSEIGNANTS')
                user.groups.add(enseignant_groupe)

                return Afficher_enseignants(request)  # Redirect to a success page or another URL
        else:
            form = EnseignantForm()
            return render(request, 'MAIN/enseignants/Ajouter_enseignants.html', {'form':form})
    else:
        msg = 'Vous ne pouvez pas ajouter d\'enseignants sans être connecté..'
        form = AuthenticationForm(request.POST)
        return render(request, 'registration/login.html', {'form': form, 'msg': msg})

    return render(request, 'MAIN/enseignants/Ajouter_enseignants.html')


def Afficher_cours(request):
    cours = Cours.objects.all()
    return render(request, 'MAIN/cours/Afficher_Cours.html', {'cours':cours})

def Ajouter_cour(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CoursForm(request.POST)
            if form.is_valid():
                form.save()  # Save the form data to the database
                return Afficher_cours(request)  # Redirect to a success page or another URL
        else:
            groupe = GroupeEtu.objects.all()
            enseignant = Enseignant.objects.all()
            form = CoursForm()
            return render(request, 'MAIN/cours/Ajouter_cours.html', {'form':form, 'groupe':groupe, 'enseignant':enseignant})
    else:
        msg = 'Vous ne pouvez pas ajouter de cours sans être connecté..'
        form = AuthenticationForm(request.POST)
        return render(request, 'registration/login.html', {'form': form, 'msg': msg})

def Ajouter_etudiants(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EtudiantsForm(request.POST)
            if form.is_valid():
                etudiant = form.save(commit=False)  # Save the form data to an instance
                etudiant.save()  # Save the instance to the database
                # Create a new user and assign it to the Etudiant
                user = User.objects.create_user(username=etudiant.mail, password='toto')
                etudiant.user = user
                etudiant.save()
                # Add the user to the ETUDIANTS group
                etudiants_group = Group.objects.get(name='ETUDIANTS')
                user.groups.add(etudiants_group)
                return Afficher_etudiants(request)  # Redirect to a success page or another URL
        else:
            groupe = GroupeEtu.objects.all()
            form = EtudiantsForm()
            return render(request, 'MAIN/etudiants/Ajouter_etudiants.html', {'form':form, 'groupe': groupe})
    else:
        msg = 'Vous ne pouvez pas ajouter d\'étudiants sans être connecté..'
        form = AuthenticationForm(request.POST)
        return render(request, 'registration/login.html', {'form': form, 'msg': msg})

    return render(request, 'MAIN/etudiants/Ajouter_etudiants.html')

def Afficher_etudiants(request):
    etudiant = Etudiants.objects.all()
    return render(request, 'MAIN/etudiants/Afficher_etudiants.html', {'etudiant': etudiant})



def afficher_modif_form(request, id):
    print(id)
    print(request)
    print("/////////////////////////////////////////////////////")
    try:
        print("showing the form")
        etudiant = Etudiants.objects.get(id=id)
        form = EtudiantsForm(instance=etudiant)
        modifier_etudiant_url = reverse('ABSENCES:modifier_etudiant', args=[id])
        return render(request, 'MAIN/etudiants/modifier_etudiant.html', {'form': form, 'modifier_etudiant_url': modifier_etudiant_url})
    except ObjectDoesNotExist:
        print("FATAL ERROR OBJECT !!")
        return HttpResponse("Item not found", status=404)
    except Exception as e:
        print("FATAL ERROR EXCEPTION !!")
        print(e)
        return HttpResponse("An error occurred", status=500)



def modifier_etudiant(request, id):
    print("METHODE")
    print(request.method)
    etudiant = get_object_or_404(Etudiants, id=id)
    form = EtudiantsForm(instance=etudiant)

    if request.method == 'POST':
        form = EtudiantsForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return Afficher_etudiants(request)
    else:
        print(form)
    
    return render(request, 'MAIN/etudiants/modifier_etudiant.html', {'form': form})


def afficher_modif_form_ens(request, id):
    enseignant = Enseignant.objects.get(id=id)
    form = EnseignantForm(instance=enseignant)
    modifier_enseignant_url = reverse('ABSENCES:modifier_enseignant', args=[id])
    return render(request, 'MAIN/enseignants/modifier_enseignant.html', {'form':form, 'modifier_enseignant_url':modifier_enseignant_url})

def modifier_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    form = EnseignantForm(instance=enseignant)

    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return Afficher_enseignants(request)
    
    return render(request, 'MAIN/enseignants/modifier_enseignant.html', {'form':form})

def afficher_modif_form_cour(request,id):
    cour = Cours.objects.get(id=id)
    form = CoursForm(instance=cour)
    modifier_cour_url = reverse('ABSENCES:modifier_cour', args=[id])
    return render(request, 'MAIN/cours/modifier_cour.html', {'form':form, 'modifier_cour_url':modifier_cour_url})

def modifier_cour(request, id):
    cour = get_object_or_404(Cours, id=id)
    form = CoursForm(instance=cour)

    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cour)
        if form.is_valid():
            form.save()
            return Afficher_cours(request)
    return render(request, 'MAIN/cours/modifier_cour.html', {'form':form})

def supprimer_etudiant(request, id):
    etudiant = Etudiants.objects.get(id=id)

    if request.method == 'POST':
        etudiant.delete()
        return Afficher_etudiants(request)
    else:
        return Afficher_etudiants(request)

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


    
#def profile_ens(request, id):
 #   enseignant = Enseignant.objects.get(id=id)

#    return render(request, 'MAIN/enseignants/Affiche-modif-profil-ens.html', {'enseignant':enseignant})



def Gestion_enseignants(request, arg1):
    if arg1 == 'ACCEUIL':
        return render(request, 'MAIN/enseignants/acceuil-ens.html')
    elif arg1 == 'GESTION':
        return render(request, 'MAIN/enseignants/gestion_ens.html')
    elif arg1 == 'PROFIL':
        enseignant = Enseignant.objects.get(id=id)
        return render(request, 'MAIN/enseignants/Affiche-modif-profil-ens.html')
    
def Supprimer_enseignant(request, id):
    enseignant = Enseignant.objects.get(id=id)

    if request.method == 'POST':
        enseignant.delete()
        return Afficher_enseignants(request)
    else:
        return Afficher_enseignants(request)



def modification_groupe(request, id):
    groupe = GroupeEtu.objects.get(id=id)

    if request.method == 'POST':
        form = GroupeEtuForm(request.POST, instance=groupe)
        if form.is_valid():
            form.save()
            return Afficher_groupes(request)
    else:
        form = GroupeEtuForm(instance=groupe)

    return render(request, 'MAIN/groupes/Modifier_groupe.html', {'form': form})

def Supprimer_cour(request, id):
    cour = Cours.objects.get(id=id)

    if request.method == 'POST':
        cour.delete()
        return Afficher_cours(request)
    else:
        return Afficher_cours(request)


def suppression_groupe(request, id):
    groupe = GroupeEtu.objects.get(id=id)

    if request.method == 'POST':
        groupe.delete()
        return Afficher_groupes(request)
    else:
        return Afficher_groupes(request)



def gestion_etudiants(request, arg1):
    if arg1 == 'PROFIL':
        return render(request, 'MAIN/etudiants/acceuil-etu.html')
    elif arg1 == 'GESTION':
        return render(request, 'MAIN/etudiants/gestion_etu.html')
    
def acceuil_etu(request, id):
    etudiant = get_object_or_404(Etudiants, id=id)
    
    return render(request, 'MAIN/etudiants/acceuil-etu.html', {'etudiant':etudiant})

    
def Ajouter_absence(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AbsenceForm(request.POST)
            if form.is_valid():
                absence = form.save(commit=False)
                absence.Justifie_bool = False
                absence.Checke_par = None
                absence.Commentaire_enseignant = ''
                absence.Inspection_terminee = False
                absence.save()
                return acceuil_etu(request, request.user.id)
            else:
                print("________________________DEPART FORM______________________________")
                print(form)
                print("________________________FIN FORM______________________________")
        else:
            form = AbsenceForm(initial={'Etudiant': request.user.id})
            form.fields['Checke_par'].required = False  # Set Checke_par field as not required
            return render(request, 'MAIN/absences/Ajouter_absence.html', {'form': form})
    else:
        msg = 'Vous ne pouvez pas ajouter d\'étudiants sans être connecté..'
        form = AuthenticationForm(request.POST)
        return render(request, 'registration/login.html', {'form': form, 'msg': msg})

    return render(request, 'MAIN/absences/Ajouter_absence.html')