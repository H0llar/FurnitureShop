from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'account__login--input',
        'placeholder': 'Введите логин'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'account__login--input',
        'placeholder': 'Введите пароль'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'account__login--input',
        'placeholder': 'Повторите пароль'}))
