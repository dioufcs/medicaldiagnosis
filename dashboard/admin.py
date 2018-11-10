from django.contrib import admin
from .models import *

admin.site.register(Medecin)
admin.site.register(Patient)
admin.site.register(Consultation)
admin.site.register(Antecedant)
admin.site.register(Symptome)
admin.site.register(Maladie)