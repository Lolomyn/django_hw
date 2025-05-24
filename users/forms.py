from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'country', 'phone', 'avatar']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude = []

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите e-mail'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })

        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите номер телефона'
        })

        self.fields['country'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите страну'
        })
