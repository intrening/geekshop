from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('contact/', mainapp.contact, name='contact'),
    path('products/', include('products.urls', namespace='products')),
    path('category/', include('products.urls.category', namespace='category')),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
