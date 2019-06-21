from django.urls import path

from products.views import *

app_name = 'products'

urlpatterns = [
    path('', product_list, name='index'),
    path('add/', product_add, name='add'),
    path('<int:pk>/', product_detail, name='detail'),
    path('<int:pk>/update', product_update, name='update'),
    path('<int:pk>/delete', product_delele, name='delete'),

    path('category/', category_list, name='category_list'),
    path('category/add/', category_add, name='category_add'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('category/<int:pk>/update/', category_update, name='category_update'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),
]

