import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail

from main.models import Log, Newsletter


def change_newsletter_status(newsletter, current_datetime) -> None:
    """Функция меняющая статус подписки."""
    if newsletter.status == "created":
        newsletter.status = "launched"
        print(f"{newsletter.title} launched")
    elif newsletter.status == "launched":
        print(f"{newsletter.title}launched")
    elif (
            newsletter.status == "launched"
            and newsletter.datetime_finish <= current_datetime
    ):
        newsletter.status = "completed"
        newsletter.is_active = False
        print(f"{newsletter.title}completed")
    newsletter.save()


def get_date_send(newsletter, current_datetime):
    """
    Корректировки даты и времени для следующей отправки рассылки (datetime_send).
    """
    if newsletter.datetime_send < current_datetime:
        if newsletter.periodicity == "daily":
            newsletter.datetime_send += timedelta(days=1, hours=0, minutes=0)
        elif newsletter.periodicity == "weekly":
            newsletter.datetime_send += timedelta(days=7, hours=0, minutes=0)
        elif newsletter.periodicity == "monthly":
            newsletter.datetime_send += timedelta(days=30, hours=0, minutes=0)
        newsletter.save()


def send_mail_by_time():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    newsletter_list = Newsletter.objects.all().filter(is_active=True)
    if newsletter_list:
        for newsletter in newsletter_list:
            change_newsletter_status(newsletter, current_datetime)
            if (
                    newsletter.datetime_send
                    <= current_datetime
                    <= newsletter.datetime_finish
            ):
                emails_list = [client.email for client in newsletter.clients.all()]

                try:
                    server_response = send_mail(
                        subject=newsletter.message.subject,
                        message=newsletter.message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=emails_list,
                        fail_silently=False,
                    )
                    print("Письмо отправлено")
                    status = "Отправлено"
                    log = Log(
                        newsletter=newsletter,
                        status=status,
                        server_response=server_response,
                        owner=newsletter.author
                    )
                    log.save()
                    print("log сохранен")
                    get_date_send(newsletter, current_datetime)

                except smtplib.SMTPException as error:
                    status = "Не отправлено"
                    server_response = f"Ошибка отправки {error}"
                    log = Log(
                        newsletter=newsletter,
                        status=status,
                        server_response=server_response,
                        owner=newsletter.author
                    )
                    log.save()
                    print("Лог с ошибкой отправки", error)

    else:
        print("Нет newsletter_list")
