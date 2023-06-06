from django.shortcuts import render

# Create your views here.

def getMainPage(request):
    return render(request, 'MAIN PAGE/mp.html')