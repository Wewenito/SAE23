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
    groupe = models.ForeignKey("GroupeEtu", on_delete=models.CASCADE, default=None)
    photo = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    boursier = models.BooleanField()

class Cours(models.Model):
    Titre_cours = models.CharField(max_length=50, blank=False, null=False)
    enseignant = models.ForeignKey("Enseignant",on_delete=models.CASCADE, default=None)
    Groupes = models.ManyToManyField("GroupeEtu")

class Archives(models.Model):
    Etudiant = models.ForeignKey("Etudiants", on_delete=models.CASCADE, default=None)
    Cours = models.ForeignKey("Cours", on_delete=models.CASCADE, default=None)
    Explication = models.ForeignKey("Absences", related_name="explication_archives", on_delete=models.CASCADE, default=None)
    Justifie = models.ForeignKey("Absences", related_name="justifie_archives", on_delete=models.CASCADE, default=None)
    Justificatif = models.ForeignKey("Absences", related_name="justificatif_archives", on_delete=models.CASCADE, default=None)
    Justifie_par = models.ForeignKey("Absences", related_name="justifie_par_archives", on_delete=models.CASCADE, default=None)
    Commentaire_enseignant = models.ForeignKey("Absences", related_name="commentaire_enseignant_archives", on_delete=models.CASCADE, default=None)
    Inspection_finie = models.BooleanField()

class Absences(models.Model):
    Etudiant = models.ForeignKey("Etudiants", on_delete=models.CASCADE, default=None)
    Cours = models.ForeignKey("Cours", on_delete=models.CASCADE, default=None)
    Explication = models.CharField(max_length=200, blank=False, null=False)
    Justifie_bool = models.BooleanField(blank=False, null=False)
    Justif_url = models.CharField(max_length=200, blank=True, null=True)
    Checke_par = models.ForeignKey("Enseignant", on_delete=models.CASCADE, default=None)
    Commentaire_enseignant = models.CharField(max_length=100, blank=True, null=True)
    Inspection_terminee = models.BooleanField(blank=False, null=False) 