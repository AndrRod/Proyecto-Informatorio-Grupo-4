# Generated by Django 3.2.3 on 2021-08-22 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AniversarioChaco', '0015_alter_preguntasrespondidas_respuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntasrespondidas',
            name='respuesta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AniversarioChaco.elegirrespuesta'),
        ),
    ]
