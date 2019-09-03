from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView,
)

from products.models import ProductCategory
from products.forms import CategoryForm


class CategoryList(ListView):
    model = ProductCategory
    template_name = 'category/list.html'

class CategoryDetail(DetailView):
    model = ProductCategory
    template_name = 'category/detail.html'

class CategoryCreate(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = ProductCategory
    template_name = 'category/add.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')

    def test_func(self):
        user = self.request.user
        return user.has_perm('category.can_create')

class CategoryUpdate(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = ProductCategory
    template_name = 'category/update.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category:list')

    def test_func(self):
        user = self.request.user
        return user.has_perm('category.can_update')

class CategoryDelete(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = ProductCategory
    template_name = 'category/delete.html'
    success_url = reverse_lazy('category:list')

    def test_func(self):
        user = self.request.user
        return user.has_perm('category.can_delete')
