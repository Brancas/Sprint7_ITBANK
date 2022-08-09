from django.db import models

# Create your models here.


class Cliente(models.Model):
    Apellido = models.CharField(max_length=30, verbose_name='Apellido')
    Nombre = models.CharField(max_length=30, verbose_name='Nombre')
    DNI = models.IntegerField(verbose_name='DNI')
    FechaNacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    telefono = models.IntegerField(verbose_name='telefono')
    Email = models.EmailField(max_length=255, verbose_name='Email')

    def __str__(self):
        return self.Apellido


class Empleado(models.Model):
    Apellido = models.CharField(max_length=30, verbose_name='Apellido')
    Nombre = models.CharField(max_length=30, verbose_name='Nombre')
    DNI = models.IntegerField(verbose_name='DNI')
    FechaNacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    telefono = models.IntegerField(verbose_name='telefono')
    Email = models.EmailField(max_length=255, verbose_name='Email')

    def __str__(self):
        return self.Apellido


class Prestamo(models.Model):
    Tipo = models.CharField(max_length=255, verbose_name="Tipo")
    Fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")
    Total = models.IntegerField(verbose_name="Total")
    # cliente id foring key?

    def __str__(self):
        return self.Tipo
