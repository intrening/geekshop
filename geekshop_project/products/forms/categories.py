from django import forms
from products.models import ProductCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name','description']
        widgets = {
            'name': forms.widgets.TextInput(attrs={
                'class':'name-field',
                'placeholder': 'имя категории'
                }),
            'description':forms.widgets.TextInput(attrs={
                'class':'name-field',
                'placeholder ': 'Описание категории'
                })
        }
        