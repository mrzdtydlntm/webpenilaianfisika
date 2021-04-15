# Generated by Django 3.1.7 on 2021-04-10 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('penilaian', '0002_auto_20210410_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadberkasbuku',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_buku_reviewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uploadberkashaki',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_haki_reviewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='uploadberkasprosiding',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_prosiding_reviewer', to=settings.AUTH_USER_MODEL),
        ),
    ]
