from django.db import models
from .choices import tipo_clientes
from Sucursal.models import Sucursal
from django.contrib.auth.models import User
#from django.core.validators import validate_email
#from custom_validator.custom_validator import validate_length_dni, validate_length_phone_number

# Create your models here.


class Cliente(models.Model):
    Apellido = models.CharField(max_length=30, verbose_name='Apellido')
    Nombre = models.CharField(max_length=30, verbose_name='Nombre')
    DNI = models.IntegerField(verbose_name='DNI')
    FechaNacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    telefono = models.IntegerField(verbose_name='telefono')
    Email = models.EmailField(max_length=255, verbose_name='Email')
    tipo_cliente = models.CharField(
        max_length=1, choices=tipo_clientes, default='C')
    sucursal = models.ForeignKey(
        Sucursal, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'

    def __str__(self):
        return self.Apellido