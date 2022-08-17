from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class ExtendUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'nombre', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.nombre = self.cleaned_data['nombre']
        user.apellido = self.cleaned_data['apellido']

        if commit:
            user.save()
        return user


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('DNI', 'FechaNacimiento', 'telefono')
