from django.db import models
from recursos_humanos.models import Empresa,Empleado

# Create your models here.
class Variable(models.Model):
    cod_variable = models.AutoField(unique=True, primary_key=True)
    descripcion = models.CharField(max_length=250)
    monto = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return '%s ,  Monto: %s' %(self.descripcion , self.monto)

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

class ElementoPago(models.Model):
    AD = (
        ('asignacion', 'Asignacion'),
        ('deduccion', 'Deduccion'),
        ('prestamo', 'Prestamo'),
    )
    CP = (
        ('fijo', 'Fijo'),
        ('variable', 'Variable'),
        ('fijoingreso','Fijo De Ingreso')
    ) 
    FC = (

        ('td','Todas las Quincenas'),
        ('fm','Final de Mes'),
    ) 
    cod_elemento_pago = models.AutoField(unique=True, primary_key=True)
    descripcion = models.CharField(max_length=20)
    codigo_ad = models.CharField(choices=AD, max_length=30, default='asignacion')
    cod_formula = models.ForeignKey(Formulacion, on_delete=models.SET_NULL,  blank=True, null=True)
    formula = models.CharField(max_length=250 ,blank=True, null=True, verbose_name='Formula o Monto')
    frecuencia = models.CharField(choices=FC, max_length=30, default='td',blank=True, null=True)
    codigo_cp = models.CharField(choices=CP, max_length=30, default='variable',blank=True, null=True)
    control = models.CharField(max_length=100,blank=True, null=True)
    empleado_pago = models.ManyToManyField(Empleado,  through='PagoEmpleado')
    pago = models.ManyToManyField('self',  through='PagoEmpleado', symmetrical=False)



    def save(self, *args, **kwargs):
        if not self.formula:
            self.formula = self.cod_formula.formula
        super(ElementoPago, self).save(*args, **kwargs) 

    def __str__(self):
    	return self.descripcion

    class Meta:
        verbose_name = "Elemento de Pago"
        verbose_name_plural = "Elementos de Pago"



class PagoEmpleado(models.Model):
    cod_pago = models.AutoField(unique=True, primary_key=True)
    cod_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, blank=True, null=True)
    elemento_pago = models.ForeignKey(ElementoPago, on_delete=models.CASCADE , blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True, default='1')
    monto = models.DecimalField(decimal_places=2, max_digits=20, default='0',blank=True, null=True)
    formula = models.CharField(max_length=250 ,blank=True, null=True)

    def save(self, *args, **kwargs):
        self.formula = self.elemento_pago.formula
        self.monto = eval(self.elemento_pago.formula)
        if self.elemento_pago.codigo_ad == 'deduccion':
            self.monto = self.monto*-1
        if self.cantidad > 0:
             self.monto = self.monto*self.cantidad
        super(PagoEmpleado, self).save(*args, **kwargs) 

    class Meta:
        ordering = ('cod_empleado',)
        verbose_name = "Pago de Empleado"
        verbose_name_plural = "Pagos de los Empleados"

    def __str__(self):
        return 'Empleado %s, Pago: %s' %(self.cod_empleado , self.elemento_pago)