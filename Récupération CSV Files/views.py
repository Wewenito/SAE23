import csv
from django.shortcuts import render

def upload_csv(request):
    if request.method == 'POST' and 'csv_file' in request.FILES:
        csv_file = request.FILES['csv_file']
        if csv_file:
            # Lire le contenu du fichier CSV
            csv_data = csv_file.read().decode('utf-8').splitlines()

            # Convertir les données CSV en une liste
            data = list(csv.reader(csv_data))

            return render(request, 'myfirstapp/csv_display.html', {'data': data})

    return render(request, 'myfirstapp/upload_csv.html')

def index(request):
    return render(request, 'myfirstapp/index.html')
