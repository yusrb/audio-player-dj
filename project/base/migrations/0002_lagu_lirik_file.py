# Generated by Django 5.1.4 on 2024-12-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lagu',
            name='lirik_file',
            field=models.FileField(blank=True, null=True, upload_to='lirik'),
        ),
    ]
