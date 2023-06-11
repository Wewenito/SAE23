from django.db import models

# Create your models here.


class Enseignant(models.Model):
    nom = models.CharField(max_length=50, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=False, null=False)
    mail = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        chaine = f"L'enseignant : {self.nom} {self.mail}. Adresse de contact : {self.mail}"
        return chaine
    
    def dico(self):
        return {"nom":self.nom, "prenom": self.prenom, "mail":self.mail}

class GroupeEtu(models.Model):
    nom_getu = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        chaine = f"L'étudiant appartient au {self.nom_getu}"
        return chaine
    
    def GroupeEtu(self):
        return {"nom_getu":self.nom_getu}
    
class Etudiants(models.Model):
    nom_etu = models.CharField(max_length=50, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=False, null=False)
    mail = models.CharField(max_length=50, blank=False, null=False)
    #groupe = models.ForeignKey("GroupeEtu", default=None)
    photo = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    boursier = models.BooleanField()

    def __str__(self):
        chaine = f"Etudiant : {self.nom_etu} {self.prenom}. Adresse de contact : {self.mail}. Photo : {self.photo}. Description : {self.description}. Adresse : {self.adresse}. Téléphone : {self.telephone}. Boursier ? {self.boursier}"
        return chaine
    
    def Etudiants(self):
        return {"nom_etu":self.nom_etu, "prenom":self.prenom, "mail":self.mail, "photo":self.photo, "description":self.description, "adresse":self.adresse, "telephone":self.telephone, "boursier":self.boursier}

class Cours(models.Model):
    Titre_cours = models.CharField(max_length=50, blank=False, null=False)
    Date = models.DateField(max_length=50, blank=False, null=False)
    #enseignant = models.ForeignKey("Enseignant", default=None)
    Duree = models.TimeField(blank=False, null=False)
    #Groupe = models.ForeignKey("GroupeEtu", default=None)

    def __str__(self):
        chaine = f"Le cours : {self.Titre_cours}, aura lieu le {self.Date} pour une durée de {self.Duree}"
        return chaine
    
    def Cours(self):
        return {"Titre_cours":self.Titre_cours, "Date":self.Date, "Duree":self.Duree}

class Archives(models.Model):
    #Etudiant = models.ForeignKey("Etudiants", default=None)
    #Cours = models.ForeignKey("Cours", default=None)
    #Explication = models.ForeignKey("Absences", default=None)
    #Justifie = models.ForeignKey("Absences", default=None)
    #Justificatif = models.ForeignKey("Absences", default=None)
    #Justifie_par = models.ForeignKey("Absences", default=None)
    #Commentaire_enseignant = models.ForeignKey("Absences", default=None)
    Inspection_finie = models.BooleanField()

    def __str__(self):
        chaine = f"Inspection_finie {self.Inspection_finie}"
        return chaine
    
    def Archives(self):
        return {"Inspection_finie":self.Inspection_finie}

class Absences(models.Model):
    #Etudiant = models.ForeignKey("Etudiants", default=None)
    #Cours = models.ForeignKey("Cours", default=None)
    Explication = models.CharField(max_length=200, blank=False, null=False)
    Justifie_bool = models.BooleanField(blank=False, null=False)
    Justif_url = models.CharField(max_length=200, blank=True, null=True)
    #Checke_par = models.ForeignKey("Enseignant", default=None)
    Commentaire_enseignant = models.CharField(max_length=100, blank=True, null=True)
    Inspection_terminee = models.BooleanField(blank=False, null=False)

    def __str__(self):
        chaine = f"Explication de l'absences : {self.Explication}, Justifié ? {self.Justifie_bool}, Document : {self.Justif_url}, Commentaire de l'enseignant : {self.Commentaire_enseignant}, Inspection terminée ? : {self.Inspection_terminee}"
        return chaine
    
    def Absences(self):
        return {"Explication":self.Explication, "Justifie_bool":self.Justifie_bool, "Justif_url":self.Justif_url, "Commentaire_enseignant" :self.Commentaire_enseignant, "Inspection_terminee" : self.Inspection_terminee}