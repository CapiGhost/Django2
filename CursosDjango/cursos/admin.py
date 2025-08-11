# cursos/admin.py
from django.contrib import admin
from .models import Curso
from .models import Actividad

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'duracion_horas', 'precio', 'activo', 'fecha_creacion')
    ordering = ('fecha_creacion',)
    search_fields = ('nombre', 'categoria')
    list_filter = ('activo', 'categoria', 'fecha_creacion')
    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'categoria', 'duracion_horas', 'precio', 'activo')
        }),
        ('Imágenes y fechas', {
            'fields': ('imagen', 'fecha_creacion'),
            'description': 'Campos automáticos y de imagen'
        }),
    )
    
    readonly_fields = ('fecha_creacion',)

class AdministrarActividades(admin.ModelAdmin):
    list_display=('clave', 'curso', 'act')
    search_fields=('clave', 'curso' 'created')
    date_hierarchy='created'
    readonly_fields=('created', 'clave')

admin.site.register(Actividad, AdministrarActividades)

