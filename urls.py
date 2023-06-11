from django.urls import path
from . import views, GroupeEtu_views, Etudiants_views, Cours_views, Archives_views, Absences_views

app_name = 'ABSENCES'

#enseignants
urlpatterns = [
    path('enseignants/', views.index),
    path('enseignants/ajout/', views.ajout),
    path('enseignants/traitement/', views.traitement), 
    path('enseignants/affiche/<int:id>/',views.affiche),
    path('enseignants/update/<int:id>/',views.update),
    path('enseignants/updatetraitement/<int:id>/', views.updatetraitement),
    path('enseignants/delete/<int:id>/', views.delete),


#groupeetu
    path('GroupeEtu/', GroupeEtu_views.GroupeEtu_index),
    path('GroupeEtu/ajout/', GroupeEtu_views.GroupeEtu_ajout),
    path('GroupeEtu/traitement/', GroupeEtu_views.GroupeEtu_traitement), 
    path('GroupeEtu/affiche/<int:id>/',GroupeEtu_views.GroupeEtu_affiche),
    path('GroupeEtu/update/<int:id>/',GroupeEtu_views.GroupeEtu_update),
    path('GroupeEtu/updatetraitement/<int:id>/', GroupeEtu_views.GroupeEtu_updatetraitement),
    path('GroupeEtu/delete/<int:id>/', GroupeEtu_views.GroupeEtu_delete),

#étudiants
    path('Etudiants/', Etudiants_views.Etudiants_index),
    path('Etudiants/ajout/', Etudiants_views.Etudiants_ajout),
    path('Etudiants/traitement/', Etudiants_views.Etudiants_traitement), 
    path('Etudiants/affiche/<int:id>/',Etudiants_views.Etudiants_affiche),
    path('Etudiants/update/<int:id>/',Etudiants_views.Etudiants_update),
    path('Etudiants/updatetraitement/<int:id>/', Etudiants_views.Etudiants_updatetraitement),
    path('Etudiants/delete/<int:id>/', Etudiants_views.Etudiants_delete),


#cours
    path('Cours/', Cours_views.Cours_index),
    path('Cours/ajout/', Cours_views.Cours_ajout),
    path('Cours/traitement/', Cours_views.Cours_traitement), 
    path('Cours/affiche/<int:id>/',Cours_views.Cours_affiche),
    path('Cours/update/<int:id>/',Cours_views.Cours_update),
    path('Cours/updatetraitement/<int:id>/', Cours_views.Cours_updatetraitement),
    path('Cours/delete/<int:id>/', Cours_views.Cours_delete),

#archives
    path('Archives/', Archives_views.Archives_index),
    path('Archives/ajout/', Archives_views.Archives_ajout),
    path('Archives/traitement/', Archives_views.Archives_traitement), 
    path('Archives/affiche/<int:id>/',Archives_views.Archives_affiche),
    path('Archives/update/<int:id>/',Archives_views.Archives_update),
    path('Archives/updatetraitement/<int:id>/', Archives_views.Archives_updatetraitement),
    path('Archives/delete/<int:id>/', Archives_views.Archives_delete),


#absences
    path('Absences/', Absences_views.Absences_index),
    path('Absences/ajout/', Absences_views.Absences_ajout),
    path('Absences/traitement/', Absences_views.Absences_traitement), 
    path('Absences/affiche/<int:id>/',Absences_views.Absences_affiche),
    path('Absences/update/<int:id>/',Absences_views.Absences_update),
    path('Absences/updatetraitement/<int:id>/', Absences_views.Absences_updatetraitement),
    path('Absences/delete/<int:id>/', Absences_views.Absences_delete),
]