# Generated by Django 3.1.7 on 2021-05-03 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0008_auto_20210502_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadberkasbuku',
            name='penulis_utama',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_buku_penulis_utama', to='penilaian.users', verbose_name='Penulis Utama'),
        ),
        migrations.AlterField(
            model_name='uploadberkashaki',
            name='pemegang_berkas_utama',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_pemegang_berkas_utama', to='penilaian.users', verbose_name='Pemegang Berkas Utama'),
        ),
    ]
