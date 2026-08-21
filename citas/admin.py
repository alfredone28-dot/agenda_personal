from django.contrib import admin
from .models import cliente, servicio

# Register your models here.
@admin.register(servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'duracion_min')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono')
    search_fields = ('nombre',)
    ordering = ('nombre',)