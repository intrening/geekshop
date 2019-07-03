from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.urls import reverse
from .forms import LoginForm

# Create your views here.

def login_view(request):
    form = LoginForm()
    success_url = reverse('mainapp:index')
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