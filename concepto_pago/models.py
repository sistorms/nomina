from django.db import models

# Create your models here.
class Variable(models.Model):
    cod_variable = models.AutoField(unique=True, primary_key=True)
    descripcion = models.CharField(max_length=250)
    monto = models.DecimalField(decimal_places=2, max_digits=20)

    class Meta:
        verbose_name= "Variable"
        verbose_name_plural = "Variables"

class Formulacion(models.Model):
    cod_formula = models.AutoField(unique=True, primary_key=True)
    formula = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250, default='prueba')

    class Meta:
        verbose_name= "Formulacion"
        verbose_name_plural= "Formulaciones"
    
    def __str__(self):
        return self.descripcion