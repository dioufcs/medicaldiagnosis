from dashboard.models import *
import io

def fillBD():
	with open('search/medicaldataFR.txt', 'r', encoding='latin-1') as mon_fichier:
	#with io.open('search/medicaldataFR.txt','r',encoding='utf-8') as mon_fichier:
		#while mon_fichier.read(1):
		while mon_fichier.readline():
			ligne_maladie = mon_fichier.readline().strip('\n')
			ligne_description = mon_fichier.readline().strip('\n')
			m = Maladie(nomMaladie = ligne_maladie, description = ligne_description)
			m.save()
			ligne_symptomes = mon_fichier.readline().strip('\n')
			ligne_symptomes = ligne_symptomes.replace(' ou ', ', ').replace(' et ', ', ')
			ligne_s = ligne_symptomes.split(', ')
			for i in ligne_s:
				try:
					s = Symptome.objects.get(nomSymptome = i)
				except Symptome.DoesNotExist:
					s = None
				if not s:
					s = Symptome(nomSymptome = i)
					s.save()
				m.symptomes.add(s)
			#mon_fichier.readline()
			

