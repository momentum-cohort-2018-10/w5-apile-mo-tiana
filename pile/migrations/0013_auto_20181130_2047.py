# Generated by Django 2.1.3 on 2018-11-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pile', '0012_auto_20181130_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]
