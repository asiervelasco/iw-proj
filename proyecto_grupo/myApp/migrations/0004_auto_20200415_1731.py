# Generated by Django 3.0.5 on 2020-04-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20200415_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='responsable',
        ),
        migrations.AddField(
            model_name='tarea',
            name='responsable',
            field=models.ManyToManyField(to='myApp.Empleado'),
        ),
    ]