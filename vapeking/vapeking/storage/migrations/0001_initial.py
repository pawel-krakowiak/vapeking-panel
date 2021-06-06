# Generated by Django 3.2.2 on 2021-05-31 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0002_auto_20210529_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.store')),
                ('store', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
    ]