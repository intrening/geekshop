from django.shortcuts import render, redirect, get_object_or_404
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

def product_add (request):
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

def product_update (request,pk):
	obj = get_object_or_404(Product, pk=pk)
	form = ProductForm (instance=obj)
	if request.POST:
		form = ProductForm(request.POST,instance=obj)
		if form.is_valid():
			form.save()
			return redirect (
				reverse('products:index')
			)
	return render (request, 'products/update.html', {
		'form': form
	})

def product_delele (request,pk):
	obj = get_object_or_404(Product, pk=pk)
	if request.method == 'POST':
		obj.delete()
		return redirect(
			reverse('products:index')
			)
	return render (request,
		'products/delete.html',{
			'object': obj 
		}
	)