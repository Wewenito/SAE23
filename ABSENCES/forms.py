from django import forms
from .models import GroupeEtu, Cours

class GroupeEtuForm(forms.ModelForm):
    class Meta:
        model = GroupeEtu
        fields = ['nom']


class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = '__all__'
