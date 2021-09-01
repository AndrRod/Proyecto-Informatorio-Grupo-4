# Generated by Django 3.2.3 on 2021-09-01 18:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AniversarioChaco', '0053_auto_20210901_0731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='CANTIDAD_PREGUNTAS_RESPONDIDAS_CORRECTAMENTE',
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='max_puntaje',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6, verbose_name='Maximo Puntaje'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='CANTIDAD_PARTIDAS_JUGADAS',
            field=models.IntegerField(default=0, null=True, verbose_name='historial cantidad de partidas Jugadas'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2021, 9, 1, 18, 23, 28, 331452, tzinfo=utc), verbose_name='fecha de login'),
        ),
    ]
