# Generated by Django 5.1.1 on 2024-10-10 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_reinspeccion_prevencion_rif_comercio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reinspeccion_prevencion',
            name='nombre_comercio',
        ),
    ]
