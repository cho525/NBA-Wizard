# Generated by Django 4.2 on 2023-04-26 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestats', '0018_remove_players_team_players_age_players_height_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teamid', models.CharField(default='0', max_length=10)),
                ('season', models.CharField(max_length=10)),
                ('wins', models.CharField(max_length=10)),
                ('losses', models.CharField(max_length=10)),
                ('pts', models.CharField(max_length=10)),
                ('ast', models.CharField(default='0', max_length=10)),
                ('orb', models.CharField(default='0', max_length=10)),
                ('ftd', models.CharField(default='0', max_length=10)),
                ('conf', models.CharField(default='0', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='teamcache',
            name='ast',
        ),
        migrations.RemoveField(
            model_name='teamcache',
            name='ftd',
        ),
        migrations.RemoveField(
            model_name='teamcache',
            name='losses',
        ),
        migrations.RemoveField(
            model_name='teamcache',
            name='orb',
        ),
        migrations.RemoveField(
            model_name='teamcache',
            name='pts',
        ),
        migrations.RemoveField(
            model_name='teamcache',
            name='season',
        ),
        migrations.RemoveField(
            model_name='teamcache',
            name='teamid',
        ),
        migrations.RemoveField(
            model_name='teamcache',
            name='wins',
        ),
    ]
