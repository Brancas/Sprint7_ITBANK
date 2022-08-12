from django.db import models
from Cliente.models import Cliente

# Create your models here.

class Movimiento(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='fecha')
    categoria = models.CharField(max_length=255, verbose_name='categoria')
    descripcion = models.CharField(max_length=255, verbose_name='descripcion')
    importe = models.FloatField(verbose_name='importe')
    saldo = models.FloatField(verbose_name='saldo')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

    class Meta:
        verbose_name = ('Movimiento')
        verbose_name_plural = ('Movimientos')
        db_table = 'movimientos'

    def __str__(self):
        return self.categoria