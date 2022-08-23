from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class ExtendedUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30,required=True)

    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name','password1','password2')
       
       
    # NO PODEMOS SOBREESCRIBIR LOS ATRIBUTOS DE LOS FORMULARIOS USANDO *USER CREATION FORM* DE ESTA MANERA.
    # ES MAS SENCILLO IMPLEMENTARLO UTILIZANDO LA LIBRERIA DJANGO-WIDGET-TWEAKS   
    '''
        widgets={
            "username": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "first_name": forms.TextInput(attrs={'class':'form-control'}),
            "last_name": forms.TextInput(attrs={'class':'form-control'}),
            "password1": forms.CharField(attrs={'class':'form-control'}),
            "password2": forms.CharField(attrs={'class':'form-control'}),
           


        } '''
    
    def save(self, commit = True):

        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location', 'age')
        widgets={
            "location": forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese la provincia donde vive'}),
            "age":forms.NumberInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese su edad'}),
        }