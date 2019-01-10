from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import search
from .models import Patient, Antecedant, Medecin
from .forms  import PatientForm, AntecedantForm, MedecinForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from search.views import MedicalData
from django.http import JsonResponse

# Create your views here.
@login_required
def dashboard(request):

	return render(request, "dashboard/dashboard.html")

@login_required
def rendezvous(request):

	return render(request, "dashboard/rendezvous.html")

@login_required
def dossiers(request):
	patients = Patient.objects.all().order_by('nom', 'prenom')
	return render(request ,"dashboard/dossiers.html", {'patients' : patients})

#fonction pour lire un patient donné
@login_required
def showPatient(request, pk):
	pk= int(pk) # make sure we have an integer.
	patient = Patient.objects.get(id=pk)
	antecedant = Antecedant.objects.filter(patient=patient)
	return render(request, "dashboard/showPatient.html", {'p': patient, 'antecedant': antecedant})

@login_required
def catalogue(request):

	return render(request, "dashboard/catalogue.html")

@login_required
def profil(request):
	user=request.user
	medecin = get_object_or_404(Medecin, pk=user.id)
	print(medecin.nom)
	if request.method == "POST":
		form = MedecinForm(request.POST, instance=medecin)
		if form.is_valid():
			post = form.save()
			return redirect('http://localhost:8000/dashboard/profil')
	else:
		form = MedecinForm(instance=medecin)
	return render(request, "dashboard/profil.html", {'form': form, 'm': medecin})



@login_required
def diagnostic(request, pk):
	pk= int(pk) # make sure we have an integer.
	patient = Patient.objects.get(id=pk)
	antecedant = Antecedant.objects.filter(patient=patient)
	return render(request, "dashboard/diagnostic.html", {'p': patient, 'antecedant': antecedant})


#vues pour ajouter un patient dans le système et le modifier par la suite
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
			return redirect('http://localhost:8000/dashboard/showPatient/{}'.format(post.pk))
	else:
		form = PatientForm(instance=patient)
	return render(request, 'dashboard/creer_patient.html', {'form': form})


@csrf_exempt
def listeMaladies(request, pk):
#	print("here")
#	print("eeee"+request.POST['texte'])

#	pk= int(pk) # make sure we have an integer.
	patient = Patient.objects.get(id=pk)

	listeMaladies = request.POST['texte'].split("-")

	return render(request, "dashboard/listeMaladies.html", {'p': patient, 'listeMaladies': listeMaladies}) 



def pagefinale(request, pk):
	import math

	some_var = request.POST.getlist('checks')
	print(some_var)
	diagnostic = search.views.diagnostic(some_var)
	s = dict()
	d = dict()
	for hit in diagnostic:
		s[hit['_source']['nomMaladie']] = hit['_score']
#		print(hit['_score'], hit['_source']['nomMaladie'])
	maxValue = s[(next(iter(s)))]
	print(maxValue)
	maladie = MedicalData.objects.get(nomMaladie = next(iter(s)))
	print(maladie.nomMaladie, maladie.listeSymptomes)

	cpt = 0
	for i in some_var:
		if i in maladie.listeSymptomes:
			cpt+=1


	coeff = ((cpt/(len(maladie.listeSymptomes.split(','))-1))*100)/maxValue

	for key, value in s.items():
		s[key] = math.ceil(value * coeff)

	for key, value in s.items():
		d[key.capitalize()] = value


	print(d)

	return render(request, "dashboard/pagefinale.html", {'d': d})

def detailMaladie(request):


	maladie = MedicalData.objects.get(nomMaladie = request.GET.get('nomMaladie'))
	details = {'nomMaladie': maladie.nomMaladie.capitalize(), 'description': maladie.description, 'listeSymptomes': maladie.listeSymptomes}
	return JsonResponse(details)

#vues pour ajouter, éditer les antécédents d'un patient
@login_required
def  addAntecedant(request):
	patient = Patient.objects.get(id=request.GET.get('idPatient'))
#	if request.method == "POST":
	nature = request.GET.get('modalNature')
	description = request.GET.get('modalDescription')
	antecedant = Antecedant.objects.create(nature = nature, description = description, patient = patient)
	details = {'nature': antecedant.nature, 'description': antecedant.description}
	return JsonResponse(details)

#maladie = MedicalData.objects.get(nomMaladie = request.GET.get('nomMaladie'))
#details = {'nomMaladie': maladie.nomMaladie.capitalize(), 'description': maladie.description, 'listeSymptomes': maladie.listeSymptomes}
#return JsonResponse(details)