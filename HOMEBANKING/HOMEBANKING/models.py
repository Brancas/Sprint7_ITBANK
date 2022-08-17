from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DNI = models.IntegerField(verbose_name='DNI')
    FechaNacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    telefono = models.IntegerField(verbose_name='telefono')
    
    def __str__(self):
        return self.user.username