from django.contrib import admin
from Cliente import models

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id',"Apellido", 'Nombre', 'DNI', "FechaNacimiento", "telefono", "Email", "tipo_cliente", "sucursal"]
    list_filter = ['id',"Apellido", 'Nombre', 'DNI', "FechaNacimiento", "telefono", "Email", "tipo_cliente", "sucursal"]
    search_fields = ['id',"Apellido", 'Nombre', 'DNI', "FechaNacimiento", "telefono", "Email", "tipo_cliente", "sucursal"]
    
admin.site.register(models.Cliente, ClienteAdmin)