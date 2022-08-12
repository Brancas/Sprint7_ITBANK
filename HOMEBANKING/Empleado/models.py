from django.db import models
from Sucursal.models import Sucursal


class Empleado(models.Model):
    Apellido = models.CharField(max_length=30, verbose_name='Apellido')
    Nombre = models.CharField(max_length=30, verbose_name='Nombre')
    DNI = models.IntegerField(verbose_name='DNI')
    FechaNacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    telefono = models.IntegerField(verbose_name='telefono')
    Email = models.EmailField(max_length=255, verbose_name='Email')
    sucursal = models.ForeignKey(
        Sucursal, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'

    def __str__(self):
        return self.Apellido