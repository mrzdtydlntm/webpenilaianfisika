# Generated by Django 3.1.7 on 2021-05-02 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0007_auto_20210502_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadberkashaki',
            name='jenis_haki',
            field=models.CharField(choices=[('Merek', 'Merek'), ('Paten', 'Paten'), ('Hak Cipta', 'Hak Cipta'), ('Desain Industri', 'Desain Industri'), ('Indikasi Geografis', 'Indikasi Geografis'), ('DTLST', 'DTLST'), ('Rahasia Dagang', 'Rahasia Dagang')], max_length=50, verbose_name='Jenis HaKI'),
        ),
    ]