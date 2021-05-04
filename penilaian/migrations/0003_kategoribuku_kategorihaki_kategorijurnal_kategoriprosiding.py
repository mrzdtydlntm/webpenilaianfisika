# Generated by Django 3.1.7 on 2021-04-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0002_auto_20210428_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriBuku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=100, verbose_name='Kategori Buku')),
                ('nilai_max', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KategoriHaki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=100, verbose_name='Kategori Haki')),
                ('nilai_max', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KategoriJurnal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=100, verbose_name='Kategori Jurnal')),
                ('nilai_max', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KategoriProsiding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=100, verbose_name='Kategori Prosiding')),
                ('nilai_max', models.PositiveIntegerField()),
            ],
        ),
    ]