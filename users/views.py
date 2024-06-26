import secrets
from django.conf import settings
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserForm, UserPasswordChangeForm, UserRegisterForm
from users.models import User


class UserRegisterView(CreateView):
    """Класс для создания нового Пользователя"""

    model = User
    form_class = UserRegisterForm

    def get_success_url(self):
        """Метод для определения пути, после создания Пользователя"""
        return reverse("users:login")

    def form_valid(self, form):
        """Метод верифекации email"""
        token = secrets.token_hex(16)
        user = form.save()
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        link = f"http://{host}/users/confirm-register/{token}"
        message = f"Вы успешно зарегистрировались на сайте 'Здоровье в ложке'. Предлагаем Вам подтвердить почту {link}"
        send_mail("Верификация почты", message, settings.EMAIL_HOST_USER, [user.email])
        return super().form_valid(form)


def confirm_email(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserUpdateView(UpdateView):
    """Редактирования профиля Пользователя"""

    model = User
    success_url = reverse_lazy("users:profile")
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):

    form_class = UserPasswordChangeForm
    template_name = "users/password_change_form.html"
    success_url = reverse_lazy("users:password-change-done")
