# Generated by Django 3.0.3 on 2020-02-22 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_humanos', '0005_auto_20200216_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personasummary',
            options={'verbose_name': 'Informacion de Solicitud', 'verbose_name_plural': 'Informacion de Solicitudes'},
        ),
        migrations.CreateModel(
            name='Escala',
            fields=[
                ('cod_escala', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Codigo De Escala')),
                ('escala', models.CharField(choices=[('1', 'Escala Nivel I'), ('2', 'Escala Nivel II'), ('3', 'Escala Nivel III'), ('4', 'Escala Nivel IV')], max_length=20, verbose_name='Nombre Escala')),
                ('grado', models.IntegerField(verbose_name='Grado')),
                ('paso', models.IntegerField(verbose_name='Paso')),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Sueldo Base')),
                ('cod_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recursos_humanos.Empresa', verbose_name='Codigo De La Empresa')),
            ],
            options={
                'verbose_name': 'Escala de Sueldo',
                'verbose_name_plural': 'Escala de Sueldos',
                'ordering': ['escala'],
                'unique_together': {('escala', 'grado', 'paso')},
            },
        ),
    ]
