from django.shortcuts import render, redirect, get_object_or_404
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

def category_update(request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)
    if request.POST:
        form = CategoryForm(request.POST,instance=obj)
        if form.is_valid:
            form.save()
            return redirect(
                reverse('products:category_list')
            )
    form = CategoryForm(instance=obj)
    return render(
        request,'products/category_update.html',{
            'form': form
        }

    )
def category_delete (request, pk):
    obj = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(
                reverse('products:category_list')
            )
    return render(request,'products/category_delete.html',{
        'object': obj
    })