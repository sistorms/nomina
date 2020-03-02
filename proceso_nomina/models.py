from django.db import models
from concepto_pago.models import PagoEmpleado

# Create your models here.

class Prenomina(models.Model):
	PG = (
        ('obreros', 'Obreros'),
        ('trabajadores', 'Trabajadores'),
        ('ejecutivo', 'Ejecutivo'),
    	)
	cod_prenomina = models.AutoField(unique=True, primary_key=True)
	tipo = models.CharField(choices=PG, max_length=30, default='trabajadores')
	descripcion =  models.CharField(max_length=20, blank=True, null=True)
	pagos_empleados = models.ManyToManyField(PagoEmpleado)
	fecha_inicio = models.DateTimeField(blank=True, null=True)
	fecha_final = models.DateTimeField(blank=True, null=True)

class Nomina(models.Model):
	cod_nomina = models.AutoField(unique=True, primary_key=True)
	cod_prenomina = models.ForeignKey(Prenomina, verbose_name='Prenomina Procesada', on_delete=models.CASCADE)
	procesado = models.BooleanField(verbose_name='Procesar Nomina')




class PrenominaSummary(Prenomina):
    class Meta:
        proxy = True
        verbose_name = 'Informacion Nomina'
        verbose_name_plural = 'Vista Sobre las Nominas'