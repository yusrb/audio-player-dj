# Generated by Django 5.1.4 on 2024-12-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_playlist_lagu_alter_lagu_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lagu',
            name='playlist',
            field=models.ManyToManyField(blank=True, to='base.playlist'),
        ),
    ]
