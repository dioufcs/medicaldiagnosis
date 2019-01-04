from django_elasticsearch_dsl import DocType, Index, fields
from elasticsearch_dsl import analyzer, tokenizer
from .models import MedicalData
from dashboard.models import Symptome

medicaldata = Index('medicaldata')
symptomes = Index('symptomes')
symptomes2 = Index('symptomes')

symptomes.settings(
    number_of_shards=1,
    number_of_replicas=0
)

my_analyzer = analyzer (
	'my_analyzer',
	type = "custom",
	tokenizer = "standard",
	filter = [ "asciifolding",
            "lowercase",
            "shingle"
            ]
	)

html_strip = analyzer(
    'html_strip',
    tokenizer="custom",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@medicaldata.doc_type
class MedicalDataDocument(DocType):
	class Meta:
		model  = MedicalData

		fields = [
            'id',
            'nomMaladie',
            'description',
            'listeSymptomes',
        ]

@symptomes.doc_type
class SymptomeDocument (DocType):
	
	class Meta:
		model = Symptome

		fields = [
			'id',
			'nomSymptome'
		]
