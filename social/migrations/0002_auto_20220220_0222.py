# Generated by Django 3.2.11 on 2022-02-20 05:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 5, 22, 43, 685198, tzinfo=utc), editable=False, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='edited',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 5, 22, 43, 685198, tzinfo=utc), verbose_name='Edited'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 5, 22, 43, 684193, tzinfo=utc), editable=False, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 5, 22, 43, 684193, tzinfo=utc), verbose_name='Created'),
        ),
    ]
