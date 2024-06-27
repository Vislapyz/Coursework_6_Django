from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import EmailField
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель для пользователя"""
    username = None

    avatar = models.ImageField(
        upload_to='users_avatar',
        verbose_name='Аватар пользователя',
        help_text='Загрузите изображение',
        **NULLABLE
    )
    phone_number = PhoneNumberField(
        verbose_name='Номер телефона',
        help_text='Введите номер телефона в формате +71234567890',
        blank=True,
        null=True,
        **NULLABLE
    )
    country = models.CharField(
        verbose_name='Страна',
        help_text='Выберите страну',
        max_length=100,
        **NULLABLE
    )
    email: EmailField = models.EmailField(
        verbose_name='email',
        help_text='Введите адрес электронной почты',
        unique=True,
    )
    token = models.CharField(
        max_length=50,
        verbose_name='Токен',
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
