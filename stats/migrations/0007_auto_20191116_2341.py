# Generated by Django 2.2.7 on 2019-11-16 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_auto_20191116_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='region',
            new_name='regions',
        ),
    ]
