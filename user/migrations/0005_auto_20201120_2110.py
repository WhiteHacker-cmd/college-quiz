# Generated by Django 2.2 on 2020-11-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_player_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='is_online',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
