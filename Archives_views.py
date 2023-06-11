from django.shortcuts import render, HttpResponseRedirect
from .forms import ArchivesForm
from . import models

# Create your views here.

def Archives_index(request):
    liste = list(models.Archives.objects.all())
    return render(request,"Archives/index.html",{"liste" : liste})


def Archives_ajout(request):
    if request.method == "POST":
        form = ArchivesForm(request)
        if form.is_valid(): 
            Archives = form.save() 
            return render(request,"Archives/affiche.html",{"Archives" : Archives})
        else:
            return render(request,"Archives/ajout.html",{"form": form})
    else:
        form = ArchivesForm() 
        return render(request,"Archives/ajout.html",{"form" : form})
    

def Archives_traitement(request):
    lform = ArchivesForm(request.POST)
    if lform.is_valid():
        Archives = lform.save()
        return HttpResponseRedirect("/Archives")
    else:
        return render(request,"Archives/ajout.html",{"form": lform})
    


def Archives_affiche(request, id):
    Archives = models.Archives.objects.get(pk=id)
    return render(request,"Archives/affiche.html",{"Archives": Archives})

def Archives_update(request, id):
    Archives = models.Archives.objects.get(pk=id)
    form = ArchivesForm(Archives.__dict__)
    return render(request, "Archives/ajout.html",{"form":form, "id": id})

def Archives_updatetraitement(request, id):
    lform = ArchivesForm(request.POST)
    if lform.is_valid():
        Archives = lform.save(commit=False)
        Archives.id = id
        Archives.save()
        return HttpResponseRedirect("/Archives") 
    else:
        return render(request, "Archives/ajout.html", {"form": lform, "id":id})
    
def Archives_delete(request, id):
    Archives = models.Archives.objects.get(pk=id)
    Archives.delete()
    return HttpResponseRedirect("/Archives")