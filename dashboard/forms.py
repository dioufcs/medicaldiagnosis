from django import forms
from .models import *

class PatientForm(forms.ModelForm):
	"""Formulaire créé à partir du modèle Patient de notre application"""
	class Meta:
	    model = Patient
	    fields = ('__all__')