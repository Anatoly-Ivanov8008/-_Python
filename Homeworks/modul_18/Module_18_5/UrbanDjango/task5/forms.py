from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, label='Введите пароль:')
    repeat_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, label='Повторите пароль:')
    age = forms.CharField(max_length=3, label='Введите свой возраст:')
