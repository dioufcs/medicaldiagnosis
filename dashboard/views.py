from django.shortcuts import render, redirect, get_object_or_404
from .forms  import PatientForm
from .models import Patient

# Create your views here.

def dashboard(request):

	return render(request, "dashboard/dashboard.html")

def rendezvous(request):

	return render(request, "dashboard/rendezvous.html")

def dossiers(request):

	return render(request, "dashboard/dossiers.html")

def catalogue(request):

	return render(request, "dashboard/catalogue.html")

def profil(request):

	return render(request, "dashboard/profil.html")

#vue pour ajouter un patient dans le système
def creer_patient(request):
	if request.method == "POST":
		form = PatientForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('dashboard/dossiers.html', pk=post.pk)
	else:
		form = PatientForm()
	return render(request, 'dashboard/creer_patient.html', {'form': form})

def edit_patient(request, pk):
	patient = get_object_or_404(Patient, pk=pk)
	if request.method == "POST":
		form = PatientForm(request.POST, instance = patient)
		if form.is_valid():
			patient = form.save(commit=False)
			patient.save()
			return redirect ('dashboard/dossiers.html', pk=post.pk)
	else:
		form = PatientForm(instance=patient)
	return render(request, 'dashboard/creer_patient.html', {'form': form})