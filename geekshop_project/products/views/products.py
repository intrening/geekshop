from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from products.models import Product, ProductCategory
from products.forms import ProductForm

from django.views.generic import (
	CreateView, UpdateView, DeleteView, ListView, DetailView
)

class ProductList (ListView):
	model = Product
	template_name = 'products/index.html'

class ProductDetail (DetailView):
	model = Product
	template_name = 'products/detail.html'

class ProductDelete (DeleteView):
	model = Product
	template_name = 'products/delete.html'
	success_url = reverse_lazy('products:index')

class ProductCreate (CreateView):
    model = Product
    template_name = 'products/add.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:index')

class ProductUpdate (UpdateView):
    model = Product
    template_name = 'products/update.html'
    fields = ['name','category','description','image','price','quantity']
    success_url = reverse_lazy('products:index')

# def product_list(request):
# 	categories = ProductCategory.objects.all()

# 	if 'category' in request.GET:
# 		category = request.GET['category']
# 		products = Product.objects.filter(category=category)
# 		title = ProductCategory.objects.get(id = request.GET['category'])
# 	else:
# 		products = Product.objects.all()
# 		title = 'Все продукты'

# 	return render(request, 'products/index.html',{
# 		'products':products,
# 		'categories': categories,
# 		'title': title
# 		})

# def product_detail (request,pk):
#     product = Product.objects.get(id=pk)
#     return render(request, 'products/detail.html', {
#         'product':product})

# def product_add (request):
# 	if request.POST:
# 		form = ProductForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect (
# 				reverse('products:index')
# 			)
# 	form = ProductForm()
# 	return render (request, 'products/add.html', {
# 		'form': form
# 	})

# def product_update (request,pk):
# 	obj = get_object_or_404(Product, pk=pk)
# 	form = ProductForm (instance=obj)
# 	if request.POST:
# 		form = ProductForm(request.POST,instance=obj)
# 		if form.is_valid():
# 			form.save()
# 			return redirect (
# 				reverse('products:index')
# 			)
# 	return render (request, 'products/update.html', {
# 		'form': form
# 	})

# def product_delele (request,pk):
# 	obj = get_object_or_404(Product, pk=pk)
# 	if request.method == 'POST':
# 		obj.delete()
# 		return redirect(
# 			reverse('products:index')
# 			)
# 	return render (request,
# 		'products/delete.html',{
# 			'object': obj 
# 		}
# 	)