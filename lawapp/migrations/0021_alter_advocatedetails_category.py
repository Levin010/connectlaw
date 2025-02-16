# Generated by Django 4.2.5 on 2024-03-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawapp', '0020_alter_case_case_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocatedetails',
            name='category',
            field=models.CharField(choices=[('general_practice', 'General Practice'), ('corporate_law', 'Corporate Law'), ('criminal_defense', 'Criminal Defense'), ('environmental_law', 'Environmental Law'), ('entertainment_law', 'Entertainment Law'), ('family_law', 'Family Law'), ('finance_law', 'Finance Law'), ('immigration_law', 'Immigration Law'), ('land_law', 'Land Law')], max_length=20),
        ),
    ]
