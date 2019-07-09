from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator

from products.models import Product, ProductCategory
from products.forms import CategoryForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
	CreateView, UpdateView, DeleteView, ListView, DetailView
)
from django.core.serializers import serialize
from django.http import JsonResponse
import json

class RestCategoryListView(ListView):
    model = ProductCategory
    def get_context_data(self, **kwargs):
        context = super(RestCategoryListView, self).get_context_data(**kwargs)
        object_list = context.get('object_list')

        return {
            'results':json.loads(serialize('json', object_list, fields=('name')))
        }

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
        #  super().render_to_response(context, **response_kwargs)


class CategoryList (ListView):
    model = ProductCategory
    template_name = 'category/list.html'    

class CategoryDetail (DetailView):
    model = ProductCategory
    template_name = 'category/detail.html'
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super (CategoryDetail, self).get_context_data(**kwargs)
        category = context.get('object')
        paginator = Paginator (category.product_set.all().prefetch_related(), self.paginate_by)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        return context


class CategoryCreate (UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = ProductCategory
    template_name = 'category/add.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')

class CategoryUpdate (UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = ProductCategory
    template_name = 'category/update.html'
    fields = ['name','description']
    success_url = reverse_lazy('category:list')

class CategoryDelete (UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = ProductCategory
    template_name = 'category/delete.html'
    success_url = reverse_lazy('category:list')

    def test_func(self):
        user = self.request.user
        user.has_perm('products.can_delete')
        return super().test_func()


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