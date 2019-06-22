from django.urls import path

from products.views import *

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('add/', ProductCreate.as_view(), name='add'),
    path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('<int:pk>/update', ProductUpdate.as_view(), name='update'),
    path('<int:pk>/delete', ProductDelete.as_view(), name='delete'),

    # path('category/', CategoryList.as_view(), name='category_list'),
    # path('category/add/', CategoryCreate.as_view(), name='category_add'),
    # path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    # path('category/<int:pk>/update/', CategoryUpdate.as_view(), name='category_update'),
    # path('category/<int:pk>/delete/', CategoryDelete.as_view(), name='category_delete'),
]

