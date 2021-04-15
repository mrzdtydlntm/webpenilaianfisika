# Generated by Django 3.1.7 on 2021-04-11 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('penilaian', '0005_auto_20210411_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadberkasjurnal',
            name='is_verificated',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='uploadberkasjurnal',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_jurnal_reviewer', to=settings.AUTH_USER_MODEL),
        ),
    ]
