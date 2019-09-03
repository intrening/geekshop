from django.urls import path

from products.views import (
    ProductList, ProductCreate, ProductUpdate, ProductDelete, ProductDetail,
)

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('add/', ProductCreate.as_view(), name='add'),
    path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('<int:pk>/update', ProductUpdate.as_view(), name='update'),
    path('<int:pk>/delete', ProductDelete.as_view(), name='delete'),
]
