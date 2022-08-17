from django.db import models
from .choices import tipo_cuentas
from Cliente.models import Cliente

# Create your models here.


class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    balance = models.FloatField(verbose_name="balance")
    iban = models.CharField(verbose_name="iban", max_length=255)
    tipo_cuenta = models.CharField(choices=tipo_cuentas, max_length=3)

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        db_table = 'Cuenta'

    def __str__(self):
        return str(self.cliente)