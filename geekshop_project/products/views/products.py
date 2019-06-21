from django.shortcuts import render, redirect
from django.urls import reverse

from products.models import Product, ProductCategory
from products.forms import ProductForm

def product_list(request):
	categories = ProductCategory.objects.all()

	if 'category' in request.GET:
		category = request.GET['category']
		products = Product.objects.filter(category=category)
		title = ProductCategory.objects.get(id = request.GET['category'])
	else:
		products = Product.objects.all()
		title = 'Все продукты'

	return render(request, 'products/index.html',{
		'products':products,
		'categories': categories,
		'title': title
		})

def product_detail (request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'products/detail.html', {
        'product':product})

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