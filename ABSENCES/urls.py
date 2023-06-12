from django.urls import path

from . import views

app_name = 'ABSENCES'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signin/',views.signin, name='signin'),
    path('profile/<int:id>/',views.profile_ens, name='profile'),
    path('profil/update_mail_ens/<int:id>/', views.update_mail_ens, name='update_mail_ens'),

    path('ajout_cour/', views.ajout_cour, name='ajout_cour'),

    path('Afficher_groupes/', views.Afficher_groupes, name="Afficher_groupes"),
    path('ajout_groupe/', views.ajout_groupe, name='ajout_groupe'),
]