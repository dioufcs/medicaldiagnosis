from django.urls import path, include

from dashboard import views

app_name = 'dashboard'


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('rendezvous/', views.rendezvous, name='rendezvous'),
    path('dossiers/', views.dossiers, name='dossiers'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('profil/', views.profil, name='profil'),


    path('diagnostic/', views.diagnostic, name='diagnostic'),
    path('listeMaladies/', views.listeMaladies, name='listeMaladies'),
    path('pagefinale/', views.pagefinale, name='pagefinale'),

    path('nouveauPatient/', views.creer_patient, name='nouveauPatient'),
    path('editPatient/<pk>', views.editPatient, name='editPatient'),
    path('showPatient/<pk>', views.showPatient, name='showPatient'),
    path('nouvelAntecedant/<pk>', views.addAntecedant, name='nouvelAntecedant')
]