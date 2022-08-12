from django.db import models

# Create your models here.

class Tarjeta(models.Model):
    numero_tarjeta = models.IntegerField(max_length=20 ,verbose_name="numero_tarjeta")
    cvv = models.IntegerField(max_length=4 ,verbose_name= "cvv")
    fecha = models.DateField(auto_now_add=True, verbose_name="fecha")
    fecha_expiracion = models.DateField(verbose_name="fecha_expiracion")
