from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def main_cuenta(request):

    return render(request, 'main_cuenta.html')


@login_required
def main_configuracion(request):
    
    return render(request, 'main_configuracion.html')


@login_required
def main_actividad(request):
    
    return render(request, 'main_actividad.html')