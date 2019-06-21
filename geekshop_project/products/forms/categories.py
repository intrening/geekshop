from django import forms
from products.models import ProductCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name','description']
        