from django.contrib import admin
from Movimiento import models

# Register your models here.


class MovimientoAdmin(admin.ModelAdmin):
    list_display = ['id', "fecha", 'categoria', 'descripcion',"importe","saldo", "cliente"]
    list_filter = ['id',"fecha", 'categoria', 'descripcion',"importe","saldo", "cliente"]
    search_fields = ['id',"fecha", 'categoria', 'descripcion',"importe","saldo", "cliente"]

admin.site.register(models.Movimiento, MovimientoAdmin)