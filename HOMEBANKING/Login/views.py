from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import Template,context

from django.shortcuts import render, redirect
from django.template import Template, context

from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import registroForm

# Create your views here.

admin_django="http://127.0.0.1:8000/admin/"

def registro_usuario(request):
    submitted=False
    if request.method == 'POST':
        form=registroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registro_usuario?submmited=True')
    else:
        form=registroForm
        if 'submitted' in request.GET:
            submitted=True
             

    return render(request,'registro.html', {'form':form,'submitted':submitted})



def login_usuario(request):
    # Con este if comprobamos que el usuario haya rellenado los formularios.
    # Si no los rellena solamente muestra la pagina.        
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("Bienvenido de nuevo."))
            
            if user.is_staff:
                return redirect('/admin')
            
            
            return redirect('main')

           
            # Redirect to a success page.

            
        else:
            username = request.POST['username']
            password = request.POST['password']
            messages.success(request, ("Usuario o contraseña invalidos."))
            
            
            return redirect(login_usuario)
            # Return an 'invalid login' error message.
            
    else:
        return render(request, 'login.html')
    
def logout(request):
    logout(request)
    
    return redirect('login')