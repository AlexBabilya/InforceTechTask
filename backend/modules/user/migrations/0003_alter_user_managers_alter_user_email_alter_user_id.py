# Generated by Django 4.2.3 on 2023-07-28 14:40

import django.contrib.auth.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("modules_user", "0002_alter_user_managers"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                default=uuid.uuid4,
                max_length=100,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
