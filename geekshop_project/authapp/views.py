from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth.views import (
    LoginView, LogoutView
)

class authLoginView(LoginView):
    template_name = 'authapp/login.html'

class authLogoutView(LogoutView):
    template_name = 'authapp/logout.html'
    


# Create your views here.

def login_view(request):
    form = LoginForm()
    success_url = reverse('authapp:login')
    if request.method == 'POST':
        form = LoginForm (data=request.POST)
        if form.is_valid:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                username=username,
                password=password
            )
            if user and user.is_active:
                login(request, user)
                return redirect (success_url)
    return render(
        request, 'authapp/login.html', {
            'form': form
        }
    )