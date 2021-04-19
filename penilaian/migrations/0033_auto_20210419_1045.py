# Generated by Django 3.1.7 on 2021-04-19 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0032_auto_20210419_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadberkasbuku',
            name='jmlh_penulis_lain',
        ),
        migrations.RemoveField(
            model_name='uploadberkashaki',
            name='jmlh_penulis_lain',
        ),
        migrations.RemoveField(
            model_name='uploadberkasprosiding',
            name='jmlh_penulis_lain',
        ),
        migrations.AddField(
            model_name='penilaianberkasbuku',
            name='jmlh_penulis_lain',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='penilaianberkashaki',
            name='jmlh_penulis_lain',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='penilaianberkasprosiding',
            name='jmlh_penulis_lain',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
