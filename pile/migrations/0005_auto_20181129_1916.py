# Generated by Django 2.1.3 on 2018-11-29 19:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pile', '0004_auto_20181129_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='favorited_users',
            field=models.ManyToManyField(related_name='favorite_posts', through='pile.Favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
