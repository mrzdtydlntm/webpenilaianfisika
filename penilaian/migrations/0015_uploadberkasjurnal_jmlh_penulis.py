# Generated by Django 3.1.7 on 2021-04-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0014_penilaianberkasjurnal_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadberkasjurnal',
            name='jmlh_penulis',
            field=models.PositiveIntegerField(default=None, verbose_name='Jumlah Penulis'),
            preserve_default=False,
        ),
    ]
