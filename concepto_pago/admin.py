from django.contrib import admin
from .models import Variable, Formulacion, ElementoPago, PagoEmpleado
from django.db.models import Count  
# Register your models here.

@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    pass

@admin.register(Formulacion)
class FormulacionAdmin(admin.ModelAdmin):
    pass



@admin.register(ElementoPago)
class ElementoPagoAdmin(admin.ModelAdmin):
    pass
@admin.register(PagoEmpleado)
class PagoEmpleadoAdmin(admin.ModelAdmin):
    pass