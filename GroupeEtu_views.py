from django.shortcuts import render, HttpResponseRedirect
from .forms import GroupeEtuForm
from . import models

# Create your views here.

def GroupeEtu_index(request):
    liste = list(models.GroupeEtu.objects.all())
    return render(request,"GroupeEtu/index.html",{"liste" : liste})


def GroupeEtu_ajout(request):
    if request.method == "POST":
        form = GroupeEtuForm(request)
        if form.is_valid(): 
            GroupeEtu = form.save() 
            return render(request,"GroupeEtu/affiche.html",{"GroupeEtu" : GroupeEtu})
        else:
            return render(request,"GroupeEtu/ajout.html",{"form": form})
    else:
        form = GroupeEtuForm() 
        return render(request,"GroupeEtu/ajout.html",{"form" : form})
    

def GroupeEtu_traitement(request):
    lform = GroupeEtuForm(request.POST)
    if lform.is_valid():
        GroupeEtu = lform.save()
        return HttpResponseRedirect("/GroupeEtu")
    else:
        return render(request,"GroupeEtu/ajout.html",{"form": lform})
    


def GroupeEtu_affiche(request, id):
    GroupeEtu = models.GroupeEtu.objects.get(pk=id)
    return render(request,"GroupeEtu/affiche.html",{"GroupeEtu": GroupeEtu})

def GroupeEtu_update(request, id):
    GroupeEtu = models.GroupeEtu.objects.get(pk=id)
    form = GroupeEtuForm(GroupeEtu.__dict__)
    return render(request, "GroupeEtu/ajout.html",{"form":form, "id": id})

def GroupeEtu_updatetraitement(request, id):
    lform = GroupeEtuForm(request.POST)
    if lform.is_valid():
        GroupeEtu = lform.save(commit=False)
        GroupeEtu.id = id
        GroupeEtu.save()
        return HttpResponseRedirect("/GroupeEtu") 
    else:
        return render(request, "GroupeEtu/ajout.html", {"form": lform, "id":id})
    
def GroupeEtu_delete(request, id):
    GroupeEtu = models.GroupeEtu.objects.get(pk=id)
    GroupeEtu.delete()
    return HttpResponseRedirect("/GroupeEtu")