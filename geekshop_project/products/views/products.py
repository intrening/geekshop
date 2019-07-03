from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator

from products.models import Product, ProductCategory
from products.forms import ProductForm

from django.views.generic import (
	CreateView, UpdateView, DeleteView, ListView, DetailView
)

class ProductList (ListView):
	template_name = 'product/list.html'
	model = Product
	paginate_by = 2
		# def get_context_data(self, **kwargs):
	# 	context = super (ProductList, self).get_context_data(**kwargs)
	# 	paginator = Paginator (context.get('object_list'), 1)
	# 	page_number = self.request.GET.get('page')
	# 	context['page'] = paginator.get_page(page_number)
	# 	return context
		

class ProductDetail (DetailView):
	model = Product
	template_name = 'product/detail.html'
	

class ProductDelete (DeleteView):
	model = Product
	template_name = 'product/delete.html'
	success_url = reverse_lazy('product:list')

class ProductCreate (CreateView):
	model = Product
	template_name = 'product/add.html'
	form_class = ProductForm
	success_url = reverse_lazy('product:list')

class ProductUpdate (UpdateView):
	model = Product
	template_name = 'product/update.html'
	fields = ['name','category','description','image','price','quantity']
	success_url = reverse_lazy('product:list')

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