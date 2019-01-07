from django import forms
from .models import *


class PatientForm(forms.ModelForm):
	"""Formulaire créé à partir du modèle Patient de notre application"""
	class Meta:
	    model = Patient
	    fields = ('__all__')

class AntecedantForm(forms.ModelForm):
	class Meta:
		model = Antecedant
		fields = ('__all__')

class ConsultationForm(forms.ModelForm):
	class Meta:
		model = Consultation
		fields = ('__all__')