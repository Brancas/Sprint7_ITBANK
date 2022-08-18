from django.shortcuts import render
from .forms import TransferenciaForm


# Create your views here.

def transferencia(request):
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
    return render(request, 'form.html', {'form': OBJ_transForm})