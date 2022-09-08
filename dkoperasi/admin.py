from django.contrib import admin

from .models import Type, Koperasi, KoperasiUser

# Register your models here.

admin.site.register(Type)
admin.site.register(Koperasi)
admin.site.register(KoperasiUser)