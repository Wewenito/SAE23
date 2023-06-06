from django.urls import path

from . import views

app_name = 'ABSENCES'

urlpatterns = [
    path('', views.getMainPage),
]