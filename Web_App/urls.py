"""
URL configuration for Web_App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path, include
from web.views.views import *
from web.views.views_api import *
from web.views.views_blog import *
from web.views.views_descargas import *
from web.views.views_tables import *
from django.views.generic import TemplateView
handler404 = custom_404_view
from ven911.urls import *
from seguridad_prevencion.urls import *
from junin.urls import *

#Se crean las rutas que se podran visitar en la aplicacion web.
urlpatterns = [
    # includes
    path('ven911/', include('ven911.urls')),
    path('seguridad_prevencion/', include('seguridad_prevencion.urls')),
    path('junin/', include('junin.urls')),

    # Admin
    path('alpha04/', admin.site.urls),
    path('logout/', logout, name='logout'),

    # BLOG
    path('', inicio, name="inicio"),
    path('informacion/', information,name='informacion'),
    path('salasituacional/', salasituacional,name='salasituacional'),
    path('brigadajuvenil/', brigadajuvenil,name='brigadajuvenil'),
    path('glp/', glp,name='glp'),
    path('operaciones-incendios/', operaciones_incendios,name='operaciones-inceidos'),
    path('drones/', drones,name='drones'),
    path('contacto/', contacto,name='contacto'),
    path('zoedan/', zoedan_tachira,name='zoedan_tachira'),
    path('proceso_captacion/', captacion,name='captacion'),
    path('blog_psicologia/', blog_psicologia,name='psicologia_inf'),
    path('blog_capacitacion/', blog_capacitacion,name='capacitacion_inf'),
    path('blog_prevencion/', blog_prevencion,name='prevencion_inf'),
    path('blog_serviciosmedicos/', blog_serviciosmedicos,name='serviciosmedicos_inf'),
    path('noticias/', noticias,name='noticias'),

    # SISTEMA
    path('login/', Home, name="home"),
    path('dashboard/', Dashboard,name='dashboard'),
    path('api/ultimo_procedimiento/', ultimo_procedimiento),
    path('personal/', View_personal, name='personal'),
    path("api/ultimo_personal/", ultimo_personal, name="ultimo_personal"),
    path('api/personal_comandante/', personal_primer_comandante, name='personal_comandante'),
    path('prueba/', Prueba),
    path('registros/', ver_registros, name='registros'),
    path('antecedentes/', Antecedentes, name='antecedentes'),

    # Mecanica
    path('dashboard_mecanica/', Dashboard_mecanica,name='dashboard_mecanica'),

    # SARP
    path('dashboard_sarp/', Dashboard_sarp,name='dashboard_sarp'),
    path('registros_sarp/', Registros_sarp, name='registros_sarp'),
    path('formularios_sarp/', Formularios_sarp, name='formularios_sarp'),
    path('registrar_dron/', registrar_drones, name="registrar_dron"),
    path('api/vuelos/', api_vuelos, name="api_vuelos"),  # API en formato JSON
    path('reporte/<str:id_vuelo>/', obtener_reporte, name='reporte'),
    path('editar_reporte/<str:id_vuelo>/', editar_reporte, name='obtener_reporte'),
    path("api/eliminar_vuelo/<str:id_vuelo>/", api_eliminar_vuelo, name="api_eliminar_vuelo"),
    path('api/estadisticas-misiones/', obtener_estadisticas_misiones, name="estadisticas-misiones"),
    path('api/ultimo_reporte/', obtener_ultimo_reporte),
    path('api/buscar_vuelo/<str:vuelo_id>/', buscar_vuelo_por_id, name='buscar_vuelo_por_id'),

    # Bienes Municipales
    path('dashboard_bienes/', Dashboard_bienes,name='dashboard_bienes'),
    path('inventario_bienes/', Inventario_bienes,name='inventario_bienes'),
    path('registro_bienes/', Registros_bienes,name='registro_inventario'),
    path('api/bienes/', listar_bienes, name='api_bienes'),
    path('reasignar-bien/', reasignar_bien, name='reasignar_bien'),
    path('cambiar-bien/', cambiar_estado_bienes, name='cambiar_estado_bien'),
    path('eliminar-bien/', eliminar_bien, name='eliminar_bien'),
    path('api/historial-bien/<str:bien_id>/', historial_bien_api, name='historial_bien_api'),
    path('api/verificar-identificador/', verificar_identificador, name='verificar_identificador'),

    # Unidades
    path('unidades/', View_Unidades, name='unidades'),

    path('conductores/', conductores, name='conductores'),
    path('agregar_conductores/', agregar_conductor, name='agregar_conductor'),
    path('conductores/<int:id>/editar/', editar_conductor, name='editar_conductor'),

    # API Endpoints
    path('api/conductores/', api_conductores, name='api_conductores'),
    path('api/conductores/<int:id>/', api_eliminar_conductor, name='api_eliminar_conductor'),

    path('formularioUnidades/', View_Form_unidades, name='formulario_unidades'),
    path('agregar_reportes/', agregar_reportes, name="agregar_reportes"),
    path('agregar_unidades/', agregar_unidades, name="agregar_unidades"),
    path('cambiar_estado/', cambiar_estado, name="cambiar_estado"),
    path('reasignar_division/', reasignar_division, name="reasignar_division"),
    path('obtener_info_unidad/<int:id>/', obtener_info_unidad, name="obtener_info_unidad"),
    path('mostrar_informacion/<int:id>/', mostrar_informacion, name="mostrar_informacion"),

    path("api/conteo_unidades/", contar_estados_unidades, name="conteo_unidades"),
    path("api/reportes_combustible/", contar_reportes_combustible, name="reportes_combustible"),
    path("api/reportes_lubricantes/", contar_reporte_lubricantes, name="reportes_lubricantes"),
    path("api/reportes_neumaticos/", contar_reporte_neumaticos, name="reportes_neumaticos"),
    path("api/reportes_reparaciones/", contar_reporte_reparaciones, name="reportes_reparaciones"),
    path("api/reportes_electricas/", contar_reporte_electricas, name="reportes_electricas"),
    path("api/reportes_cambio_repuestos/", contar_reporte_cambio_repuestos, name="reportes_cambio_repuestos"),
    path("api/reportes_colisiones_daños/", contar_reporte_colisiones_danos, name="reportes_colisiones_daños"),

    # Tablas
    path('tablageneral/', tabla_general, name="tabla_general"),
    path('procedimientos/', View_Procedimiento, name='view_procedimiento'),
    path('editar_procedimientos/', View_Procedimiento_Editar, name='view_procedimiento_editar'),
    path('estadisticas/', View_Estadisticas, name='view_estadisticas'),
    path('rescate/', View_Rescate, name='view_rescate'),
    path('operaciones/', View_Operaciones, name='view_operaciones'),
    path('prevencion/', View_Prevencion, name='view_prevencion'),
    path('prehospitalaria/', View_prehospitalaria, name='view_prehospitalaria'),
    path('grumae/', View_grumae, name='view_grumae'),
    path('capacitacion/', View_capacitacion, name='view_capacitacion'),
    path('enfermeria/', View_enfermeria, name='view_enfermeria'),
    path('serviciosmedicos/', View_serviciosmedicos, name='view_serviciosmedicos'),
    path('psicologia/', View_psicologia, name='view_psicologia'),

    # APIs
    path('api/procedimientos/<int:id>/', obtener_procedimiento, name='obtener_procedimiento'),
    path('api/meses/', obtener_meses, name='obtener_meses'),
    path('api/porcentajes/<str:periodo>/', obtener_porcentajes, name='api_porcentajes'),
    path('api/parroquias/', obtener_procedimientos_parroquias, name='obtener_parroquias'),
    path('api/divisiones/', obtener_divisiones, name='obtener_divisiones'),
    path('api/divisiones_estadisticas/', obtener_divisiones_estadistica, name='obtener_divisiones_estadistica'),
    path('api/generar_estadistica/', generar_resultados, name='generar_estadistica'),
    path('api/procedimientos_division/', api_procedimientos_division, name='procedimientos_division'),
    path('api/procedimientos_division_parroquia/', api_procedimientos_division_parroquias, name='procedimientos_division_parroquia'),
    path('api/procedimientos_tipo/', api_procedimientos_tipo, name='procedimientos_tipo'),
    path('api/procedimientos_tipo_horizontal/', api_procedimientos_bar_horizontales, name='procedimientos_tipo_horizontal'),
    path('api/procedimientos_tipo_parroquias/', api_procedimientos_tipo_parroquias, name='procedimientos_tipo_parroquias'),
    path('get_persona/<int:id>/', get_persona, name='get_persona'),
    path('editar_personal/', edit_personal, name='edit_personal'),
    path('api/procedimientos_tipo_detalles/', api_procedimientos_tipo_detalles, name='procedimientos_tipo_detalles'),
    path('instagram/', instagram_feed, name='instagram_feed'),
    path('api/obtener_informacion/<int:id>/', obtener_informacion_editar, name='obtener_informacion'),
    path('api/obtener_unidades/', api_unidades, name='obtener_unidades'),
    path('api/obtener_tipos_procedimientos/', api_tipos_procedimientos, name='obtener_tipos_procedimientos'),
    path('api/obtener_solicitante/', api_solicitantes, name='obtener_solicitante'),

    # Descargas
    path('descargar-excel_personal/', generar_excel_personal, name='descargar_excel_personal'),
    path('descargar-base-datos/', descargar_base_datos, name='descargar_base_datos'),

    # divisiones exportacion excel
    path('descargar-excel-capacitacion/', generar_excel_capacitacion, name='descargar_excel_capacitacion'),
    path('descargar-excel-psicologia/', generar_excel_psicologia, name='descargar_excel_psicologia'),
    path('descargar-excel-operaciones/', generar_excel_operaciones, name='descargar_excel_operaciones'),
    path('descargar-excel-grumae/', generar_excel_grumae, name='descargar_excel_grumae'),
    path('descargar-excel-prehospitalaria/', generar_excel_prehospitalaria, name='descargar_excel_prehospitalaria'),
    path('descargar-excel-serviciosmedicos/', generar_excel_serviciosmedicos, name='descargar_excel_serviciosmedicos'),
    path('descargar-excel-rescate/', generar_excel_rescate, name='descargar_excel_rescate'),
    path('descargar-excel-prevencion/', generar_excel_prevencion, name='descargar_excel_prevencion'),
    path('descargar-excel-enfermeria/', generar_excel_enfermeria, name='descargar_excel_enfermeria'),
    path('descargar-excel-operacional/', generar_excel_operacional, name='descargar_excel_operacional'),
    path('generar-excel-reportes-unidades/', generar_excel_reportes_unidades, name='generar_excel_reportes'),
    path('generar-excel-reportes-sarp/', generar_excel_reportes_sarp, name='generar_excel_sarp'),
    path('generar-excel-bienesmunicipales/', generar_excel_bienes_municipales, name='generar_excel_sarp'),


    # Urls Para el Area de Invenario de Unidades
    # Herramientas
    path('unidades_inventario/', herramienta_list, name='inventario_unidades'),
    path('herramientas/nueva/', herramienta_create, name='herramienta-create'),
    path('herramientas/<int:pk>/editar/', herramienta_update, name='herramienta-update'),
    
    # Asignaciones
    path('asignaciones/', asignacion_list, name='asignacion-list'),
    path('asignaciones/nueva/', asignacion_create, name='asignacion-create'),
    path('asignaciones/<int:pk>/devolver/', asignacion_devolver, name='asignacion-devolver'),
    
    # Inventarios
    path('inventarios/nuevo/', inventario_create, name='inventario-create'),
    path('inventarios/<int:pk>/', inventario_detail, name='inventario-detalle'),
    
    path('inventarios/', inventario_list, name='inventario-list'),
    path('inventarios/ajax/<int:pk>/', inventario_detail_ajax, name='inventario-detail-ajax'),

    # Reportes
    path('reportes/', reporte_inventario, name='reporte-inventario'),
]
