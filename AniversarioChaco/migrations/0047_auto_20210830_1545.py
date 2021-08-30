# Generated by Django 3.2.3 on 2021-08-30 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AniversarioChaco', '0046_alter_usuario_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='CANTIDAD_PREGUNTAS_RESPONDIDAS',
            field=models.IntegerField(default=0, verbose_name='cantidad de preguntas respondidas'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2021, 8, 30, 15, 45, 40, 404766), verbose_name='fecha de login'),
        ),
    ]