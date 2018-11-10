from django_elasticsearch_dsl import DocType, Index
from .models import MedicalData

medicaldata = Index('medicaldata')

@medicaldata.doc_type
class MedicalDataDocument(DocType):
	class Meta:
		model  = MedicalData

		fields = [
            'id',
            'nomMaladie',
            'listeSymptomes',
        ]
		