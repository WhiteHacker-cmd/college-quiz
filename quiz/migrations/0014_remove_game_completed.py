# Generated by Django 2.2 on 2020-11-22 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20201122_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='completed',
        ),
    ]
