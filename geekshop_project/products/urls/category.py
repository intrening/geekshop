from django.urls import path

from products.views import (
    CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete, CategoryDetail
)

app_name = 'category'

urlpatterns = [
    path('', CategoryList.as_view(), name='list'),
    path('add/', CategoryCreate.as_view(), name='add'),
    path('<int:pk>/', CategoryDetail.as_view(), name='detail'),
    path('<int:pk>/update/', CategoryUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CategoryDelete.as_view(), name='delete'),
]

# rest_urlpatterns = [
#     path('api/list/', RestCategoryListView.as_view(), name='rest_list')
# ]

# urlpatterns += rest_urlpatterns
