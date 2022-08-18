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

    return render(request, 'main_home.html')


def main_cajas(request):

    return render(request, 'main_cajas.html')

