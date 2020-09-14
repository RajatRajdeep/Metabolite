from rest_framework import serializers
from .models import Document
import os

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = '__all__'

	def validate_document(self, value):
		root, ext = os.path.splitext(str(value))
		if ext!='.xlsx':
			raise serializers.ValidationError("File extension mst be .xlsx")
		return value