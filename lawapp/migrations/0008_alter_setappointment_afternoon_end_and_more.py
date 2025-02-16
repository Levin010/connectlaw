# Generated by Django 4.2.5 on 2024-02-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawapp', '0007_alter_setappointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setappointment',
            name='afternoon_end',
            field=models.CharField(blank=True, choices=[('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00')], default='16:00', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='setappointment',
            name='afternoon_start',
            field=models.CharField(blank=True, choices=[('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00')], default='12:00', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='setappointment',
            name='appointment_duration',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(15, '15 minutes'), (30, '30 minutes'), (45, '45 minutes'), (60, '1 hour')], default=15, null=True),
        ),
        migrations.AlterField(
            model_name='setappointment',
            name='evening_end',
            field=models.CharField(blank=True, choices=[('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'), ('21', '21:00'), ('22', '22:00')], default='22:00', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='setappointment',
            name='evening_start',
            field=models.CharField(blank=True, choices=[('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'), ('21', '21:00'), ('22', '22:00')], default='16:00', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='setappointment',
            name='morning_end',
            field=models.CharField(blank=True, choices=[('6', '06:00'), ('7', '07:00'), ('8', '08:00'), ('9', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00')], default='12:00', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='setappointment',
            name='morning_start',
            field=models.CharField(blank=True, choices=[('6', '06:00'), ('7', '07:00'), ('8', '08:00'), ('9', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00')], default='06:00', max_length=5, null=True),
        ),
    ]
