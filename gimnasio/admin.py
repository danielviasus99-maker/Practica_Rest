from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Gimnasio, Usuario, Ejercicio, Rutina, DetalleRutina, SesionEntrenamiento

admin.site.register(Gimnasio)
admin.site.register(Ejercicio)
admin.site.register(Rutina)
admin.site.register(DetalleRutina)
admin.site.register(SesionEntrenamiento)

    
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol', 'is_staff')
    list_filter = ('rol', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Agrega los campos personalizados al formulario de edición en el admin
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('telefono', 'direccion', 'rol')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Adicional', {'fields': ('telefono', 'direccion', 'rol')}),
    )

