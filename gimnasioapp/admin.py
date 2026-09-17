from django.contrib import admin
from .models import Rutina
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    list_display = ('id_rutina', 'nombre_rutina', 'objetivo')
    list_filter = ('frecuencia_semanal',)

    
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


