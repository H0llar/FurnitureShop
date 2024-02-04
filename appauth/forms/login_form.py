from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'account__login--input',
        'placeholder': 'Введите логин'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'account__login--input',
        'placeholder': 'Введите пароль'}))
