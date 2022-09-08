from django.db import models
from django.conf import settings

import uuid

from django.contrib.auth.models import User

class Type(models.Model):
    name = models.CharField(
        max_length=50)
    description = models.TextField(
        blank=True)
        
    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']

class Koperasi(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False)
    name = models.CharField(
        max_length=50,
        unique=True)
    description = models.TextField(
        blank=True)
    type = models.ManyToManyField(
        Type, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        
class KoperasiUser(models.Model):
    koperasi = models.OneToOneField(Koperasi, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.koperasi} by {self.user}'

#class Jenis_jenis_Riil(models.Model):
#    Jenis_jenis = models.TextChoices('Jenis_jenis', 'Jasa Konsumen Pemasaran Produsen')
#    Jenis = models.CharField(blank=True, choices=Jenis_jenis.choices, max_length=15)

#class Jenis_jenis_Simpan_Pinjam(models.Model):
#    Jenis_jenis = models.TextChoices('Jenis_jenis', 'Konvensional Syariah')
#    Jenis = models.CharField(blank=True, choices=Jenis_jenis.choices, max_length=15)

#class Profil_Koperasi(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    Nama = models.CharField(max_length=50)
#    Jenis_Riil = models.ManyToManyField(Jenis_jenis_Riil)
#    Jenis_Simpan_Pinjam = models.ForeignKey(Jenis_jenis_Simpan_Pinjam, null=True, on_delete=models.SET_NULL)

#class MySpecialUser(models.Model):
#    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    supervisor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='supervisor_of')

# -----------------------------------


#class Info_Sering(models.Model):
#    Nama = models.CharField(
#        max_length=50)
#    Deskripsi = models.TextField(
#        blank=True)

#    class Meta:
#        abstract = True
''' ----------------------------------- ants(draft)

wip models

class Profil_Koperasi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4`cobain versi 3`, editable=False)
    Username
    Password
    Nama_Koperasi
    Jenis_Koperasi


class Template_Akun_tansi(models.Model):
    Akun_tansi (Primary_Key)
    Nama_Akun_tansi 
    Deskripsi_Akun_tansi
    Tingkat_Akun_tansi_1
    Tingkat_Akun_tansi_2
    Tingkat_Akun_tansi_3
    Jenis_Koperasi

class Nominal_Akun_tansi(models.Model):
    id dari Profil_Koperasi
    Tahun (Primary_Key)
    Akun_tansi
    Nominal_Akun_tansi

----------------------------------- '''
