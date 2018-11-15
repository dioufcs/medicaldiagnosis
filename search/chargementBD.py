from dashboard.models import *

def fillBD():
	with open('search/medicaldata.txt', 'r') as mon_fichier:
		#while mon_fichier.read(1):
		while mon_fichier.readline():
			ligne_maladie = mon_fichier.readline().strip('\n')
			ligne_description = mon_fichier.readline().strip('\n')
			m = Maladie(nomMaladie = ligne_maladie, description = ligne_description)
			m.save()
			ligne_symptomes = mon_fichier.readline().strip('\n')
			ligne_s = ligne_symptomes.split(',')
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
			

