from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime    
from django.db.models import Count 
from django.utils.safestring import mark_safe



# Modelo Empresa
class Empresa(models.Model):
    cod_empresa = models.AutoField(unique=True, primary_key=True) 
    nombre = models.CharField(max_length=50, null=True, verbose_name='Nombre de la Empresa')
    rif = models.CharField(max_length=10)
    fecha_creacion = models.DateField(auto_now= False, auto_now_add=False, verbose_name='Fecha De Creacion De Empresa')
    ceo = models.CharField(max_length=50, verbose_name='Fundador de la Empresa')
    emp = models.PositiveIntegerField(verbose_name='Cantidad De Empleados')
    prop = models.TextField(verbose_name='Proposito de la Empresa')
    fecha_update = models.DateField(auto_now= True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name= "Empresa"
        verbose_name_plural = "Empresas"

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
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True, verbose_name="Codigo Empresa")
    fecha_nacimiento = models.DateField(auto_now= False, auto_now_add=False, blank=True, null=True, verbose_name="Fecha de Nacimiento")
    edad = models.IntegerField(blank=True, null=True, verbose_name='Edad')  
    ocupacion = models.CharField(max_length=30, verbose_name='Ocupacion Actual', blank=True, null=True)
    cargo_opt = models.CharField(max_length=30, verbose_name='Cargo a Optar', blank=True, null=True)
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    telf = models.CharField( max_length=30,blank=True, null=True, verbose_name='Telefono')
    genero = models.CharField(choices=GENERO, max_length=50, null=True, blank=True)
    fech_ing = models.DateField(auto_now= True)
    imagen = models.ImageField(upload_to='empleados', blank=True, null=True)


    def imagen_tag(self):
        if self.imagen:
            return mark_safe('<img src="%s" style="width: 45px; height:45px; margin-left: 30px" />' % self.imagen.url)
        else:
            return 'No Existe Imagen'
    imagen_tag.short_description = 'Imagen'
    imagen_tag.allow_tags = True




    
    def __str__(self):
        return ' Cod %s |  %s , %s|' % (self.cod_solicitud, self.nombre_1, self.apellido_1)
    
    class Meta:
        verbose_name = 'Solicitud De Ingreso'
        verbose_name_plural = 'Solicitudes De Ingresos'

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

class PersonaSummary(Persona):
    class Meta:
        proxy = True
        verbose_name = 'Informacion de Solicitud'
        verbose_name_plural = 'Informacion de Solicitudes'

class Escala(models.Model):
    ESCALA = (
        ('1', 'Escala Nivel I'),
        ('2', 'Escala Nivel II'),
        ('3', 'Escala Nivel III'),
        ('4', 'Escala Nivel IV'),
    ) 

    cod_escala = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo De Escala')
    escala = models.CharField(choices=ESCALA,max_length=20, verbose_name='Nombre Escala')
    grado = models.IntegerField(verbose_name='Grado')
    paso = models.IntegerField(verbose_name='Paso')
    sueldo = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Sueldo Base')
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,  blank=True, null=True, verbose_name='Codigo De La Empresa')      
    porct = models.BooleanField(blank=True,null=True, verbose_name='Porcentaje', default=0)

    def save(self, *args, **kwargs):
        if self.porct==1:
            self.sueldo = self.sueldo/100
        else:
            pass
        super(Escala, self).save(*args, **kwargs) 

    class Meta:
        ordering = ['cod_empresa','escala']
        unique_together = ['cod_empresa','escala','grado','paso']
        verbose_name= "Escala de Sueldo"
        verbose_name_plural = "Escala de Sueldos"

    def __str__(self):
       return ' Escala %s | Grado %s | Paso %s | Sueldo: %s' % (self.escala, self.grado, self.paso, self.sueldo)

class Departamento(models.Model):
    cod_departamento = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo Del Departamento')
    descripcion = models.CharField(max_length=50, null=True, verbose_name='Descripcion')
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,  blank=True, null=True, verbose_name='Empresa')      
 
    def __str__(self):
            return self.descripcion
    class Meta:
        ordering = ['cod_empresa','descripcion']
        verbose_name= "Departamento"
        verbose_name_plural = "Departamentos" 

