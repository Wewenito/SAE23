from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
]