# Generated by Django 3.2.2 on 2021-09-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='city',
            field=models.CharField(choices=[('Default', 'Default'), ('Świdnica', 'Swidnica'), ('Wrocław', 'Wroclaw')], default='Default', max_length=40),
        ),
    ]
