# Generated by Django 4.2.3 on 2023-07-28 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modules_employee', '0001_initial'),
        ('modules_menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voted_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules_employee.employee')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules_menu.menu')),
            ],
        ),
    ]