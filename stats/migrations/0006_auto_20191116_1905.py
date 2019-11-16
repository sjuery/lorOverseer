# Generated by Django 2.2.7 on 2019-11-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_game_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='totalGames',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deck',
            name='totalGames',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='totalGames',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]