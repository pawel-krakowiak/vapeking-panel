# Generated by Django 3.2.2 on 2021-09-28 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('store', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
        migrations.CreateModel(
            name='StorageStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.storage')),
            ],
        ),
    ]
