# Generated by Django 3.1.7 on 2021-06-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0029_auto_20210614_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadberkasprosiding',
            name='bukti_plagiasi',
            field=models.FileField(blank=True, null=True, upload_to='plagiasi_prosiding/', verbose_name='Upload Bukti Plagiasi'),
        ),
        migrations.AddField(
            model_name='uploadberkasprosiding',
            name='plagiasi',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Similarity Index'),
        ),
    ]
