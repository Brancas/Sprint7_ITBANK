from django.shortcuts import render
from .forms import TransferenciaForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from HOMEBANKING.forms  import ExtendUserCreationForm, UserProfileForm


# Create your views here.


@login_required
def main_movimientos(request):

    return render(request, 'main_movimientos.html')

@login_required
def main_transferencia(request):
    """Esta funcion recibe la cuenta destino y el monto a transferir
    ! Falta que se conecte con la base de datos y modifique los campos correspondientes.
    ! Falta que autentifique el usuario y tome sus datos"""
    OBJ_transForm = TransferenciaForm
    #Validacion de metodo post
    if request.method == 'POST':
        #Traemos los datos
        OBJ_transForm = OBJ_transForm(data = request.POST)
        #Validacion de los datos
        if OBJ_transForm.is_valid():
            CNT_destino = request.POST.get('CT_Destino', '')
            TRF_monto = request.POST.get('TRF_monto', '')   
    
    return render(request, 'main_transferencia.html', {'form': OBJ_transForm})