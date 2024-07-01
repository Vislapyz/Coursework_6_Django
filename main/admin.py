from django.contrib import admin

# Register your models here.
from main.models import Client, Newsletter, Message, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Регистрации модели Клиента в админке."""

    list_display = ("name", "email", "owner")
    list_filter = ("name",)
    search_fields = ("email",)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    """Регистрации модели Рассылки в админке."""

    list_display = (
        "title",
        "author",
        "date_start",
        "data_send"
        "date_finish",
        "periodicity",
        "status",
        "is_active",
    )
    list_filter = ("title",)
    search_fields = ("title", "author")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Регистрации модели Сообщения в админке."""

    list_display = ("id", "subject", "body", "author")
    search_fields = ("subject", "author")


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    """Регистрации модели Лога в админке."""

    list_display = ("newsletter", "last_time_send", "status", "server_response")
    search_fields = ("newsletter",)
