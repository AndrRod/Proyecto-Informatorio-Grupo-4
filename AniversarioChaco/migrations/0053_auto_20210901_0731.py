# Generated by Django 3.2.3 on 2021-09-01 10:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AniversarioChaco', '0052_auto_20210901_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='categoria',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='dificultad_o_categoria',
            field=models.CharField(choices=[('Facil', 'Facil'), ('Medio', 'Medio'), ('Dificil', 'Dificil')], default='Facil', max_length=90, null=True, verbose_name='dificultad'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2021, 9, 1, 10, 31, 45, 723234, tzinfo=utc), verbose_name='fecha de login'),
        ),
        migrations.DeleteModel(
            name='Caract_Categoria',
        ),
    ]
