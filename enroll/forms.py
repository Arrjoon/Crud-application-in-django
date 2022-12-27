import email
from unicodedata import name
from django.core import validators
from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


class loginForm(forms.Form):
    name = forms.CharField(max_length=23)
    email = forms.EmailField()


widgets = {
    'name': forms.TextInput(attrs={'class': "form-control"}),
    'email': forms.EmailInput(attrs={'class': 'form-control'}),
    'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
}
