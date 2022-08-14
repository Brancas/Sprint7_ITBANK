"""HOMEBANKING URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


from Login.views import login_usuario
from registro.views import registro_usuario
from .views import landing_page, main_app
from Movimiento import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="Landing Page"),
    path('login', include('django.contrib.auth.urls')),
    path('login/', login_usuario),
    path('registrate/',registro_usuario),
    path('transferencia/', views.transferencia),
    path('main/', main_app),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
