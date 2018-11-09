from django.test import TestCase, TransactionTestCase
from .models import *


class MaladieTestCase(TestCase):

	def setUp(self):
		maladie = Maladie (nomMaladie = "paludisme", description = "exemple maladie")
		maladie.save()
