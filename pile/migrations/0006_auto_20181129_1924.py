# Generated by Django 2.1.3 on 2018-11-29 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pile', '0005_auto_20181129_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='favorited_users',
            new_name='favorite_posts',
        ),
    ]
