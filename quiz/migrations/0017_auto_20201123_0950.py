# Generated by Django 2.2 on 2020-11-23 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_auto_20201122_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='creator_page_visit_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='opponent_page_visit_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
