from django.forms import ModelForm, BooleanField

from main.models import Newsletter, Message, Client


class StyleFormMixin:
    """Стилизация форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class NewsletterForm(StyleFormMixin, ModelForm):
    """Форма для модели Newsletter"""

    class Meta:
        model = Newsletter
        exclude = ("next_date", "is_active")


class MessageForm(StyleFormMixin, ModelForm):
    """Форма для модели Message"""

    class Meta:
        model = Message
        fields = ("subject", "body", "author")


class ClientForm(StyleFormMixin, ModelForm):
    """Форма для модели Client"""

    class Meta:
        model = Client
        fields = ("email", "name", "owner")
