# Generated by Django 4.2.2 on 2024-06-30 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="newsletter",
            old_name="date_next",
            new_name="date_send",
        ),
    ]
