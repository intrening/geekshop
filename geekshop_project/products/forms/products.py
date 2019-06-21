from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','image','short_desc','description','price','quantity']
        widgets = {
            'name':forms.widgets.Select(attrs={
               'placeholder ': 'Категория'
               }),
           'name':forms.widgets.TextInput(attrs={
               'class':'name-field',
               'placeholder ': 'Имя продукта'
               }),
            'short_desc':forms.widgets.TextInput(attrs={
               'class':'name-field',
               'placeholder ': 'Короткое описание'
               }),
            'description':forms.widgets.Textarea(attrs={
               'class':'name-field',
               'placeholder ': 'Полное описание'
               }),
            'price':forms.widgets.NumberInput(attrs={
               'class':'name-field',
               'placeholder ': 'Цена'
               }),
            'quantity':forms.widgets.NumberInput(attrs={
               'class':'name-field',
               'placeholder ': 'Количество'
               }),
        }