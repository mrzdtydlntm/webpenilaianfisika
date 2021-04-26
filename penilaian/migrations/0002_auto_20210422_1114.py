# Generated by Django 3.1.7 on 2021-04-22 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadberkasbuku',
            name='penulis_lain_selain',
        ),
        migrations.AddField(
            model_name='uploadberkasbuku',
            name='penulis_lain_selain',
            field=models.ManyToManyField(blank=True, to='penilaian.PenulisLain', verbose_name='Penulis Lain Selain Dosen'),
        ),
        migrations.AlterField(
            model_name='uploadberkasbuku',
            name='penulis_utama_selain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pu_lain_buku', to='penilaian.penulislain', verbose_name='Penulis Utama Selain Dosen'),
        ),
        migrations.RemoveField(
            model_name='uploadberkashaki',
            name='pemegang_berkas_selain',
        ),
        migrations.AddField(
            model_name='uploadberkashaki',
            name='pemegang_berkas_selain',
            field=models.ManyToManyField(blank=True, to='penilaian.PenulisLain', verbose_name='Pemegang Berkas Selain Dosen'),
        ),
        migrations.AlterField(
            model_name='uploadberkashaki',
            name='pemegang_berkas_utama_selain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pb_lain_haki', to='penilaian.penulislain', verbose_name='Pemegang Berkas Utama Selain Dosen'),
        ),
        migrations.AlterField(
            model_name='uploadberkasprosiding',
            name='corresponding_author_selain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ca_lain_prosiding', to='penilaian.penulislain', verbose_name='Corresponding Author Selain Dosen'),
        ),
        migrations.RemoveField(
            model_name='uploadberkasprosiding',
            name='penulis_selain',
        ),
        migrations.AddField(
            model_name='uploadberkasprosiding',
            name='penulis_selain',
            field=models.ManyToManyField(blank=True, to='penilaian.PenulisLain', verbose_name='Penulis Lain Selain Dosen'),
        ),
        migrations.AlterField(
            model_name='uploadberkasprosiding',
            name='penulis_utama_selain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pu_lain_prosiding', to='penilaian.penulislain', verbose_name='Penulis Utama Selain Dosen'),
        ),
    ]