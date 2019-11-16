# Generated by Django 2.2.7 on 2019-11-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191110_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='secretCode',
            field=models.CharField(default='temp', max_length=16),
            preserve_default=False,
        ),
    ]