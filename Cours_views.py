from django.shortcuts import render, HttpResponseRedirect
from .forms import CoursForm
from . import models

# Create your views here.

def Cours_index(request):
    liste = list(models.Cours.objects.all())
    return render(request,"Cours/index.html",{"liste" : liste})


def Cours_ajout(request):
    if request.method == "POST":
        form = CoursForm(request)
        if form.is_valid(): 
            Cours = form.save() 
            return render(request,"Cours/affiche.html",{"Cours" : Cours})
        else:
            return render(request,"Cours/ajout.html",{"form": form})
    else:
        form = CoursForm() 
        return render(request,"Cours/ajout.html",{"form" : form})
    

def Cours_traitement(request):
    lform = CoursForm(request.POST)
    if lform.is_valid():
        Cours = lform.save()
        return HttpResponseRedirect("/Cours")
    else:
        return render(request,"Cours/ajout.html",{"form": lform})
    


def Cours_affiche(request, id):
    Cours = models.Cours.objects.get(pk=id)
    return render(request,"Cours/affiche.html",{"Cours": Cours})

def Cours_update(request, id):
    Cours = models.Cours.objects.get(pk=id)
    form = CoursForm(Cours.__dict__)
    return render(request, "Cours/ajout.html",{"form":form, "id": id})

def Cours_updatetraitement(request, id):
    lform = CoursForm(request.POST)
    if lform.is_valid():
        Cours = lform.save(commit=False)
        Cours.id = id
        Cours.save()
        return HttpResponseRedirect("/Cours") 
    else:
        return render(request, "Cours/ajout.html", {"form": lform, "id":id})
    
def Cours_delete(request, id):
    Cours = models.Cours.objects.get(pk=id)
    Cours.delete()
    return HttpResponseRedirect("/Cours")