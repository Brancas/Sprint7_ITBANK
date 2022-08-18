from django.shortcuts import render

# Create your views here.
def main_cuenta(request):

    return render(request, 'main_cuenta.html')


def main_configuracion(request):
    
    return render(request, 'main_configuracion.html')

def main_actividad(request):
    
    return render(request, 'main_actividad.html')