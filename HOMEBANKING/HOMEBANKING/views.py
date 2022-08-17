from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page(request):

    return render(request, 'index.html')

def main_home(request):

    return render(request, 'main_home.html')

def main_prestamos(request):

    return render(request, 'main_prestamos.html')

def main_movimientos(request):

    return render(request, 'main_movimientos.html')

def main_cajas(request):

    return render(request, 'main_cajas.html')

def main_tarjetas(request):

    return render(request, 'main_tarjetas.html')

def main_cuenta(request):

    return render(request, 'main_cuenta.html')