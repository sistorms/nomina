"""nomina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from baton.autodiscover import admin 
from django.urls import path, include
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

# from sistema.views import (

# home_page,
# #  EMPRESA
# empresa_crear_view,
# empresa_update_view,
# empresa_borrar_view,



# # Persona
# persona_crear_view,
# persona_update_view,
# persona_borrar_view,


# # Escala
# escala_crear_view,
# escala_update_view,
# escala_borrar_view,


# # Cargo
# cargo_crear_view,
# cargo_update_view,
# cargo_borrar_view,

# # Departamento
# departamento_crear_view,
# departamento_update_view,
# departamento_borrar_view,





# # Rac
# rac_crear_view,
# rac_update_view,
# rac_borrar_view,


# # Empleado
# empleado_crear_view,
# empleado_update_view,
# empleado_borrar_view,


# # Variable
# variable_crear_view,
# variable_update_view,
# variable_borrar_view,

# # Formulacion
# formulacion_crear_view,
# formulacion_update_view,
# formulacion_borrar_view,

# # Prenomina

# prenomina_crear_view,
# pago_empleado2_crear_view,

# # DEPARTAMENTO
# departamento_crear_view,
# departamento_detallada_view,
# departamento_update_view,
# departamento_borrar_view,

# # TIPO DE ESCALA
# tipo_escala_crear_view,
# tipo_escala_detallada_view,
# tipo_escala_update_view,
# tipo_escala_borrar_view,


# # ESCALA DE SUELDO
# escala_sueldo_crear_view,
# escala_sueldo_detallada_view,
# escala_sueldo_update_view,
# escala_sueldo_borrar_view,

# # CARGOS
# cargos_crear_view,
# cargos_detallada_view,
# cargos_update_view,
# cargos_borrar_view,

# # VARIABLES
# variables_crear_view,
# variables_detallada_view,
# variables_update_view,
# variables_borrar_view,


# # Frecuencia Pago
# sub_frecuencia_pago_crear_view,
# sub_frecuencia_pago_detallada_view,
# sub_frecuencia_pago_update_view,
# sub_frecuencia_pago_borrar_view,

# # Parametro Nomina
# parametro_nomina_crear_view,
# parametro_nomina_detallada_view,
# parametro_nomina_update_view,
# parametro_nomina_borrar_view,

# # Parametro Nomina
# reclutamiento_crear_view,
# reclutamiento_detallada_view,
# reclutamiento_update_view,
# reclutamiento_borrar_view,

# # Registro Asignacion de Puestos
# asignacion_puesto_crear_view,
# asignacion_puesto_detallada_view,
# asignacion_puesto_update_view,
# asignacion_puesto_borrar_view,


# # Movimiento Personal
# movimiento_personal_crear_view,
# movimiento_personal_detallada_view,
# movimiento_personal_update_view,
# movimiento_personal_borrar_view,



urlpatterns = [
#    path('jet/', include('jet.urls', 'jet')),
#    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    #
    #path('admin/', admin.site.urls),

    # path('', home_page),
    # path('prenomina/<int:pk>/', prenomina_crear_view),
    

    # # # URLS  empresa #

    # path('empresa/', empresa_crear_view),
    # path('empresa/<int:pk>/editar/', empresa_update_view),
    # path('empresa/<int:pk>/borrar', empresa_borrar_view),
    
    # # # URLS  Personas #

    # path('persona/', persona_crear_view),
    # path('persona/<int:pk>/editar/', persona_update_view),
    # path('persona/<int:pk>/borrar', persona_borrar_view),


    # # # URLS  Escala #

    # path('escala/', escala_crear_view),
    # path('escala/<int:pk>/editar/', escala_update_view),
    # path('escala/<int:pk>/borrar', escala_borrar_view),


    # # # URLS  Cargo #

    # path('cargo/', cargo_crear_view),
    # path('cargo/<int:pk>/editar/', cargo_update_view),
    # path('cargo/<int:pk>/borrar', cargo_borrar_view),


    # # # URLS  Departamento #

    # path('departamento/', departamento_crear_view),
    # path('departamento/<int:pk>/editar/', departamento_update_view),
    # path('departamento/<int:pk>/borrar', departamento_borrar_view),


    # # # URLS  Rac #

    # path('rac/', rac_crear_view),
    # path('rac/<int:pk>/editar/', rac_update_view),
    # path('rac/<int:pk>/borrar', rac_borrar_view),

    # # # URLS  Empleado #

    # path('empleado/', empleado_crear_view),
    # path('empleado/<int:pk>/editar/', empleado_update_view),
    # path('empleado/<int:pk>/borrar', empleado_borrar_view),



    # # # URLS  Variables #

    # path('variable/', variable_crear_view),
    # path('variable/<int:pk>/editar/', variable_update_view),
    # path('variable/<int:pk>/borrar', variable_borrar_view),

    # # # URLS  Formulacion #

    # path('formulacion/', formulacion_crear_view),
    # path('formulacion/<int:pk>/editar/', formulacion_update_view),
    # path('formulacion/<int:pk>/borrar', formulacion_borrar_view),


    # # # URLS Departamento #
    # path('pago_empleado/', pago_empleado2_crear_view),
    # path('departamento/', departamento_crear_view),
    # path('departamento/<str:slug>/', departamento_detallada_view),
    # path('departamento/<str:slug>/editar/', departamento_update_view),
    # path('departamento/<str:slug>/borrar', departamento_borrar_view),

    # # URLS Tipo de Escala #

    # path('tipo_escala/', tipo_escala_crear_view),
    # path('tipo_escala/<str:slug>/', tipo_escala_detallada_view),
    # path('tipo_escala/<str:slug>/editar/', tipo_escala_update_view),
    # path('tipo_escala/<str:slug>/borrar', tipo_escala_borrar_view),

    # # URLS Tipo de Escala #

    # path('escala_sueldo/', escala_sueldo_crear_view),
    # path('escala_sueldo/<str:slug>/', escala_sueldo_detallada_view),
    # path('escala_sueldo/<str:slug>/editar/', escala_sueldo_update_view),
    # path('escala_sueldo/<str:slug>/borrar', escala_sueldo_borrar_view),

    # # URLS Cargos #

    # path('cargos/', cargos_crear_view),
    # path('cargos/<str:slug>/', cargos_detallada_view),
    # path('cargos/<str:slug>/editar/', cargos_update_view),
    # path('cargos/<str:slug>/borrar', cargos_borrar_view),

    # # URLS Variables #

    # path('variables/', variables_crear_view),
    # path('variables/<str:slug>/', variables_detallada_view),
    # path('variables/<str:slug>/editar/', variables_update_view),
    # path('variables/<str:slug>/borrar', variables_borrar_view),


    # # URLS Frecuencia Pago #

    # path('sub_frecuencia_pago/', sub_frecuencia_pago_crear_view),
    # path('sub_frecuencia_pago/<str:slug>/', sub_frecuencia_pago_detallada_view),
    # path('sub_frecuencia_pago/<str:slug>/editar/', sub_frecuencia_pago_update_view),
    # path('sub_frecuencia_pago/<str:slug>/borrar', sub_frecuencia_pago_borrar_view),

    # # URLS Parametro Nomina #

    # path('parametro_nomina/', parametro_nomina_crear_view),
    # path('parametro_nomina/<str:slug>/', parametro_nomina_detallada_view),
    # path('parametro_nomina/<str:slug>/editar/', parametro_nomina_update_view),
    # path('parametro_nomina/<str:slug>/borrar', parametro_nomina_borrar_view),
    
    #     # URLS Parametro Nomina #

    # path('reclutamiento/',reclutamiento_crear_view),
    # path('reclutamiento/<str:slug>/', reclutamiento_detallada_view),
    # path('reclutamiento/<str:slug>/editar/', reclutamiento_update_view),
    # path('reclutamiento/<str:slug>/borrar', reclutamiento_borrar_view),


    #     # URLS Parametro Registro asignacion de puesto #

    # path('asignacion_puesto/',asignacion_puesto_crear_view),
    # path('asignacion_puesto/<str:slug>/', asignacion_puesto_detallada_view),
    # path('asignacion_puesto/<str:slug>/editar/', asignacion_puesto_update_view),
    # path('asignacion_puesto/<str:slug>/borrar', asignacion_puesto_borrar_view),

    # # URLS Parametro Registro asignacion de puesto #

    # path('movimiento_personal/',movimiento_personal_crear_view),
    # path('movimiento_personal/<str:slug>/', movimiento_personal_detallada_view),
    # path('movimiento_personal/<str:slug>/editar/', movimiento_personal_update_view),
    # path('movimiento_personal/<str:slug>/borrar', movimiento_personal_borrar_view),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Sistema Nomina'
