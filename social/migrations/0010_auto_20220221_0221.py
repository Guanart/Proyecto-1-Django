# Generated by Django 3.2.11 on 2022-02-21 05:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_auto_20220221_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 5, 21, 55, 933263, tzinfo=utc), editable=False, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='edited',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 5, 21, 55, 933263, tzinfo=utc), verbose_name='Edited'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 5, 21, 55, 932263, tzinfo=utc), editable=False, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='posts', verbose_name='Post picture'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 5, 21, 55, 931263, tzinfo=utc), verbose_name='Created'),
        ),
    ]
