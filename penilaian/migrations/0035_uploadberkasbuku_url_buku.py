# Generated by Django 3.1.7 on 2021-09-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0034_uploadberkasbuku_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadberkasbuku',
            name='url_buku',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tahun Terbit'),
        ),
    ]