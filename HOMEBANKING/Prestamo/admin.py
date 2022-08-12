from django.contrib import admin
from Prestamo import models

# Register your models here.

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['id',"Tipo", 'Fecha', "Total", "Cliente",]
    list_filter = ['id',"Tipo", 'Fecha', "Total", "Cliente",]
    search_fields = ['id',"Tipo", 'Fecha', "Total", "Cliente",]
    

admin.site.register(models.Prestamo, PrestamoAdmin)

