# Generated by Django 3.0.5 on 2020-04-16 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20200415_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='estado',
            field=models.IntegerField(choices=[(0, 'Fijo'), (1, 'Eventual')]),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.IntegerField(choices=[(0, 'Sin empezar'), (1, 'En marcha'), (2, 'Acabada')], max_length=100),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='prioridad',
            field=models.IntegerField(choices=[(0, 'Alta'), (1, 'Media'), (2, 'Baja')], max_length=100),
        ),
    ]