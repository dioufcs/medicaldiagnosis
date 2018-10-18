from django.shortcuts import render

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