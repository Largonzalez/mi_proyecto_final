# Generated by Django 4.0.3 on 2022-04-26 02:36

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=20)),
                ('tamaño', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Personajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=20)),
                ('club_futbol', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Viajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=40)),
                ('transporte', models.CharField(max_length=40)),
                ('duracion', models.CharField(max_length=30)),
                ('descripcion_viaje', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
