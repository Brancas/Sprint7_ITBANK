from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page(request):

    return render(request, 'index.html')

def main_app(request):

    return render(request, 'main.html')