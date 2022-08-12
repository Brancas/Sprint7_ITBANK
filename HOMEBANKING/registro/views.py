from django.shortcuts import render
from HOMEBANKING.Templates import *
# Create your views here.
def registro_usuario(request):
    return render(request,'registro.html')