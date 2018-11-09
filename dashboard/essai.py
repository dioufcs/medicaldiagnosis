from .models import *

def nokho():
	s1 = Symptome (nomSymptome = "maux de tete")
	s1.save()

	s2 = Symptome (nomSymptome = "courbatures")
	s2.save()

	s3 = Symptome (nomSymptome = "maux de ventre")
	s3.save()

	m = Maladie (nomMaladie = "paludisme", description = "exemple maladie")
	m.save()

	m.symptomes.add(s1,s2, s3)