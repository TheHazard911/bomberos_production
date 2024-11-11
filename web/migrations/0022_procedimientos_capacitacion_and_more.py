# Generated by Django 5.1.2 on 2024-10-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_procedimientos_psicologia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimientos_Capacitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_capacitacion', models.CharField(max_length=40)),
                ('tipo_clasificacion', models.CharField(max_length=40)),
                ('personas_beneficiadas', models.CharField(max_length=4)),
                ('descripcion', models.CharField(max_length=100)),
                ('material_utilizado', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Procedimientos_Frente_Preventivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_actividad', models.CharField(max_length=80)),
                ('estrategia', models.CharField(max_length=100)),
                ('personas_beneficiadas', models.CharField(max_length=4)),
                ('descripcion', models.CharField(max_length=100)),
                ('material_utilizado', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
