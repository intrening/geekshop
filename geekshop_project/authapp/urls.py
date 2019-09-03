from django.urls import path

from .views import AuthLoginView, AuthLogoutView, AuthRegistrationView

app_name = 'authapp'

urlpatterns = [
    path('login/', AuthLoginView.as_view(), name='login'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('registration/', AuthRegistrationView.as_view(), name='registration')
]
