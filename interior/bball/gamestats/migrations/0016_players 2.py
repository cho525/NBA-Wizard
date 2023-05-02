# Generated by Django 4.2 on 2023-04-25 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestats', '0015_alter_teamcache_ast_alter_teamcache_ftd_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=100)),
                ('pic', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('playerid', models.CharField(max_length=100)),
            ],
        ),
    ]