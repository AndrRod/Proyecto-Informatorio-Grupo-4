# Generated by Django 3.2.3 on 2021-09-03 03:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AniversarioChaco', '0055_auto_20210901_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='CANTIDAD_PREGUNTAS_RESPONDIDAS_CORRECTAMENTE',
            field=models.IntegerField(default=0, verbose_name='historial cantidad de preguntas respondidas correctamente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2021, 9, 3, 3, 15, 10, 796625, tzinfo=utc), verbose_name='fecha de login'),
        ),
    ]
