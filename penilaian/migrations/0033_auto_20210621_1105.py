# Generated by Django 3.1.7 on 2021-06-21 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0032_auto_20210614_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='pangkat',
            field=models.CharField(default=None, max_length=100, verbose_name='Pangkat/Golongan/Ruang'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='jabatan_pangkat',
            field=models.CharField(max_length=100, verbose_name='Jabatan Fungsional'),
        ),
    ]
