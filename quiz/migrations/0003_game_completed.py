# Generated by Django 2.2 on 2020-11-10 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20201109_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
