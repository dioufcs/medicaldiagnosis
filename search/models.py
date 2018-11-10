from django.db import models
from dashboard.models import Maladie
from django.db.models.signals import m2m_changed

class MedicalData(models.Model):
	nomMaladie = models.CharField(max_length=50, unique=True)
	listeSymptomes = models.TextField(blank=True)


def add_symptoms(sender, **kwargs):
	if kwargs['action'] == "post_add":
		instance = kwargs['instance']
		maladie = MedicalData.objects.get(nomMaladie=instance.nomMaladie)
		string = ""
		for i in instance.symptomes.all():
			string += i.nomSymptome+", "
		maladie.listeSymptomes = string
		maladie.save()

m2m_changed.connect(add_symptoms, sender = Maladie.symptomes.through)
