from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from products.models import Product, ProductCategory
from products.forms import CategoryForm

from django.views.generic import (
	CreateView, UpdateView, DeleteView, ListView, DetailView
)

class CategoryList (ListView):
    model = ProductCategory
    template_name = 'products/category_list.html'

class CategoryDetail (DetailView):
    model = ProductCategory
    template_name = 'products/category_detail.html'


class CategoryCreate (CreateView):
    model = ProductCategory
    template_name = 'products/category_add.html'
    form_class = CategoryForm
    success_url = reverse_lazy('products:category_list')

class CategoryUpdate (UpdateView):
    model = ProductCategory
    template_name = 'products/category_update.html'
    fields = ['name','description']
    success_url = reverse_lazy('products:category_list')

class CategoryDelete (DeleteView):
    model = ProductCategory
    template_name = 'products/category_delete.html'
    success_url = reverse_lazy('products:category_list')


# def category_add (request):
#     if request.POST:
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect (
#                 reverse('products:category_list')
# 			)
#     form = CategoryForm()
#     return render (request, 'products/category_add.html', {
# 		'form': form
# 	})
    
# def category_detail (request,pk):
#     category = ProductCategory.objects.get(id=pk)
#     return render(request, 'products/category_detail.html', {
#         'category': category,
#         })

# def category_list (request):
#     categories = ProductCategory.objects.all()
#     return render (request, 'products/category_list.html', {
#         'categories': categories
#     })

# def category_update(request, pk):
#     obj = get_object_or_404(ProductCategory, pk=pk)
#     if request.POST:
#         form = CategoryForm(request.POST,instance=obj)
#         if form.is_valid:
#             form.save()
#             return redirect(
#                 reverse('products:category_list')
#             )
#     form = CategoryForm(instance=obj)
#     return render(
#         request,'products/category_update.html',{
#             'form': form
#         }

#     )
# def category_delete (request, pk):
#     obj = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect(
#                 reverse('products:category_list')
#             )
#     return render(request,'products/category_delete.html',{
#         'object': obj
#     })