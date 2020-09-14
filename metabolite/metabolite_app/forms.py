from django import forms
from .models import Document

# Document form
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)