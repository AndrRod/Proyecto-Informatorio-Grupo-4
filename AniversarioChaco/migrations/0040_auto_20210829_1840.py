# Generated by Django 3.2.3 on 2021-08-29 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AniversarioChaco', '0039_auto_20210829_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='CANTIDAD_PARTIDAS_JUGADAS',
            field=models.IntegerField(default=0, verbose_name='cantidad departidas Jugadas'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2021, 8, 29, 18, 40, 58, 9436), verbose_name='fecha de login'),
        ),
    ]
