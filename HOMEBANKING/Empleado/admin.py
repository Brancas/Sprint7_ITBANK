from django.contrib import admin
from Empleado import models

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['id',"Apellido", 'Nombre', 'DNI', "FechaNacimiento", "telefono", "Email", "sucursal"]
    list_filter = ['id',"Apellido", 'Nombre', 'DNI', "FechaNacimiento", "telefono", "Email", "sucursal"]
    search_fields = ['id',"Apellido", 'Nombre', 'DNI', "FechaNacimiento", "telefono", "Email", "sucursal"]
    

admin.site.register(models.Empleado, EmpleadoAdmin)