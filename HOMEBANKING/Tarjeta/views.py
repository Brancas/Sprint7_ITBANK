from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def main_tarjetas(request):

    return render(request, 'main_tarjetas.html')

