from django.contrib import admin
from django import forms
from django.db.models import Sum
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.contenttypes.admin import GenericTabularInline
from tabbed_admin import TabbedModelAdmin


# Register your models here.
from .models import (
	Empresa,
	Persona,
	Escala,
	Cargo,
	Departamento,
	Rac,
	Formulacion,
	Empleado,
	Variable,
	ElementoPago2,
	PagoEmpleado2,
	Prenomina,
	Educacion,
	Familia,
	

	)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('cod_empresa', 'nombre','usuario', 'fecha_creacion', 'fecha_update')
	search_fields = ('cod_empresa', 'nombre')



@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
	list_display = ('cod_escala', 'escala', 'grado', 'paso', 'sueldo', 'cod_empresa')
	ordering = ('escala',)
	list_editable = ('sueldo',)

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	list_display = ('cod_cargo', 'cod_escala', 'des_cargo', 'cod_empresa')
	ordering = ('cod_escala',)
	list_editable = ('des_cargo','cod_escala')

     
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('cod_departamento', 'descripcion', 'cod_empresa')
	ordering = ('descripcion',)
	list_editable = ('descripcion',)

@admin.register(Rac)
class RacAdmin(admin.ModelAdmin):
	list_display = ('cod_rac','cod_departamento','cod_empresa')



@admin.register(Formulacion)
class FormulacionAdmin(admin.ModelAdmin):
	list_display = ('cod_formula','formula','cod_empresa',)





 	

@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
	list_display = ('cod_variable','descripcion','monto')






	



class PagoEmpleado2Inline(admin.TabularInline):
    model = PagoEmpleado2
    extra = 1
class EmpleadoAdmin(admin.ModelAdmin):
	list_display = ('pk','nombre','apellido','cedula',) 
	inlines = (PagoEmpleado2Inline,)

class ElementoPago2Admin(admin.ModelAdmin):
	inlines = (PagoEmpleado2Inline,)

admin.site.register(Empleado, EmpleadoAdmin)

admin.site.register(ElementoPago2, ElementoPago2Admin)

admin.site.register(PagoEmpleado2)



class FamiliaInline(admin.StackedInline):
    model = Familia
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('cedula',('nombre_1','nombre_2'),('apellido_1','apellido_2'),'fecha_nacimiento')
        }),
    )


#(('cedula', 'apellido_1','nombre_1'),('apellido_2','nombre_2'),('fecha_nacimiento',),)
class EducacionInline(admin.StackedInline):
    model = Educacion
    extra = 1
    fieldsets = (
        (None, {
            'fields': (('titulo', 'finalizado'),('inicio',),('fin',),'aptitudes')
        }),
    )
	


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	list_display = ['cod_solicitud', 'cod_empresa', 'nombre_1', 'cedula', 'apellido_1', 'status','cargo_opt',]
	ordering = ['status','cod_solicitud',]
	list_filter = ['status',]
	search_fields = ['nombre_1', 'cedula','cod_solicitud','cargo_opt']
	inlines = [EducacionInline,FamiliaInline]
	radio_fields = {'status': admin.HORIZONTAL}
	fieldsets = (
        (None, {
			'classes': ('extrapretty','wide'),
            'fields': ('status',)
        }), ('Datos Personales', {
			'classes': ('extrapretty','wide'),
			'fields': ('cedula',('nombre_1','nombre_2'),('apellido_1','apellido_2'),'fecha_nacimiento',('edad','genero'))

		}), ('Contacto',{
			'classes': ('extrapretty','wide'),
            'fields': (('email','telf'),'ocupacion','cargo_opt')

		})
    )
	
#'classes': ('collapse',),

	




# class PersonaAdmin(TabbedModelAdmin):
#     model = Persona
#     tab_overview = (
#          (None, {
#              'fields': ('cedula', 'status', ('nombre_1','apellido_1'),('nombre_2','apellido_2'),'cod_empresa',
# 		 	'fecha_nacimiento','edad','ocupacion','cargo_opt','email','telf','genero')
#          } ),
		
   
#     )    

#     tab_familia = (
        
#        FamiliaInline,
	   
      
#     )
#     tab_educacion = (
#         EducacionInline,
#     )

#     tabs = [
# 		('Persona', tab_overview),
#         ('Familia', tab_familia),
#         ('Educacion', tab_educacion),
#     ] 
	
	

# admin.site.register(Persona, PersonaAdmin)

@admin.register(Prenomina)
class PrenominaAdmin(admin.ModelAdmin):
	filter_horizontal=('pagos_empleados',)
	#extra = 1
	list_display = ('pk','tipo',)
	# date_hierarchy para prenomina o para pagos?
	#prepopulate



# class NominaSummaryAdmin(admin.ModelAdmin):
# 	def changelist_view(self, request, extra_context:None):
# 		date_hierarchy = 'fecha_inicio'
# 		response = super().changelist_view(request, extra_context)
# 		try:
# 			qs = response.context_data['cl'].queryset
# 		except (AttributeError, KeyError):
# 			return response
# 			metrics = {
# 			'total': Sum('pagos_empleados__monto'),
# 			}
# 		response.context_data['summary'] = list(
# 			qs.values('pagos_empleados__monto').annotate(**metrics).order_by('-pagos_empleados')
# 			)
# 		response.context_data['summary_total'] = dict (
# 			qs.aggregate(**metrics)
# 			)
# 		return response



# admin.site.register(NominaSummary)
# 	#


# @admin.register(Prenomina)
# class PrenominaAdmin(admin.ModelAdmin):
# 	list_display = ('pk','descripcion')
#  	search_fields = ['descripcion']
# 	filter_horizontal = ('pagos_empleados',)


# @admin.register(Empleado)
# class EmpleadoAdmin(admin.ModelAdmin):
#  	list_display = ('cod_empleado','cod_rac')

# @admin.register(PagoEmpleado)
# class PagoEmpleadoAdmin(admin.ModelAdmin):
# 	search_fields = ['elementopago']
#	filter_horizontal = ('empleado',)

#admin.site.register(PagoEmpleado, PagoEmpleadoAdmin)


#@admin.register(ElementoPago)
#class ElementoPagoAdmin(admin.ModelAdmin):
 #	list_display = ('cod_elemento_pago','descripcion','cod_formula')
 #	search_fields = ['descripcion']
	#filter_horizontal = ('empleado',)
