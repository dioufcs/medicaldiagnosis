from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms  import PatientForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):

	return render(request, "dashboard/dashboard.html")

@login_required
def rendezvous(request):

	return render(request, "dashboard/rendezvous.html")

@login_required
def dossiers(request):
	patients = Patient.objects.all()
	return render(request ,"dashboard/dossiers.html", {'patients' : patients})

#fonction pour lire un patient donné
@login_required
def showPatient(request, pk):
	pk= int(pk) # make sure we have an integer.
	patient = Patient.objects.get(id=pk)
	return render(request, "dashboard/showPatient.html", {'p': patient})

@login_required
def catalogue(request):

	return render(request, "dashboard/catalogue.html")

@login_required
def profil(request):

	return render(request, "dashboard/profil.html")

#vue pour ajouter un patient dans le système
@login_required
def creer_patient(request):
	if request.method == "POST":
		form = PatientForm(request.POST or None)
		if form.is_valid():
			post = form.save()
			return redirect('http://localhost:8000/dashboard/showPatient/{}'.format(post.pk), pk=post.pk)
	else:
		form = PatientForm()
	return render(request, 'dashboard/creer_patient.html', {'form': form})

@login_required
def editPatient(request, pk):
	patient = get_object_or_404(Patient, pk=pk)
	if request.method == "POST":
		form = PatientForm(request.POST, instance = patient)
		if form.is_valid():
			post = form.save()
			return redirect('http://localhost:8000/dashboard/showPatient/{}'.format(post.pk), pk=post.pk)
	else:
		form = PatientForm(instance=patient)
	return render(request, 'dashboard/creer_patient.html', {'form': form})