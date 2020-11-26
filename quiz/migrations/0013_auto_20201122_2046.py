# Generated by Django 2.2 on 2020-11-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20201122_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_status',
            field=models.CharField(blank=True, choices=[('C', 'created'), ('S', 'start'), ('C', 'complete')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_hash',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
    ]
