# Generated by Django 3.0.5 on 2020-04-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='estado',
            field=models.BooleanField(choices=[(0, 'Fijo'), (1, 'Eventual')]),
        ),
    ]