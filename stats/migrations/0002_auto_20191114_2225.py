# Generated by Django 2.2.7 on 2019-11-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='deckCode',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='opponent',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='game',
            name='player',
            field=models.CharField(max_length=25),
        ),
    ]