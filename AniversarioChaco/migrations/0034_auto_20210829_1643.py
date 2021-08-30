# Generated by Django 3.2.3 on 2021-08-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AniversarioChaco', '0033_auto_20210829_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='dificultad_o_categoria',
            field=models.CharField(choices=[('Facil', 'Facil'), ('Medio', 'Medio'), ('Dificil', 'Dificil')], max_length=90, null=True, verbose_name='dificultad'),
        ),
        migrations.DeleteModel(
            name='Caract_Categoria',
        ),
    ]
