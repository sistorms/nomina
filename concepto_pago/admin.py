from django.contrib import admin
from .models import Variable, Formulacion, ElementoPago, PagoEmpleado
# Register your models here.

@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    pass

@admin.register(Formulacion)
class FormulacionAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Count('cod_solicitud'),
            'total_sales': Sum('cod_solicitud'),
            
        }

        response.context_data['summary'] = list(
            qs
            .values('status')
            .annotate(**metrics)
            .order_by('-status')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        ) 
        return response


@admin.register(ElementoPago)
class ElementoPagoAdmin(admin.ModelAdmin):
    pass
@admin.register(PagoEmpleado)
class PagoEmpleadoAdmin(admin.ModelAdmin):
    pass