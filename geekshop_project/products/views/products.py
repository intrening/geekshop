from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
from products.models import Product
from products.forms import ProductForm


class ProductList(ListView):
    template_name = 'product/list.html'
    model = Product
    paginate_by = 3

class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'

class ProductDelete(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('product:list')

    def test_func(self):
        user = self.request.user
        return user.has_perm('product.can_delete')

class ProductCreate(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product/add.html'
    form_class = ProductForm
    success_url = reverse_lazy('product:list')

    def test_func(self):
        user = self.request.user
        return user.has_perm('product.can_create')

class ProductUpdate(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update.html'
    fields = ['name', 'category', 'description', 'image', 'price', 'quantity']
    success_url = reverse_lazy('product:list')

    def test_func(self):
        user = self.request.user
        return user.has_perm('product.can_update')
