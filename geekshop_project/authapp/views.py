from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.views import (
    LoginView, LogoutView, FormView
)

from .forms import (
    LoginForm, RegistrationForm
)

class AuthLoginView(LoginView):
    template_name = 'authapp/login.html'

class AuthLogoutView(LogoutView):
    template_name = 'authapp/logout.html'

class AuthRegistrationView(FormView):
    template_name = 'authapp/registration.html'
    form_class = RegistrationForm

def login_view(request):
    form = LoginForm()
    success_url = reverse('authapp:login')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                username=username,
                password=password
            )
            if user and user.is_active:
                login(request, user)
                return redirect(success_url)
    return render(
        request, 'authapp/login.html', {
            'form': form
        }
    )
