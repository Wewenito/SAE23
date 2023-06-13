from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Sélectionnez un fichier CSV')