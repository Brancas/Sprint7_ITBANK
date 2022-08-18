from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template, context
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

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
    