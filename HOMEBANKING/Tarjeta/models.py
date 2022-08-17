from django.db import models
from Tarjeta.choices import marca_tarjetas, tipo_tarjetas
from django.core.validators import MaxValueValidator, MinValueValidator
from Cliente.models import Cliente

# Create your models here.

class Tarjeta(models.Model):
    numero_tarjeta = models.CharField(max_length = 20,verbose_name="numero_tarjeta")
    cvv = models.IntegerField(validators=[MaxValueValidator(9999)],verbose_name= "cvv")
    fecha = models.DateField(auto_now_add=True, verbose_name="fecha")
    fecha_expiracion = models.DateField(verbose_name="fecha_expiracion")
    marca = models.CharField(max_length=2, choices=marca_tarjetas)
    tipo = models.CharField(max_length=2, choices=tipo_tarjetas)
    cliente = models.ForeignKey(Cliente,null= True, blank= True, on_delete = models.CASCADE)

    class Meta:
        verbose_name = "tarjeta"
        verbose_name_plural = "tarjetas"
        db_table = 'Tarjeta'

    def __str__(self):
        return str(self.numero_tarjeta)