from django.db import models

# Create your models here.

class Enseignant(models.Model):
    nom = models.CharField(max_length=50, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=False, null=False)
    mail = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.nom}-{self.prenom}"

class GroupeEtu(models.Model):
    nom = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.nom}"

class Cours(models.Model):
    Titre_cours = models.CharField(max_length=50, blank=False, null=False)
    enseignant = models.ForeignKey("Enseignant",on_delete=models.CASCADE, default=None, blank=True, null=True)
    Groupes = models.ForeignKey("GroupeEtu", on_delete=models.DO_NOTHING, default=None)
    Date = models.DateTimeField(blank=True, null=True)
    Duree = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.Titre_cours}"
    
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


    def __str__(self):
        return f"{self.nom}-{self.prenom}"

class Absences(models.Model):
    Etudiant = models.ForeignKey("Etudiants", on_delete=models.CASCADE, default=None)
    Cours = models.ForeignKey("Cours", on_delete=models.CASCADE, default=None)
    Explication = models.CharField(max_length=200, blank=False, null=False)
    Justifie_bool = models.BooleanField(blank=False, null=False)
    Justif_url = models.FileField(upload_to='justifications/', default='justifications/test.pdf')
    Checke_par = models.ForeignKey("Enseignant", on_delete=models.CASCADE, default=None, blank=True, null=True)
    Commentaire_enseignant = models.CharField(max_length=100, blank=True, null=True)
    Inspection_terminee = models.BooleanField(blank=False, null=False) 