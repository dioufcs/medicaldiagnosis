from django.urls import path, include

from . import views

app_name = 'dashboard'


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('rendezvous/', views.rendezvous, name='rendezvous'),
    path('dossiers/', views.dossiers, name='dossiers'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('profil/', views.profil, name='profil'),
    path('nouveauPatient/', views.creer_patient, name='nouveauPatient'),
    path('editPatient/<pk>', views.editPatient, name='editPatient'),
    path('showPatient/<pk>', views.showPatient, name='showPatient')
]