# Generated by Django 3.1.7 on 2022-07-15 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0041_uploadberkashaki_url_penerbit'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadberkasbuku',
            name='verificated_remark',
            field=models.TextField(blank=True, null=True, verbose_name='Komentar Verifikasi'),
        ),
        migrations.AddField(
            model_name='uploadberkashaki',
            name='verificated_remark',
            field=models.TextField(blank=True, null=True, verbose_name='Komentar Verifikasi'),
        ),
        migrations.AddField(
            model_name='uploadberkasjurnal',
            name='verificated_remark',
            field=models.TextField(blank=True, null=True, verbose_name='Komentar Verifikasi'),
        ),
        migrations.AddField(
            model_name='uploadberkasprosiding',
            name='verificated_remark',
            field=models.TextField(blank=True, null=True, verbose_name='Komentar Verifikasi'),
        ),
    ]
