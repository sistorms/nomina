from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime    
from django.db.models import Count    


User = settings.AUTH_USER_MODEL


class Empresa(models.Model):
    cod_empresa = models.AutoField(unique=True, primary_key=True) 
    nombre = models.CharField(max_length=50, null=True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    fecha_creacion = models.DateField(auto_now= False, auto_now_add=False)
    fecha_update = models.DateField(auto_now= True)

    def __str__(self):
        return self.nombre


    



class Persona(models.Model):
    cod_solicitud = models.AutoField(primary_key=True)
    STATUS = (
        ('trabajando', 'Trabajando'),
        ('desempleado', 'Desempleado'),
        ('ingresado', 'Ingresado'),
       
    )
    GENERO = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
        ('ninguno', 'Prefiero No Contestar'),
    ) 
    status = models.CharField(choices=STATUS, max_length=30, default='desempleado', verbose_name='Estado De La Persona')  
    cedula = models.IntegerField(blank=True, null=True, verbose_name='Cedula')  
    apellido_1 = models.CharField(max_length=30, verbose_name='Primer Apellido')  
    nombre_1 = models.CharField(max_length=30, verbose_name='Primer Nombre')
    nombre_2 = models.CharField(max_length=30, verbose_name='Segundo Nombre', blank=True, null=True)
    apellido_2 = models.CharField(max_length=30, verbose_name='Segundo Apellido', blank=True, null=True)      
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True, verbose_name='Ingreso Del Sistema')
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True, verbose_name="Codigo Empresa")
    fecha_nacimiento = models.DateField(auto_now= False, auto_now_add=False, blank=True, null=True, verbose_name="Fecha de Nacimiento")
    edad = models.IntegerField(blank=True, null=True, verbose_name='Edad')  
    ocupacion = models.CharField(max_length=30, verbose_name='Ocupacion Actual', blank=True, null=True)
    cargo_opt = models.CharField(max_length=30, verbose_name='Cargo a Optar', blank=True, null=True)
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    telf = models.IntegerField( blank=True, null=True, verbose_name='Telefono')
    genero = models.CharField(choices=GENERO, max_length=50, null=True, blank=True)

    
    def __str__(self):
        return ' Cod %s |  %s , %s|' % (self.cod_solicitud, self.nombre_1, self.apellido_1)

class Familia(models.Model):
    
    cod_familia = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    cedula = models.IntegerField(blank=True, null=True, verbose_name='Cedula')  
    apellido_1 = models.CharField(max_length=30, verbose_name='Primer Apellido')  
    nombre_1 = models.CharField(max_length=30, verbose_name='Primer Nombre')
    nombre_2 = models.CharField(max_length=30, verbose_name='Segundo Nombre', blank=True, null=True)
    apellido_2 = models.CharField(max_length=30, verbose_name='Segundo Apellido', blank=True, null=True)
    fecha_nacimiento = models.DateField(auto_now= False, auto_now_add=False, blank=True, null=True, verbose_name="Fecha de Nacimiento")
    class Meta:
        verbose_name= "Familia"
        verbose_name_plural = "Familiares"
    
class Educacion(models.Model):
    cod_educ = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, verbose_name='Titulo Obtenido')
    finalizado = models.BooleanField()
    inicio = models.DateField(auto_now= False, auto_now_add=False, blank=True, null=True, verbose_name='Fecha De Inicio Del Curso')
    fin = models.DateField(auto_now= False, auto_now_add=False, blank=True, null=True, verbose_name='Fecha De Obtencion Del Titulo')
    aptitudes = models.CharField(max_length=50, verbose_name='Aptitud o Habilidad Obtenida')
    
    class Meta:
        verbose_name= "Nivel Educativo"
        verbose_name_plural = "Educacion"

class Escala(models.Model):
    cod_escala = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo De Escala')
    escala = models.CharField(max_length=20, verbose_name='Nombre Escala')
    grado = models.IntegerField(verbose_name='Grado')
    paso = models.IntegerField(verbose_name='Paso')
    sueldo = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Sueldo')
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True, verbose_name='Codigo De La Empresa')      

    class Meta:
        ordering = ['escala']
        unique_together = ['escala','grado','paso']

    def __str__(self):
       return ' Escala %s | Grado %s | Paso %s | Sueldo: %s' % (self.escala, self.grado, self.paso, self.sueldo)

