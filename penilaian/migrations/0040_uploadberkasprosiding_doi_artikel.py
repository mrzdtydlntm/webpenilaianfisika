# Generated by Django 3.1.7 on 2022-05-31 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0039_auto_20220531_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadberkasprosiding',
            name='doi_artikel',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='DOI Artikel'),
        ),
    ]
