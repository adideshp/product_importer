from django import forms
from .models import Document, Product

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', )


class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ('sku', 'name', 'description', 'status')
