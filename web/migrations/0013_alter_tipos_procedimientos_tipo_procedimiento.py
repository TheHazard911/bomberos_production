# Generated by Django 5.1.2 on 2024-10-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_inspeccion_establecimiento_art'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipos_procedimientos',
            name='tipo_procedimiento',
            field=models.CharField(max_length=60),
        ),
    ]
