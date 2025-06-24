from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar_estudiante, name='registrar'),
    path('reporte/', views.reporte_academico, name='reporte'),
    path('listado/', views.listado_estudiantes, name= 'listado_estudiantes'),
    path('listado_reportes/', views.listado_reportes, name= 'listado_reportes'),
    path('eliminarEstudiante/<int:estudiante_id>/',views.eliminar_estudiante,     name='eliminar_estudiante'),
    path('eliminar_reporte/<int:reporte_id>/',views.eliminar_reporte, name='eliminar_reporte'),
    path('editar_estudiante/<int:estudiante_id>/', views.editar_estudiante, name='editar_estudiante'),
    path('editar_reporte/<int:reporte_id>/', views.editar_reporte, name='editar_reporte'),
    path('exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('exportar/excel/', views.exportar_excel, name='exportar_excel'),
]
