from django.shortcuts import render, HttpResponseRedirect
from .forms import AbsencesForm
from . import models

# Create your views here.

def Absences_index(request):
    liste = list(models.Absences.objects.all())
    return render(request,"Absences/index.html",{"liste" : liste})


def Absences_ajout(request):
    if request.method == "POST":
        form = AbsencesForm(request)
        if form.is_valid(): 
            Absences = form.save() 
            return render(request,"Absences/affiche.html",{"Absences" : Absences})
        else:
            return render(request,"Absences/ajout.html",{"form": form})
    else:
        form = AbsencesForm() 
        return render(request,"Absences/ajout.html",{"form" : form})
    

def Absences_traitement(request):
    lform = AbsencesForm(request.POST)
    if lform.is_valid():
        Absences = lform.save()
        return HttpResponseRedirect("/Absences")
    else:
        return render(request,"Absences/ajout.html",{"form": lform})
    


def Absences_affiche(request, id):
    Absences = models.Absences.objects.get(pk=id)
    return render(request,"Absences/affiche.html",{"Absences": Absences})

def Absences_update(request, id):
    Absences = models.Absences.objects.get(pk=id)
    form = AbsencesForm(Absences.__dict__)
    return render(request, "Absences/ajout.html",{"form":form, "id": id})

def Absences_updatetraitement(request, id):
    lform = AbsencesForm(request.POST)
    if lform.is_valid():
        Absences = lform.save(commit=False)
        Absences.id = id
        Absences.save()
        return HttpResponseRedirect("/Absences") 
    else:
        return render(request, "Absences/ajout.html", {"form": lform, "id":id})
    
def Absences_delete(request, id):
    Absences = models.Absences.objects.get(pk=id)
    Absences.delete()
    return HttpResponseRedirect("/Absences")