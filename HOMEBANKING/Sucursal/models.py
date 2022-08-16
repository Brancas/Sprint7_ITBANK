from django.db import models

# Create your models here.

class Sucursal(models.Model):
    numero_sucursal = models.IntegerField(verbose_name='Numero Sucursal')
    nombre_sucursal = models.CharField(max_length=255, verbose_name='Nombre Sucursal')
    direccion_sucursal = models.CharField(max_length=255, verbose_name='Direccion Sucursal')

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        db_table = 'Sucursal'
    
    def __str__(self):
        return self.nombre_sucursal