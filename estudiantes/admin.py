from django.apps import AppConfig
from django.contrib import admin


class EstudianteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estudiante'

    def ready(self):
       admin.site.site_header= "Panel de Administracion"
       admin.site.site_title= "Bienvenido al panel de Administración"
       admin.site.index_title= "Sistemas de reportes Académicos"
