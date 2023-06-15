from django.urls import path

from . import views

app_name = 'ABSENCES'

urlpatterns = [
    path('home/', views.home, name='home'),

    path('signin/',views.signin, name='signin'),

    #///////////////////////////////////////////////etudiant////////////////////////////////////////////////////

    path('gestion_etudiants/<str:arg1>/', views.gestion_etudiants, name='gestion_etudiants'),
    path('acceuil_etu/<int:id>/', views.acceuil_etu, name='acceuil_etu'),

    path('Ajouter_absence/', views.Ajouter_absence, name='Ajouter_absence'),

    #/////////////////////////////////////////////enseignant////////////////////////////////////////////////////

    path('Afficher_etudiants/', views.Afficher_etudiants, name='Afficher_etudiants'),
    path('Ajouter_etudiants/', views.Ajouter_etudiants, name='Ajouter_etudiants'),
    path('supprimer_etudiant/<int:id>/', views.supprimer_etudiant, name='supprimer_etudiant'),
    path('modifier_etudiant/<int:id>/', views.modifier_etudiant, name='modifier_etudiant'),
    path('afficher_modif_form/<int:id>/', views.afficher_modif_form, name='afficher_modif_form'),


    path('profil/update_mail_ens/<int:id>/', views.update_mail_ens, name='update_mail_ens'),

    path('Gestion_enseignants/<str:arg1>/', views.Gestion_enseignants, name='Gestion_enseignants'),
    path('Gestion_enseignants/<str:arg1>/<int:id>/', views.Gestion_enseignants, name='Gestion_enseignants'),

    path('Afficher_groupes/', views.Afficher_groupes, name='Afficher_groupes'),
    path('ajout_groupe/', views.ajout_groupe, name='ajout_groupe'),
    path('suppression_groupe/<int:id>/', views.suppression_groupe, name='suppression_groupe'),
    path('modification_groupe/<int:id>/', views.modification_groupe, name='modification_groupe'),

    path('Ajouter_cour/', views.Ajouter_cour, name='Ajouter_cour'),
    path('Afficher_cours/', views.Afficher_cours, name='Afficher_cours'),
    path('Supprimer_cour/<int:id>/', views.Supprimer_cour, name='Supprimer_cour'),
    path('afficher_modif_form_cour/<int:id>/', views.afficher_modif_form_cour, name='afficher_modif_form_cour'),
    path('modifier_cour/<int:id>/', views.modifier_cour, name='modifier_cour'),


    path('Afficher_enseignants/', views.Afficher_enseignants, name='Afficher_enseignants'),
    path('Ajouter_enseignants/', views.Ajouter_enseignants, name='Ajouter_enseignants'),
    path('Supprimer_enseignant/<int:id>/', views.Supprimer_enseignant, name='Supprimer_enseignant'),
    path('afficher_modif_form_ens/<int:id>/', views.afficher_modif_form_ens, name='afficher_modif_form_ens'),
    path('modifier_enseignant/<int:id>/', views.modifier_enseignant, name='modifier_enseignant'),

]