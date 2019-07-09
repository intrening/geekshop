from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=128, required=True
    )
    password = forms.CharField(
        max_length=72, required=True,
        widget=forms.widgets.PasswordInput()
    )

class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField (
        max_length=72,
        required=True,
        widget=forms.widgets.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            'password': forms.widgets.PasswordInput(),
        }
