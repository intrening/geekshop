from django.urls import path

from .views import authLoginView, authLogoutView, authRegistrationView

app_name = 'authapp'

urlpatterns = [
    path('login/', authLoginView.as_view(), name='login'),
    path('logout/', authLogoutView.as_view(), name='logout'),
    path('registration/', authRegistrationView.as_view(), name='registration')
]

