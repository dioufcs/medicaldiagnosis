from django.shortcuts import render, redirect, get_object_or_404
from .forms  import PatientForm
from .models import Patient
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import search

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

def diagnostic(request):

	return render(request, "dashboard/diagnostic.html")


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


@csrf_exempt
def listeMaladies(request):
#	print("here")
#	print("eeee"+request.POST['texte'])


	return render(request, "dashboard/listeMaladies.html", {'listeMaladies': request.POST['texte'].split("-")}) 



def pagefinale(request):
	some_var = request.POST.getlist('checks')
	print(some_var)
	diagnostic = search.views.diagnostic(some_var)
	s = dict()
	for hit in diagnostic:
		s[hit['_source']['nomMaladie']] = hit['_score']
#		print(hit['_score'], hit['_source']['nomMaladie'])
	print(s)
	return render(request, "dashboard/pagefinale.html", {'s': s})