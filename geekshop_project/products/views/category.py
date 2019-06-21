from django.shortcuts import render, redirect
from django.urls import reverse

from products.models import Product, ProductCategory
from products.forms import CategoryForm

def category_detail (request,pk):
    category = ProductCategory.objects.get(id=pk)
    return render(request, 'products/category_detail.html', {
        'category': category,
        })

def category_list (request):
    categories = ProductCategory.objects.all()
    return render (request, 'products/category_list.html', {
        'categories': categories
    })

def category_add (request):
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (
                reverse('products:category_list')
			)
    form = CategoryForm()
    return render (request, 'products/category_add.html', {
		'form': form
	})