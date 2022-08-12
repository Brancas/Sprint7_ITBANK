from django.contrib import admin
from Sucursal import models

# Register your models here.
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['id',"numero_sucursal", 'nombre_sucursal', "direccion_sucursal",]
    list_filter = ['id',"numero_sucursal", 'nombre_sucursal', "direccion_sucursal",]
    search_fields = ['id',"numero_sucursal", 'nombre_sucursal', "direccion_sucursal",]

admin.site.register(models.Sucursal, SucursalAdmin)