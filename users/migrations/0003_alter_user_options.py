# Generated by Django 4.2.2 on 2024-06-30 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_country"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": [("set_is_active", "Может блокировать пользователя")],
                "verbose_name": "Пользоаптель",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
