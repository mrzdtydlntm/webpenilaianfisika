# Generated by Django 3.1.7 on 2021-05-08 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0019_auto_20210507_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='penilaianberkasbuku',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='penilaianberkasbuku2',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='penilaianberkashaki',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='penilaianberkashaki2',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='penilaianberkasprosiding',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='penilaianberkasprosiding2',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
