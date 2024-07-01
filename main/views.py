from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from main.forms import NewsletterForm, MessageForm, ClientForm
from main.models import Client, Log, Message, Newsletter
from blog.models import Blog


class NewsletterListView(ListView):
    """Отображения всех рассылок"""

    model = Newsletter


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    """Вывода страницы с одной рассылкой по pk"""

    model = Newsletter


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    """Создания новой рассылки"""

    model = Newsletter
    form_class = NewsletterForm

    success_url = reverse_lazy("main:newsletter_list")

    def form_valid(self, form):
        """Автоматического привязывания Пользователя к создаваемой Рассылке"""
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирования рассылки"""

    model = Newsletter
    form_class = NewsletterForm

    def get_success_url(self):
        """Куда будет совершен переход после редактирования рассылки"""
        return reverse("main:newsletter_detail", args=[self.get_object().pk])

    def get_form_class(self):
        """Выводит правильную форму редактирования"""
        user = self.request.user
        if user == self.object.author or self.request.user.is_superuser:
            return NewsletterForm

        raise PermissionDenied("Вы не можете редактировать эту рассылку.")


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    """Удаления рассылки"""

    model = Newsletter
    success_url = reverse_lazy("main:newsletter_list")


class MessageListView(ListView):
    """Отображения всех созданных сообщений"""

    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    """Вывода страницы с одним сообщением по pk"""

    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Создания нового сообщения"""

    model = Message
    form_class = MessageForm

    success_url = reverse_lazy("main:message_list")

    def form_valid(self, form):
        """Автоматического привязывания Пользователя к создаваемому Сообщению"""
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирования сообщения"""

    model = Message
    form_class = MessageForm

    def get_success_url(self):
        """Куда будет совершен переход после редактирования рассылки"""
        return reverse("main:message_detail", args=[self.get_object().pk])


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Удаления сообщения"""

    model = Message
    success_url = reverse_lazy("main:message_list")


class ClientListView(ListView):
    """Отображения всех созданных Клиентов"""

    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    """Вывода страницы с одним Клиентом по pk"""

    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Создания нового Клиент"""

    model = Client
    form_class = ClientForm

    success_url = reverse_lazy("main:client_list")

    def form_valid(self, form):
        """Автоматического привязывания Пользователя к создаваемому Клиенту"""
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирования Клиента"""

    model = Client
    form_class = ClientForm

    def get_success_url(self):
        """Куда будет совершен переход после редактирования рассылки"""
        return reverse("main:client_detail", args=[self.get_object().pk])


class ClientDeleteView(DeleteView):
    """Удаления Клиента"""

    model = Client
    success_url = reverse_lazy("main:client_list")


class IndexView(TemplateView):
    """Отображение статистики по сайту"""
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        """Отображение статистики на Главной странице"""

        context = super().get_context_data(**kwargs)
        article_list = Blog.object.all()[:3]
        context['article_list'] = article_list
        newsletter_count = Newsletter.objects.all().count()
        context["newsletter_count"] = newsletter_count

        unique_clients_count = Client.objects.all().values("email").distinct().count()
        context["unique_clients_count"] = unique_clients_count

        active_newsletter_count = Newsletter.objects.filter(is_active=True).count()
        context["active_newsletter_count"] = active_newsletter_count
        return context


class LogListView(ListView):
    """Отображения всех созданных Логов."""

    model = Log

    def get_queryset(self, *args, **kwargs):
        """Вывода листа с Логами только для Автора рассылок"""
        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = super().get_queryset(*args, **kwargs)
        else:
            queryset = super().get_queryset().filter(owner=user)
        return queryset


def toggle_activity(request, pk):
    """
    Функция для Модератора по смене активности рассылки.
    """
    newsletter_status = get_object_or_404(Newsletter, pk=pk)
    if newsletter_status.is_active is True:
        newsletter_status.is_active = False

    elif newsletter_status.is_active is False:
        newsletter_status.is_active = True

    newsletter_status.save()
    return redirect(reverse("main:newsletter_list"))
