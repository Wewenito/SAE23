from django import forms
from .models import GroupeEtu, Cours, Etudiants, Enseignant, Absences

class GroupeEtuForm(forms.ModelForm):
    class Meta:
        model = GroupeEtu
        fields = ['nom']


class CoursForm(forms.ModelForm):
    Groupes = forms.ModelChoiceField(queryset=GroupeEtu.objects.all())
    enseignant = forms.ModelChoiceField(queryset=Enseignant.objects.all())

    class Meta:
        model = Cours
        fields = [
            'Titre_cours', 
            'enseignant', 
            'Groupes', 
            'Date', 
            'Duree',
            ]

class EtudiantsForm(forms.ModelForm):
    groupe = forms.ModelChoiceField(queryset=GroupeEtu.objects.all())

    class Meta:
        model = Etudiants
        fields = ['nom', 'prenom', 'mail', 'groupe', 'photo', 'description', 'adresse', 'telephone', 'boursier']



class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'mail']


class AbsenceForm(forms.ModelForm):
    Checke_par = forms.ModelChoiceField(queryset=Enseignant.objects.all(), required=False)

    class Meta:
        model = Absences
        fields = ['Etudiant', 'Cours', 'Explication', 'Justifie_bool', 'Justif_url', 'Checke_par', 'Commentaire_enseignant', 'Inspection_terminee']
