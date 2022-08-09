from django.contrib import admin
from Cliente import models

# Register your models here.

class Cliente(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'DNI', "FechaNacimiento", "Telefono", "Email"]
    list_filter = ['id', 'nombre', 'DNI', "FechaNacimiento", "Telefono", "Email"]
    search_fields = ['id', 'nombre', 'DNI', "FechaNacimiento", "Telefono", "Email"]
    

admin.site.register(models.Cliente)
admin.site.register(models.Empleado)

