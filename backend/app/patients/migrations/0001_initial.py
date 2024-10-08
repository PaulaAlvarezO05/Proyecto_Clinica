# Generated by Django 5.1.1 on 2024-09-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=200, verbose_name='Nombres Completo')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('genero', models.CharField(max_length=30, verbose_name='Género')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('nombre_emergencia', models.CharField(max_length=200, verbose_name='Nombre Contacto de Emergencia')),
                ('telefono_emergencia', models.IntegerField(verbose_name='Teléfono de Emergencia')),
                ('compañia_Seguros', models.CharField(max_length=100, verbose_name='Compañia de Seguros')),
                ('numero_poliza', models.IntegerField(verbose_name='Número de Poliza')),
                ('estado_poliza', models.CharField(max_length=20, verbose_name='Estado de Póliza')),
                ('vigencia_poliza', models.DateField(verbose_name='Vigencia de Poliza')),
            ],
        ),
    ]
