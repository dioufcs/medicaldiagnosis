from django.urls import path, include

from dashboard import views

app_name = 'dashboard'


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('rendezvous/', views.rendezvous, name='rendezvous'),
    path('dossiers/', views.dossiers, name='dossiers'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('profil/', views.profil, name='profil'),
    path('nouveau_patient', views.creer_patient, name='nouveau_patient'),
    path('edit_patient/<pk>', views.edit_patient, name='edit_patient'),
    path('diagnostic/', views.diagnostic, name='diagnostic'),
    path('listeMaladies/', views.listeMaladies, name='listeMaladies'),
    path('pagefinale/', views.pagefinale, name='pagefinale'),

]