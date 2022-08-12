from django.db import models

# Create your models here.

class Prestamo(models.Model):
    Tipo = models.CharField(max_length=255, verbose_name="Tipo")
    Fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")
    Total = models.IntegerField(verbose_name="Total")
    # cliente id foring key?

    def __str__(self):
        return self.Tipo