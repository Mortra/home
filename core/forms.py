from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="User", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-input"}))


class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label="Фамилия")
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": 'form-control'}))
    email = forms.EmailField(label="Email", help_text="Введите существующий Email", widget=forms.EmailInput(attrs={"class": 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": 'form-control'}))
    password2 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "last_name", "email", "password1", "password2")



