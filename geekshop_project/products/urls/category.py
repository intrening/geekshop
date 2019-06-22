from django.urls import path

from products.views import *

app_name = 'category'

urlpatterns = [
    # path('', ProductList.as_view(), name='index'),
    # path('add/', ProductCreate.as_view(), name='add'),
    # path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    # path('<int:pk>/update', ProductUpdate.as_view(), name='update'),
    # path('<int:pk>/delete', ProductDelete.as_view(), name='delete'),

    path('', CategoryList.as_view(), name='list'),
    path('add/', CategoryCreate.as_view(), name='add'),
    path('<int:pk>/', CategoryDetail.as_view(), name='detail'),
    path('<int:pk>/update/', CategoryUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CategoryDelete.as_view(), name='delete'),
]

