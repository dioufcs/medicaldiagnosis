from django.db import models
from django.contrib.auth.models import User

#verbose_name permet de gérer l'affichage du champ (le label)
class Personne (models.Model):
	nom = models.CharField(max_length=30, verbose_name='Nom')
	prenom = models.CharField(max_length=30, verbose_name='Prénom')
	tel = models.IntegerField(verbose_name='Téléphone')
	adresse = models.CharField(max_length=50, verbose_name='Adresse')
	dateNaiss = models.DateField(verbose_name='Date de naissance')

	class Meta:
		abstract = True

class Medecin (Personne):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	specialite = models.CharField(max_length=20, verbose_name='Spécialité')
	lieuTravail = models.CharField(max_length=20, verbose_name='Lieu de travail')

class Patient (Personne):
	profession = models.CharField(max_length=20, verbose_name='Profession')
	situationMatr = models.CharField(max_length=10, verbose_name="Situation Matrimoniale")
	assurance = models.CharField(max_length=10, verbose_name="Assurance")
	securiteSociale = models.CharField(max_length=13, verbose_name="N° Sécurité sociale")

class Consultation (models.Model):
	date = models.DateField(verbose_name='Date de consultation')
	poids = models.FloatField(verbose_name='Poids')
	temperature = models.FloatField(verbose_name='temperature')
	tension = models.FloatField(verbose_name='Tension')
	motifs = models.CharField(max_length=500, verbose_name='Motifs')
	examenClinique = models.CharField(max_length=500, verbose_name='Examen Clinique')
	diagnostic = models.CharField(max_length=100, verbose_name='Diagnostic')

	models.ForeignKey(Medecin, on_delete=models.DO_NOTHING)
	models.ForeignKey(Patient, on_delete=models.DO_NOTHING)

class Antecedant (models.Model):
	nature = models.CharField(max_length=15, verbose_name="Nature de l'antécédant")
	description = models.CharField(max_length=30, verbose_name="Description de l'année")
	
	models.ForeignKey(Patient, on_delete=models.CASCADE)