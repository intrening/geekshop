from django.shortcuts import render, redirect
import json
from products.models import Product, ProductCategory
from .forms import ProductForm
from django.urls import reverse
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    categorys = ProductCategory.objects.all()
    return render(request, 'products/index.html', {
        'products':products,
        'categorys': categorys,
        'title': 'Все продукты'
        })

def product_detail (request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'products/detail.html', {
        'product':product})


def category_detail (request,pk):
    #products = Product.objects.all()
    #categorys = ProductCategory.objects.all()
    category = ProductCategory.objects.get(id=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'products/index.html', {
        'products':products,
        'categorys': [category],
        'title': category.name
        })


def addProduct(request):
	if request.POST:
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect (
				reverse('products:index')
			)
	form = ProductForm()
	return render (request, 'products/add.html', {
		'form': form
	})