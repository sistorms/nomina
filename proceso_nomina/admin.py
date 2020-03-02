from django.contrib import admin

# Register your models here.
from .models import Prenomina, Nomina,PrenominaSummary



@admin.register(Prenomina)
class PrenominaAdmin(admin.ModelAdmin):
    pass

@admin.register(PrenominaSummary)
class PrenominaSummaryAdmin(admin.ModelAdmin):
    actions = False
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False



@admin.register(Nomina)
class NominaAdmin(admin.ModelAdmin):
    pass
