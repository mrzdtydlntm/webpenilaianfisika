# Generated by Django 3.1.7 on 2021-04-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0009_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadberkasjurnal',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_jurnal_reviewer', to='penilaian.reviewer'),
        ),
    ]
