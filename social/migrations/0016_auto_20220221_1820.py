# Generated by Django 3.2.11 on 2022-02-21 21:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0015_auto_20220221_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 21, 20, 16, 962698, tzinfo=utc), editable=False, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='edited',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 21, 20, 16, 962698, tzinfo=utc), verbose_name='Edited'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 21, 20, 16, 962698, tzinfo=utc), editable=False, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 21, 20, 16, 961696, tzinfo=utc), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='profiles/default.png', null=True, upload_to='profiles', verbose_name='Profile picture'),
        ),
    ]
