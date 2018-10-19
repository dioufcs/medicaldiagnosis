from django.db import models
from django.contrib.auth.models import User

class Personne (models.Model):
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	tel = models.IntegerField()
	adresse = models.CharField(max_length=50)
	dateNaiss = models.DateField()

	class Meta:
		abstract = True

class Medecin (Personne):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	specialite = models.CharField(max_length=20)
	lieuTravail = models.CharField(max_length=20)

class Patient (Personne):
	profession = models.CharField(max_length=20)
	situationMatr = models.CharField(max_length=10)
	assurance = models.CharField(max_length=10)
	securiteSociale = models.IntegerField()

class Consultation (models.Model):
	date = models.DateField()
	poids = models.FloatField()
	temperature = models.FloatField()
	tension = models.FloatField()
	motifs = models.CharField(max_length=500)
	examenClinique = models.CharField(max_length=500)
	diagnostic = models.CharField(max_length=100)

	models.ForeignKey(Medecin, on_delete=models.CASCADE)
	models.ForeignKey(Patient, on_delete=models.CASCADE)

class Antecedant (models.Model):
	nature = models.CharField(max_length=15)
	description = models.CharField(max_length=30)
	
	models.ForeignKey(Patient, on_delete=models.CASCADE)