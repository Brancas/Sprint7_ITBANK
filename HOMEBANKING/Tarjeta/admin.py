from django.contrib import admin
from Tarjeta import models

# Register your models here.

class TarjetaAdmin(admin.ModelAdmin):
    list_display = ['id',"numero_tarjeta", 'cvv', 'fecha', "fecha_expiracion", "marca", "tipo",]
    list_filter = ['id',"numero_tarjeta", 'cvv', 'fecha', "fecha_expiracion", "marca", "tipo",]
    search_fields = ['id',"numero_tarjeta", 'cvv', 'fecha', "fecha_expiracion", "marca", "tipo",]


admin.site.register(models.Tarjeta, TarjetaAdmin)