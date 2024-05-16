# Generated by Django 4.2.5 on 2024-03-15 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lawapp', '0016_alter_case_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('advocate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills_generated', to=settings.AUTH_USER_MODEL)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawapp.case')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
