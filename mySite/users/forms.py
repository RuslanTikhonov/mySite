from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Введите Email",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    username = forms.CharField(
        label="Введите логин",
        required=True,
        help_text="Нельзя вводить символы",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Введите пароль",
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    password2 = forms.CharField(
        label="Подтвердите пароль",
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]