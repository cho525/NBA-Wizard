# Generated by Django 4.2 on 2023-04-22 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestats', '0005_comcache_gamecache_delete_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamecache',
            name='info',
        ),
        migrations.AddField(
            model_name='gamecache',
            name='away',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamecache',
            name='home',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamecache',
            name='id2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamecache',
            name='time',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
