from django import forms

class TransferenciaForm(forms.Form):

    CNT_destino = forms.CharField(label = "CT_Destino", max_length = 50)

    TRF_monto = forms.IntegerField(label= "TRF_monto", min_value = 0)       #Aca faltaria analizar tipo de cliente 
                                                        #... y su monto maximo de transferencia sin avisar
    