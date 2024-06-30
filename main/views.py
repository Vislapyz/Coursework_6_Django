# from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.forms import NewsletterForm, MessageForm, ClientForm
from main.models import Newsletter, Message, Client


class NewsletterListView(ListView):
    """Отображения всех рассылок"""

    model = Newsletter


class NewsletterDetailView(DetailView):
    """Вывода страницы с одной рассылкой по pk"""

    model = Newsletter


class NewsletterCreateView(CreateView):
    """Создания новой рассылки"""

    model = Newsletter
    form_class = NewsletterForm

    success_url = reverse_lazy("main:newsletter_list")

    # def form_valid(self, form):
    #     """Метод для автоматического привязывания Пользователя к создаваемой Рассылке"""
    #     # Сохранение формы
    #     self.object = form.save()
    #     self.object.author = self.request.user
    #     self.object.save()
    #
    #     return super().form_valid(form)


class NewsletterUpdateView(UpdateView):
    """Редактирования рассылки"""

    model = Newsletter
    form_class = NewsletterForm

    def get_success_url(self):
        """Метод для определения пути, куда будет совершен переход после редактирования рассылки"""
        return reverse("main:newsletter_detail", args=[self.get_object().pk])


class NewsletterDeleteView(DeleteView):
    """Удаления рассылки"""

    model = Newsletter
    success_url = reverse_lazy("main:newsletter_list")


class MessageListView(ListView):
    """Отображения всех созданных сообщений"""

    model = Message


class MessageDetailView(DetailView):
    """Вывода страницы с одним сообщением по pk"""

    model = Message


class MessageCreateView(CreateView):
    """Создания нового сообщения"""

    model = Message
    form_class = MessageForm

    success_url = reverse_lazy("main:message_list")


class MessageUpdateView(UpdateView):
    """Редактирования сообщения"""

    model = Message
    form_class = MessageForm

    def get_success_url(self):
        """Метод куда будет совершен переход после редактирования сообщения"""
        return reverse("main:message_detail", args=[self.get_object().pk])


class MessageDeleteView(DeleteView):
    """Удаления сообщения"""

    model = Message
    success_url = reverse_lazy("main:message_list")


class ClientListView(ListView):
    """Отображения всех созданных Клиентов"""

    model = Client


class ClientDetailView(DetailView):
    """Вывода страницы с одним Клиентом по pk"""

    model = Client


class ClientCreateView(CreateView):
    """Создания нового Клиент"""

    model = Client
    form_class = ClientForm

    success_url = reverse_lazy("main:client_list")


class ClientUpdateView(UpdateView):
    """Редактирования Клиента"""

    model = Client
    form_class = ClientForm

    def get_success_url(self):
        """Метод куда будет совершен переход после редактирования сообщения"""
        return reverse("main:client_detail", args=[self.get_object().pk])


class ClientDeleteView(DeleteView):
    """Удаления Клиента"""

    model = Client
    success_url = reverse_lazy("main:client_list")