class Cargo(models.Model):
    cod_cargo = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo Del Cargo')
    cod_escala = models.ForeignKey(Escala, on_delete=models.SET_NULL, blank=True, null=True,verbose_name='Codigo Escala')
    des_cargo = models.CharField(max_length=50, null=True, verbose_name='Descripcion Del Cargo')
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True, verbose_name='Codigo De La Empresa')      

    def __str__(self):
            return self.des_cargo

class Departamento(models.Model):
    cod_departamento = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo Del Departamento')
    descripcion = models.CharField(max_length=50, null=True, verbose_name='Nombre Departamento')
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True, verbose_name='Codigo De La Empresa')      
 
    def __str__(self):
            return self.descripcion

class Rac(models.Model):
    cod_rac = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo RAC')
    cod_departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Codigo Del Departamento')
    cod_cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Codigo Del Cargo')
    cod_solicitud = models.ForeignKey(Persona, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Codigo De Solicitud Empleado')
    cod_escala = models.ForeignKey(Escala, on_delete=models.SET_NULL, blank=True, null=True)
    compensacion = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now= False, auto_now_add=False)
    fecha_update = models.DateTimeField(auto_now= True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True, verbose_name='Codigo De La Empresa')
    sueldo = models.DecimalField(decimal_places=2, max_digits=20)

    def save(self, *args, **kwargs):
        self.cod_escala = self.cod_cargo.cod_escala
        self.sueldo = self.cod_escala.sueldo
        super(Rac, self).save(*args, **kwargs)

    def __str__(self):
        return ' RAC %s , Departamento: %s, Sueldo: %s' % (self.cod_rac, self.cod_departamento.descripcion, self.sueldo)

class Empleado(models.Model):
    cod_empleado = models.AutoField(unique=True, primary_key=True)
    cedula = models.IntegerField(blank=True, null=True)  
    apellido = models.CharField(max_length=30,blank=True, null=True)  
    nombre = models.CharField(max_length=30,blank=True, null=True)  
    cod_rac = models.ForeignKey(Rac, on_delete=models.SET_NULL, blank=True, null=True)
    cod_departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True)
    cod_solicitud = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True, related_name='Solicitud_Empleado')
    sueldo = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now= False, auto_now_add=True)
    fecha_update = models.DateTimeField(auto_now= True)
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True)      
    cod_cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, blank=True, null=True) 
   
    def save(self, *args, **kwargs):
        self.cod_departamento = self.cod_rac.cod_departamento
        self.sueldo = self.cod_rac.cod_escala.sueldo
        self.cod_empresa = self.cod_rac.cod_cargo.cod_empresa
        self.cod_cargo = self.cod_rac.cod_cargo

        super(Empleado, self).save(*args, **kwargs)

    def __str__(self):
        return self.cod_rac.cod_solicitud.nombre_1

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
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True)

    class Meta:
        verbose_name= "Formulacion"
        verbose_name_plural= "Formulaciones"
    
    def __str__(self):
        return self.descripcion


class ElementoPago2(models.Model):
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
    empleado_pago = models.ManyToManyField(Empleado,  through='PagoEmpleado2')
    pago = models.ManyToManyField('self',  through='PagoEmpleado2', symmetrical=False)



    def save(self, *args, **kwargs):
        if not self.formula:
            self.formula = self.cod_formula.formula
        super(ElementoPago2, self).save(*args, **kwargs) 

    def __str__(self):
    	return self.descripcion

    class Meta:
        verbose_name = "Elemento de Pago"
        verbose_name_plural = "Elementos de Pago"



class PagoEmpleado2(models.Model):
    cod_pago = models.AutoField(unique=True, primary_key=True)
    cod_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, blank=True, null=True)
    elemento_pago = models.ForeignKey(ElementoPago2, on_delete=models.CASCADE , blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True, default='1')
    monto = models.DecimalField(decimal_places=2, max_digits=20, default='0',blank=True, null=True)
    formula = models.CharField(max_length=250 ,blank=True, null=True)

    def save(self, *args, **kwargs):
        self.formula = self.elemento_pago.formula
        self.monto = eval(self.formula)
        if self.elemento_pago.codigo_ad == 'deduccion':
            self.monto = self.monto*-1
        if self.cantidad > 0:
            self.monto = self.monto*self.cantidad
        super(PagoEmpleado2, self).save(*args, **kwargs) 

    class Meta:
        ordering = ('cod_empleado',)
        verbose_name = "Pago de Empleado"
        verbose_name_plural = "Pagos de los Empleados"

    def __str__(self):
        return 'Empleado %s, Pago: %s' %(self.cod_empleado , self.elemento_pago)




