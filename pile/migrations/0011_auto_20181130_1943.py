# Generated by Django 2.1.3 on 2018-11-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pile', '0010_auto_20181130_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(null=True, unique=True),
        ),
    ]
