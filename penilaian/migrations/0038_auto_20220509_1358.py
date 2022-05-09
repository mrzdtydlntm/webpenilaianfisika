# Generated by Django 3.1.7 on 2022-05-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0037_auto_20210930_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadberkasjurnal',
            name='url_resurchify',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL Resurchify'),
        ),
        migrations.AddField(
            model_name='uploadberkasjurnal',
            name='url_sjr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL SJR'),
        ),
        migrations.AddField(
            model_name='uploadberkasprosiding',
            name='url_resurchify',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL Resurchify'),
        ),
        migrations.AddField(
            model_name='uploadberkasprosiding',
            name='url_sjr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='URL SJR'),
        ),
    ]
