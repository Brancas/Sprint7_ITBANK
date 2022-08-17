from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from Cliente.models import Cliente

class registroForm(ModelForm):
    class Meta:
        model=Cliente
        fields=('Apellido','Nombre','DNI','FechaNacimiento','telefono','Email')