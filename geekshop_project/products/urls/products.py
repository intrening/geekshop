from django.urls import path

from products.views import *

app_name = 'products'

urlpatterns = [
    path('', product_list, name='index'),
    path('<int:pk>/', product_detail, name='detail'),
    path('add/', addProduct, name='add'),

    path('category/', category_list, name='category_list'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('category/add/', category_add, name='category_add'),
]

