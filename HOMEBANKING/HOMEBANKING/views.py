from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms  import ExtendUserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def landing_page(request):

    return render(request, 'index.html')


@login_required
def main_home(request):

    print(request.POST)
    return render(request, 'main_home.html')


@login_required
def main_cajas(request):

    return render(request, 'main_cajas.html')

