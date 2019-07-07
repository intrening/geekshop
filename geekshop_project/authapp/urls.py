from django.urls import path

from .views import authLoginView, authLogoutView

app_name = 'authapp'

urlpatterns = [
    path('login/', authLoginView.as_view(), name='login'),
    path('logout/', authLogoutView.as_view(), name='logout')
]

