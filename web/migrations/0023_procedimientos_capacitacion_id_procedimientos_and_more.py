# Generated by Django 5.1.2 on 2024-10-22 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_procedimientos_capacitacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedimientos_capacitacion',
            name='id_procedimientos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.procedimientos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procedimientos_frente_preventivo',
            name='id_procedimientos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.procedimientos'),
            preserve_default=False,
        ),
    ]
