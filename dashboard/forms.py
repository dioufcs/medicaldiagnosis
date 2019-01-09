from django import forms
from .models import *

"""Formulaire créé à partir du modèle Patient de notre application"""
class PatientForm(forms.ModelForm):
	 dateNaiss = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y", attrs={'type':'date'}))
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

class MedecinForm(forms.ModelForm):
	dateNaiss = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y", attrs={'type':'date'}))
	class Meta:
	    model = Medecin
	    exclude = ['user']