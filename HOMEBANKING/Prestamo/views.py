from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from HOMEBANKING.forms  import ExtendUserCreationForm, UserProfileForm

# Create your views here.

@login_required
def main_prestamos(request):

    return render(request, 'main_prestamos.html')