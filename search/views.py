from django.shortcuts import render
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from .documents import *
from django.http import JsonResponse


def search (texte):
	test = True
	listeSymptomes = list()

	client = Elasticsearch()
	s = Search(using=client)
	#texte = " hémorragie cérébrale.j'ai une acouphène diarrhée, douleurs abdominales, nausées, vomissements,  et de la fièvre sans oublier les lésions cérébrales  maux de tête et la diarrhée je ne m'appelle pas Biram mais abcès dans la région de l'aine lol mdr"
	#texte = "diarrhée et fièvre"
	while test:
		test = False
		s = Search().using(client).query("match", nomSymptome=texte)
		#print(s.execute())
		for i in list(s.execute()):
			if texte.__contains__(i.nomSymptome):
				print(i.nomSymptome)
				listeSymptomes.append(i.nomSymptome)
				texte = texte.replace(i.nomSymptome, '')

				test = True
		
	return listeSymptomes

def query(listeSymptomes):
	q = {"query": {"bool" : {"should" : []}}}

	for i in listeSymptomes:
		q['query']['bool']['should'].append({"match" : { "listeSymptomes" : i }})
	print(q)
	return q

def diagnostic(listeSymptomes):

	client = Elasticsearch()

	response = client.search(
	    index="medicaldata",
	    body = query(listeSymptomes)
	#    body={
	#	  "query": {
	#	    "bool" : {
	#	       "should" : [
	#	       	{ "match" : { "listeSymptomes" : "diarrhée" } },
	#	        { "match" : { "listeSymptomes" : "douleurs abdominales" } },
	#	        { "match" : { "listeSymptomes" : "nausées" } },
	#	        { "match" : { "listeSymptomes" : "vomissements" } },
	#	      ],
	#	    }
	#	  }
	#	}


	)
	return response['hits']['hits'][:5]

#	for hit in response['hits']['hits'][:5]:
#		print(hit['_score'], hit['_source']['nomMaladie'])

def synthetiseur(request):
	import speech_recognition as sr
	import os
	import time

	time.sleep(2)

	#AUDIO_FILE = os.path.join(os.path.dirname('/Users/dioufcheikhsadibou/Downloads/'), request.GET.get('url').replace(':', '_'))
	AUDIO_FILE = os.path.join(os.path.dirname('/Users/dioufcheikhsadibou/Downloads/'), '2019-01-01T23_20_40.152Z.wav')
	print("AUDIO_FILE :",AUDIO_FILE)
	#print(request.GET.get('url'))
	# obtain audio from the microphone
	r = sr.Recognizer()
	#audio = r.record(request.GET.get('url'))


	harvard = sr.AudioFile(AUDIO_FILE)
	with harvard as source:
		audio = r.record(source)

#	with sr.Microphone() as source:
#	    r.adjust_for_ambient_noise(source)
#	    print("Dites quelque chose!")
#	    audio = r.record(source, duration=1)


	print('ok')
	# recognize speech using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
#		print("Google Speech Recognition pense que vous avez dit: " + r.recognize_google(audio, language="fr-FR"))
#		texte = {'texte': '-'.join(search(r.recognize_google(audio, language="fr-FR")))}
		texte = {'texte': '-'.join(search('J\'ai des maux de têtes, une fièvre, maux de tête et une diarrhée'))}
		#print('-'.join(listeSymptomes['listeSymptomes']))
		return JsonResponse(texte)
	     
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))

	

	#texte = {'texte':r.recognize_google(audio, language="fr-FR")}
	#return JsonResponse(texte)

def instantSearch(request):
	

	from dashboard.models import Symptome
	import time
	start_time = time.time()

	res = list(Symptome.objects.filter(nomSymptome__startswith=request.GET.get('nomMaladie')))
	res[:] = map(lambda x: x.nomSymptome, res)
	print("--- %s seconds ---" % (time.time() - start_time))
	propositions = {'propositions': '-'.join(res)}
	return JsonResponse(propositions)
