# Generated by Django 2.2.7 on 2019-11-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0008_auto_20191117_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='losses',
            new_name='expeditionLosses',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='totalGames',
            new_name='expeditionTotal',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='wins',
            new_name='expeditionWins',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='losses',
            new_name='expeditionLosses',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='totalGames',
            new_name='expeditionTotal',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='wins',
            new_name='expeditionWins',
        ),
        migrations.AddField(
            model_name='card',
            name='normalLosses',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='normalTotal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='normalWins',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='normalLosses',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='normalTotal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='normalWins',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deck',
            name='code',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
