# Generated by Django 4.2.5 on 2024-03-03 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lawapp', '0011_updates_advocate_updates_case_updates_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='updates',
            name='client',
        ),
    ]