class Cargo(models.Model):
    cod_cargo = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo Del Cargo')
    cod_escala = models.ForeignKey(Escala, on_delete=models.SET_NULL, blank=True, null=True,verbose_name='Escala de Sueldo')
    cargo = models.CharField(max_length=50, null=True, verbose_name='Nombre del Cargo')
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True, verbose_name='Empresa')      
    sueldo = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Sueldo Base', blank=True, null=True)
    insuel = models.BooleanField(blank=True,null=True, verbose_name='Utilizar Sueldo Escala', default=1)
    desc = models.TextField(verbose_name='Descripcion del Cargo', null=True, blank=True)


    def __str__(self):
            return self.cargo

    def save(self, *args, **kwargs):
        if self.insuel==1:
            self.sueldo = self.cod_escala.sueldo
        else:
            pass
        super(Cargo, self).save(*args, **kwargs) 
    
    class Meta:
        ordering = ['cod_empresa','cargo']
        verbose_name= "Cargo"
        verbose_name_plural = "Cargos" 


class Rac(models.Model):
    cod_rac = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo Puesto')
    cod_departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Departamento')
    cod_cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cargo')
    cod_escala = models.ForeignKey(Escala, on_delete=models.SET_NULL, blank=True, null=True)
    compensacion = models.IntegerField()
    fecha_creacion = models.DateField(auto_now=True)
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True, verbose_name='Empresa')
    sueldo = models.DecimalField(decimal_places=2, max_digits=20)
    #cod_solicitud = models.OneToOneField(Persona, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Solicitud Empleado')

    

    def save(self, *args, **kwargs):
        self.sueldo = self.cod_cargo.sueldo
        self.cod_escala = self.cod_cargo.cod_escala
        self.cod_empresa = self.cod_cargo.cod_empresa
        if self.compensacion:
            self.sueldo = (self.cod_cargo.sueldo+self.compensacion)
        # else:
        #     pass
        # if self.cod_solicitud:
        #     if self.pk is None:
        #         obj = Empleado.objects.update_or_create(
        #             cedula=self.cod_solicitud.cedula , 
        #             apellido_1=self.cod_solicitud.apellido_1 ,
        #              nombre_1=  self.cod_solicitud.nombre_1, 
        #              apellido_2= self.cod_solicitud.apellido_2 , 
        #              nombre_2= self.cod_solicitud.nombre_2,
        #             cod_rac=self.pk ,
        #             cod_cargo= self.cod_cargo, 
        #             cod_departamento= self.cod_departamento, 
        #             sueldo= self.sueldo, 
        #             cod_empresa= self.cod_cargo.cod_empresa, 
        #             edad= self.cod_solicitud.edad, 
        #             email= self.cod_solicitud.email, 
        #             telf= self.cod_solicitud.telf, 
        #             genero=self.cod_solicitud.genero)
        #     if self.cod_rac:
        #         obj2 = Empleado.objects.filter(cod_rac=self.pk).update_or_create(
        #             cedula=self.cod_solicitud.cedula , 
        #             apellido_1=self.cod_solicitud.apellido_1 ,
        #             nombre_1=  self.cod_solicitud.nombre_1, 
        #             apellido_2= self.cod_solicitud.apellido_2 , 
        #             nombre_2= self.cod_solicitud.nombre_2,
        #             cod_cargo= self.cod_cargo, 
        #             cod_departamento= self.cod_departamento, 
        #             sueldo= self.sueldo, 
        #             cod_empresa= self.cod_cargo.cod_empresa, 
        #             edad= self.cod_solicitud.edad, 
        #             email= self.cod_solicitud.email, 
        #             telf= self.cod_solicitud.telf, 
        #             genero=self.cod_solicitud.genero,
        #             cod_rac=self.cod_rac)
                
        # else:
        #     pass

            

        super(Rac, self).save(*args, **kwargs)

    def __str__(self):
        return ' Puesto: %s, Cargo: %s  , Departamento: %s, Sueldo: %s' % (self.cod_rac, self.cod_cargo , self.cod_departamento.descripcion, self.sueldo)
    
    class Meta:
        ordering = ['cod_empresa','cod_rac']
        verbose_name= "Puesto de Trabajo"
        verbose_name_plural = "Puestos de Trabajos" 

