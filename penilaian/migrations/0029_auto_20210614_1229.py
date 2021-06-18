# Generated by Django 3.1.7 on 2021-06-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0028_gabunganpenilaianberkasjurnal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadberkasbuku',
            name='nomor_isbn',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nomor ISBN'),
        ),
        migrations.AlterField(
            model_name='users',
            name='jabatan',
            field=models.CharField(blank=True, default=None, max_length=70, verbose_name='Jabatan Fungsional'),
        ),
        migrations.AlterField(
            model_name='users',
            name='pangkat',
            field=models.CharField(blank=True, default=None, max_length=70, verbose_name='Pangkat/Golongan/Ruang'),
        ),
        migrations.AlterField(
            model_name='users',
            name='unit',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='Unit Kerja'),
        ),
    ]
