# Generated by Django 4.1 on 2022-12-22 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phmsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='engine_alarm_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarm_datetime', models.DateTimeField(default=datetime.date(1900, 1, 1), verbose_name='alarm_time')),
                ('system', models.CharField(max_length=20, verbose_name='system')),
                ('alarm_class', models.IntegerField(verbose_name='alarm_class')),
                ('events', models.CharField(max_length=100, verbose_name='events')),
            ],
        ),
    ]