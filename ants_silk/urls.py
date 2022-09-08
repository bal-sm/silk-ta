"""ants_silk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

#-------------------------------------
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('/home/')),
#    path('home/', include('django.contrib.auth.urls')),
    path('home/', include('dmember.urls')),
    path('koperasi/', include('dkoperasi.urls')),
    path('lkrat/', include('pelkrat.urls')),
    path('pdf_lkrat/', include('pdflkrat.urls')),
]
# -----------------------------------

''' ----------------------------------- ants(draft)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('input_koperasi', views.input_koperasi, name='input_koperasi'),
    path('form_input_akun', views.form_input_akun, name='form_input_akun'),
    path('rekapitulasi_input', views.rekapitulasi_input, name='rekapitulasi_input'),
]

--------------------------------------------- '''
