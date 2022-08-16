from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms  import ExtendUserCreationForm, UserProfileForm
# Create your views here.


def landing_page(request):

    return render(request, 'index.html')


def main_home(request):

    return render(request, 'nuevo_template/index.html')


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


def register(request):
    if request.method == 'POST':
        form = ExtendUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid:
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)

            return redirect('index')
    else:
        form = ExtendUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'register.html', context)

@ login_required
def home(request):
    return HttpResponse("Hola")