# Generated by Django 3.1.7 on 2021-04-12 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0013_auto_20210412_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='penilaianberkasjurnal',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]
