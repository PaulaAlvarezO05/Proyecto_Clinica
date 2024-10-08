# Generated by Django 5.1.1 on 2024-09-29 18:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
        ('consultationType', '0001_initial'),
        ('patients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='medico',
            field=models.ForeignKey(blank=True, limit_choices_to={'rol__nombre': 'Médico'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Médico'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patient', verbose_name='Paciente'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='tipo_consulta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consultationType.consultationtype', verbose_name='Tipo de consulta'),
        ),
    ]
