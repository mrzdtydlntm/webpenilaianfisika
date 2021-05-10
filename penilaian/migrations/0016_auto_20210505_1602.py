# Generated by Django 3.1.7 on 2021-05-05 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0015_auto_20210505_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadberkasbuku',
            name='pengusul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_pengusul_buku', to='penilaian.users', verbose_name='Pengusul'),
        ),
        migrations.AlterField(
            model_name='uploadberkashaki',
            name='pengusul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_pengusul_haki', to='penilaian.users', verbose_name='Pengusul'),
        ),
        migrations.AlterField(
            model_name='uploadberkasjurnal',
            name='pengusul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_pengusul_jurnal', to='penilaian.users', verbose_name='Pengusul'),
        ),
        migrations.AlterField(
            model_name='uploadberkasprosiding',
            name='pengusul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_pengusul_prosiding', to='penilaian.users', verbose_name='Pengusul'),
        ),
    ]
