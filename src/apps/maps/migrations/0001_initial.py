# Generated by Django 4.1.5 on 2023-03-08 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=255, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
        migrations.CreateModel(
            name='TransportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Вид транспорта')),
            ],
        ),
        migrations.CreateModel(
            name='TravelTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.SmallIntegerField(default=10, verbose_name='Время в пути')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='maps.map', verbose_name='Карта')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='maps.transporttype', verbose_name='Вид транспорта')),
                ('travel_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='maps.traveltime', verbose_name='Время в пути')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Выбор',
                'verbose_name_plural': 'Выборы',
            },
        ),
    ]