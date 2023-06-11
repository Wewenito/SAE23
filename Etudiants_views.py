from django.shortcuts import render, HttpResponseRedirect
from .forms import EtudiantsForm
from . import models

# Create your views here.
def Etudiants_index(request):
    liste = list(models.Etudiants.objects.all())
    return render(request,"Etudiants/index.html",{"liste" : liste})

def Etudiants_ajout(request):
    if request.method == "POST":
        form = EtudiantsForm(request)
        if form.is_valid():
            Etudiants = form.save()
            return render(request, "Etudiants/affiche.html", {"Etudiants": Etudiants})

        else:
            return render(request, "Etudiants/ajout.html", {"form": form})
    else:
        form = EtudiantsForm()
        return render(request, "Etudiants/ajout.html", {"form": form})


def Etudiants_traitement(request):
    lform = EtudiantsForm(request.POST)
    if lform.is_valid():
        Etudiants = lform.save()
        return HttpResponseRedirect("/Etudiants")
    else:
        return render(request, "Etudiants/ajout.html", {"form": lform})


def Etudiants_affiche(request, id):
    Etudiants = models.Etudiants.objects.get(pk=id)
    return render(request, "Etudiants/affiche.html", {"Etudiants": Etudiants})


def Etudiants_update(request, id):
    Etudiants = models.Etudiants.objects.get(pk=id)
    form = EtudiantsForm(Etudiants.__dict__)
    return render(request, "Etudiants/ajout.html",{"form":form, "id": id})

def Etudiants_updatetraitement(request, id):
    lform = EtudiantsForm(request.POST)
    if lform.is_valid():
        Etudiants = lform.save(commit = False)
        Etudiants.id = id
        Etudiants.save()
        return HttpResponseRedirect("/Etudiants")
    else:
        return render(request, "Etudiants/ajout.html", {"form": lform, "id":id})

def Etudiants_delete(request, id):
    Etudiants = models.Etudiants.objects.get(pk=id)
    Etudiants.delete()
    return HttpResponseRedirect("/Etudiants")