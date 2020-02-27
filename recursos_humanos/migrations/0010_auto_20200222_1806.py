# Generated by Django 3.0.3 on 2020-02-22 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_humanos', '0009_auto_20200222_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='des_cargo',
        ),
        migrations.AddField(
            model_name='cargo',
            name='cargo',
            field=models.CharField(max_length=50, null=True, verbose_name='Cargo'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion del Cargo'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='cod_empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recursos_humanos.Empresa', verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='cod_escala',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recursos_humanos.Escala', verbose_name='Escala de Sueldo'),
        ),
    ]
