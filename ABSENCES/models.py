from django.db import models

# Create your models here.



class Enseignant(models.Model):
    nom = models.CharField(max_length=50, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=False, null=False)
    mail = models.CharField(max_length=50, blank=False, null=False)

class GroupeEtu(models.Model):
    nom = models.CharField(max_length=50, blank=False, null=False)
    
class Etudiants(models.Model):
    nom = models.CharField(max_length=50, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=False, null=False)
    mail = models.CharField(max_length=50, blank=False, null=False)
    #groupe = models.ForeignKey("GroupeEtu", default=None)
    photo = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    boursier = models.BooleanField()

class Cours(models.Model):
    Titre_cours = models.CharField(max_length=50, blank=False, null=False)
    Date = models.DateField(max_length=50, blank=False, null=False)
    #enseignant = models.ForeignKey("Enseignant", default=None)
    Duree = models.TimeField(blank=False, null=False)
    #Groupe = models.ForeignKey("GroupeEtu", default=None)

class Archives(models.Model):
    #Etudiant = models.ForeignKey("Etudiants", default=None)
    #Cours = models.ForeignKey("Cours", default=None)
    #Explication = models.ForeignKey("Absences", default=None)
    #Justifie = models.ForeignKey("Absences", default=None)
    #Justificatif = models.ForeignKey("Absences", default=None)
    #Justifie_par = models.ForeignKey("Absences", default=None)
    #Commentaire_enseignant = models.ForeignKey("Absences", default=None)
    Inspection_finie = models.BooleanField()

class Absences(models.Model):
    #Etudiant = models.ForeignKey("Etudiants", default=None)
    #Cours = models.ForeignKey("Cours", default=None)
    Explication = models.CharField(max_length=200, blank=False, null=False)
    Justifie_bool = models.BooleanField(blank=False, null=False)
    Justif_url = models.CharField(max_length=200, blank=True, null=True)
    #Checke_par = models.ForeignKey("Enseignant", default=None)
    Commentaire_enseignant = models.CharField(max_length=100, blank=True, null=True)
    Inspection_terminee = models.BooleanField(blank=False, null=False) 