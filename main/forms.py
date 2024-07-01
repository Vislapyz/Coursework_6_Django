from django.forms import ModelForm, BooleanField, DateTimeInput

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
        exclude = ("datatime_send", "author")

        widgets = {
            "datetime_start": DateTimeInput(
                attrs={"placeholder": "ДД.ММ.ГГГГ ЧЧ:ММ:СС", "type": "datetime-local"}
            ),
            "datetime_finish": DateTimeInput(
                attrs={"placeholder": "ДД.ММ.ГГГГ ЧЧ:ММ:СС", "type": "datetime-local"}
            ),
        }


class MessageForm(StyleFormMixin, ModelForm):
    """Форма для модели Message"""

    class Meta:
        model = Message
        fields = ("subject", "body")


class ClientForm(StyleFormMixin, ModelForm):
    """Форма для модели Client"""

    class Meta:
        model = Client
        fields = ("email", "name")
