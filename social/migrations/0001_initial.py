# Generated by Django 3.2.11 on 2022-02-20 05:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, height_field=320, null=True, upload_to='profiles', verbose_name='Profile picture', width_field=320)),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 2, 20, 5, 22, 13, 283560, tzinfo=utc), verbose_name='Created')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('picture', models.ImageField(blank=True, height_field=320, null=True, upload_to='posts', verbose_name='Post picture', width_field=320)),
                ('content', models.TextField(verbose_name='Content')),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 2, 20, 5, 22, 13, 285531, tzinfo=utc), editable=False, verbose_name='Created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 2, 20, 5, 22, 13, 286775, tzinfo=utc), editable=False, verbose_name='Created')),
                ('edited', models.DateTimeField(default=datetime.datetime(2022, 2, 20, 5, 22, 13, 286775, tzinfo=utc), verbose_name='Edited')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
            },
        ),
    ]