class Prenomina(models.Model):
	PG = (
        ('obreros', 'Obreros'),
        ('trabajadores', 'Trabajadores'),
        ('ejecutivo', 'Ejecutivo'),
    	)
	cod_prenomina = models.AutoField(unique=True, primary_key=True)
	tipo = models.CharField(choices=PG, max_length=30, default='trabajadores')
	descripcion =  models.CharField(max_length=20, blank=True, null=True)
	pagos_empleados = models.ManyToManyField(PagoEmpleado2)
	fecha_inicio = models.DateTimeField(blank=True, null=True)
	fecha_final = models.DateTimeField(blank=True, null=True)



    




# class NominaSummary(Prenomina2):
#     class Meta:
#         proxy= True
#         verbose_name = "pago prenomina"
#         verbose_name_plural = "pagos prenominas"
   
# class PreNomina2(models.Model):
# 	cod_pago = models.AutoField(unique=True, primary_key=True)
# 	pagos_empleados = models.ManyToManyField(PagoEmpleado2)
# 	fecha = models.DateTimeField()
	

# class PreNomina3(models.Model):
# 	pago = models.ForeignKey(PagoEmpleado2, on_delete=models.CASCADE)
# 	orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
# 	fecha = models.DateTimeField()


# class ElementoPago(models.Model):
#     AD = (
#         ('asignacion', 'Asignacion'),
#         ('deduccion', 'Deduccion'),
#     )
#     CP = (
#         ('fijo', 'Fijo'),
#         ('variable', 'Variable'),
#         ('fijoingreso','Fijo De Ingreso')
#     ) 
#     FC = (

#         ('td','Todas las Quincenas'),
#         ('fm','Final de Mes'),
#     ) 
#     cod_elemento_pago = models.AutoField(unique=True, primary_key=True)
#     descripcion = models.CharField(max_length=20)
#     codigo_ad = models.CharField(choices=AD, max_length=30, default='asignacion')
#     cod_formula = models.ForeignKey(Formulacion, on_delete=models.SET_NULL,  blank=True, null=True)
#     formula = models.CharField(max_length=250 ,blank=True, null=True)
#     monto = models.DecimalField(decimal_places=2, max_digits=20, default='0', blank=True, null=True)
#     frecuencia = models.CharField(choices=FC, max_length=30, default='td',blank=True, null=True)
#     codigo_cp = models.CharField(choices=CP, max_length=30, default='variable',blank=True, null=True)
#     control = models.CharField(max_length=100,blank=True, null=True)



#     def save(self, *args, **kwargs):
#         if not self.monto:
#             if not self.formula:
#                 self.formula = self.cod_formula.formula
#             else:
#                 self.formula = self.formula
#         super(ElementoPago, self).save(*args, **kwargs) 

#     def __str__(self):
#     	return self.descripcion



# class PagoEmpleado(models.Model):
#     cod_empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL ,blank=True, null=True)
#     cod_elemento_pago = models.ForeignKey(ElementoPago, on_delete=models.CASCADE, blank=True, null=True)
#     cantidad = models.IntegerField()
#     monto = models.DecimalField(decimal_places=2, max_digits=20, default='0',blank=True, null=True)
#     formula = models.CharField(max_length=250 ,blank=True, null=True)

#     class Meta:
#         ordering = ('cod_empleado',)

#     def save(self, *args, **kwargs):
#         if not self.monto:
#             self.formula = self.cod_elemento_pago.formula
#             self.monto = eval(self.formula)
#         if self.cod_elemento_pago.codigo_ad == 'deduccion':
#             self.monto = self.monto*-1
#         super(PagoEmpleado, self).save(*args, **kwargs) 

#     def __str__(self):
#        return ' %s , Pago %s ' % (self.cod_empleado.cod_solicitud.nombre_1, self.cod_elemento_pago.descripcion)

# class PreNomina(models.Model):
#     pagos = models.ManyToManyField(PagoEmpleado)
#     periodo_i = models.DateTimeField()
#     periodo_f = models.DateTimeField()
#     empleado = models.CharField(max_length=250)

#     class Meta:
#         ordering = ('empleado',)
