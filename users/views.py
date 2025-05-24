from django.shortcuts import render, redirect
from django.views.generic import DetailView

from users.forms import UserRegisterForm, UserForm
from users.models import User
import secrets
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from djangoProject1.settings import EMAIL_HOST_USER
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('catalog:product_list')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('catalog:product_list')


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()

        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет, перейди по ссылку для подтверждения почты: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )


def email_confirm(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
