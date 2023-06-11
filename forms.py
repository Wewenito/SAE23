from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class EnseignantForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = ('nom', 'prenom', 'mail')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prénom'),
            'mail' : _('Mail'),
}


class GroupeEtuForm(ModelForm):
    class Meta:
        model = models.GroupeEtu
        fields = ('nom_getu',)
        labels = {'nom_getu' : _('Nom du groupe')
}

class EtudiantsForm(ModelForm):
    class Meta:
        model = models.Etudiants
        fields = ('nom_etu', 'prenom', 'mail', 'photo', 'description', 'adresse', 'telephone', 'boursier')
        labels = {
            'nom_etu' : _('Nom étudiant'),
            'prenom' : _('Prénom'),
            'mail' : _('Mail'),
            'photo' : _('Photo'),
            'description' : _('Description'),
            'adresse' : _('Adresse'),
            'telephone' : _('Telephone'),
            'boursier' : _('Boursier ?'),

}

class CoursForm(ModelForm):
    class Meta:
        model = models.Cours
        fields = ('Titre_cours', 'Date', 'Duree')
        labels = {
            'Titre_cours' : _('Titre du cours'),
            'Date' : _('Date du cours'),
            'Duree' : _('Durée du cours'),

}

class ArchivesForm(ModelForm):
    class Meta:
        model = models.Archives
        fields = ('Inspection_finie',)
        labels = {
            'Inspection_finie' : _('Inspection finie ?'),


}
        
class AbsencesForm(ModelForm):
    class Meta:
        model = models.Absences
        fields = ('Explication', 'Justifie_bool', 'Justif_url', 'Commentaire_enseignant', 'Inspection_terminee')
        labels = {
            'Explication' : _('Explication'),
            'Justifie_bool' : _('Justifié ?'),
            'Justif_url' : _('Document'),
            'Commentaire_enseignant' : _('Commentaire enseignant'),
            'Inspection_terminee' : _('Inspection terminée ?'),

}