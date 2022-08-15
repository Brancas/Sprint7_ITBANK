from django.db import models
from Cliente.models import Cliente
from .choices import tipo_prestamos

# Create your models here.


class Prestamo(models.Model):
    Tipo = models.CharField(choices=tipo_prestamos,
                            max_length=3, default='HTO')
    Fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")
    Total = models.IntegerField(verbose_name="Total")
    Cliente = models.ForeignKey(
        Cliente, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        db_table = 'Prestamo'

    def __str__(self):
        return self.Tipo
