from django.contrib import admin
from Cliente import models

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id',"Apellido", 'Nombre', 'DNI', "FechaNacimiento", "telefono", "Email"]
    list_filter = ['id',"Apellido", 'Nombre', 'DNI', "FechaNacimiento", "telefono", "Email"]
    search_fields = ['id',"Apellido", 'Nombre', 'DNI', "FechaNacimiento", "telefono", "Email"]
    

admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Empleado)