class Empleado(models.Model):
    cod_empleado = models.AutoField(unique=True, primary_key=True)
    STATUSE = (
        ('trabajando', 'Trabajando'),
        ('vacaciones', 'Vacaciones'),
        ('jubilado', 'Jubilado'),
       
    )
    GENERO = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
        ('ninguno', 'Prefiero No Contestar'),
    )
    cedula = models.IntegerField(blank=True, null=True, verbose_name='Cedula')
    cod_solicitud = models.OneToOneField(Persona, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Solicitud Empleado')  
    apellido_1 = models.CharField(max_length=30, verbose_name='Primer Apellido')  
    nombre_1 = models.CharField(max_length=30, verbose_name='Primer Nombre')
    nombre_2 = models.CharField(max_length=30, verbose_name='Segundo Nombre', blank=True, null=True)
    apellido_2 = models.CharField(max_length=30, verbose_name='Segundo Apellido', blank=True, null=True) 
    cod_rac = models.OneToOneField(Rac, on_delete=models.SET_NULL, blank=True, null=True)
    cod_cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, blank=True, null=True)
    cod_departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True)
    sueldo = models.FloatField(verbose_name='Sueldo Empleado', blank=True, null=True)
    fecha_creacion = models.DateField(auto_now= False, auto_now_add=False, verbose_name='Fecha de Ingreso' ,blank=True, null= True)
    fecha_update = models.DateField(auto_now= True)
    cod_empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL,  blank=True, null=True, verbose_name="Codigo Empresa")    
    fecha_nacimiento = models.DateField(auto_now= False, auto_now_add=False, blank=True, null=True, verbose_name="Fecha de Nacimiento")
    edad = models.IntegerField(blank=True, null=True, verbose_name='Edad')  
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    telf = models.CharField( max_length=30,blank=True, null=True, verbose_name='Telefono')
    genero = models.CharField(choices=GENERO, max_length=50, null=True, blank=True)
    imagen = models.ImageField(upload_to='empleados', blank=True, null=True)
    status = models.CharField(choices=STATUSE, max_length=30, default='desempleado', verbose_name='Estado De La Persona')  
    direccion = models.TextField(blank=True, null=True, verbose_name='Direccion')

    def imagen_tag(self):
        if self.imagen:
            return mark_safe('<img src="%s" style="width: 45px; height:45px; margin-left: 30px" />' % self.imagen.url)
        else:
            return 'No Existe Imagen'
    imagen_tag.short_description = 'Imagen'
    imagen_tag.allow_tags = True
    class Meta:
        verbose_name= "Empleado"
        verbose_name_plural = "Empleados" 

class FamiliaEmpleado(models.Model):
    
    cod_familia = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cedula = models.IntegerField(blank=True, null=True, verbose_name='Cedula')  
    apellido_1 = models.CharField(max_length=30, verbose_name='Primer Apellido')  
    nombre_1 = models.CharField(max_length=30, verbose_name='Primer Nombre')
    nombre_2 = models.CharField(max_length=30, verbose_name='Segundo Nombre', blank=True, null=True)
    apellido_2 = models.CharField(max_length=30, verbose_name='Segundo Apellido', blank=True, null=True)
    fecha_nacimiento = models.DateField(auto_now= False, auto_now_add=False, blank=True, null=True, verbose_name="Fecha de Nacimiento")
    class Meta:
        verbose_name= "Familia"
        verbose_name_plural = "Familiares"
    
class EducacionEmpleado(models.Model):
    cod_educ = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, verbose_name='Titulo Obtenido')
    finalizado = models.BooleanField()
    inicio = models.DateField(auto_now= False, auto_now_add=False, blank=True, null=True, verbose_name='Fecha De Inicio Del Curso')
    fin = models.DateField(auto_now= False, auto_now_add=False, blank=True, null=True, verbose_name='Fecha De Obtencion Del Titulo')
    aptitudes = models.CharField(max_length=50, verbose_name='Aptitud o Habilidad Obtenida')
    
    class Meta:
        verbose_name= "Nivel Educativo"
        verbose_name_plural = "Educacion"
