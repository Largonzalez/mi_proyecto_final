# Generated by Django 4.0.3 on 2022-05-11 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_rename_viajes_vacaciones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacaciones',
            old_name='descripcion_viaje',
            new_name='descripcion',
        ),
    ]