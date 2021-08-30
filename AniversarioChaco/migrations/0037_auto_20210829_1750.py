# Generated by Django 3.2.3 on 2021-08-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AniversarioChaco', '0036_alter_usuario_fecha_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True, verbose_name='fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_login',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha de login'),
        ),
    ]
