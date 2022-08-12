from django.contrib import admin
from Cuenta import models

# Register your models here.

class CuentaAdmin(admin.ModelAdmin):
    list_display = ['id',"cliente", 'balance', "iban", "tipo_cuenta",]
    list_filter = ['id',"cliente", 'balance', "iban", "tipo_cuenta",]
    search_fields = ['id',"cliente", 'balance', "iban", "tipo_cuenta",]
    

admin.site.register(models.Cuenta, CuentaAdmin)
