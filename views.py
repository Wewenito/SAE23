from django.shortcuts import render, HttpResponseRedirect
from .forms import EnseignantForm
from . import models

# Create your views here.

def index(request):
    liste = list(models.Enseignant.objects.all())
    return render(request,"enseignants/index.html",{"liste" : liste})


def ajout(request):
    if request.method == "POST":
        form = EnseignantForm(request)
        if form.is_valid(): 
            Enseignant = form.save() 
            return render(request,"enseignants/affiche.html",{"Enseignant" : Enseignant})
        else:
            return render(request,"enseignants/ajout.html",{"form": form})
    else:
        form = EnseignantForm() 
        return render(request,"enseignants/ajout.html",{"form" : form})
    

def traitement(request):
    lform = EnseignantForm(request.POST)
    if lform.is_valid():
        Enseignant = lform.save()
        return HttpResponseRedirect("/enseignants")
    else:
        return render(request,"enseignants/ajout.html",{"form": lform})
    


def affiche(request, id):
    Enseignant = models.Enseignant.objects.get(pk=id)
    return render(request,"enseignants/affiche.html",{"Enseignant": Enseignant})

def update(request, id):
    Enseignant = models.Enseignant.objects.get(pk=id)
    form = EnseignantForm(Enseignant.__dict__)
    return render(request, "enseignants/ajout.html",{"form":form, "id": id})

def updatetraitement(request, id):
    lform = EnseignantForm(request.POST)
    if lform.is_valid():
        Enseignant = lform.save(commit=False)
        Enseignant.id = id
        Enseignant.save()
        return HttpResponseRedirect("/enseignants") 
    else:
        return render(request, "enseignants/ajout.html", {"form": lform, "id":id})
    
def delete(request, id):
    Enseignant = models.Enseignant.objects.get(pk=id)
    Enseignant.delete()
    return HttpResponseRedirect("/enseignants")