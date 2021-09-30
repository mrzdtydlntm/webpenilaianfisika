# Generated by Django 3.1.7 on 2021-09-30 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0035_uploadberkasbuku_url_buku'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadberkasjurnal',
            name='url_jurnal_lengkap',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Link Jurnal Lengkap'),
        ),
        migrations.AddField(
            model_name='uploadberkasprosiding',
            name='url_prosiding_lengkap',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Link Prosiding Lengkap'),
        ),
        migrations.AlterField(
            model_name='uploadberkasbuku',
            name='url_buku',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Url Buku'),
        ),
        migrations.AlterField(
            model_name='uploadberkashaki',
            name='url_repository',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Alamat Repository'),
        ),
        migrations.AlterField(
            model_name='uploadberkasjurnal',
            name='url_jurnal',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Link Jurnal'),
        ),
        migrations.AlterField(
            model_name='uploadberkasprosiding',
            name='url_repository',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Link Repository'),
        ),
    ]