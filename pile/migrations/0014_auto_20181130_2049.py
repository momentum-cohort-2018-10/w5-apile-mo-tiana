# Generated by Django 2.1.3 on 2018-11-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pile', '0013_auto_20181130_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
