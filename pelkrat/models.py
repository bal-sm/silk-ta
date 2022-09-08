from django.db import models

import uuid
from datetime import datetime

# ===================================
# Create your models here.

class AkunNominal(models.Model):
    koperasi = models.ForeignKey('dkoperasi.Koperasi', on_delete=models.CASCADE)
    input_date = models.DateField(default=datetime.now)
    akun = models.ForeignKey('dakun.Akun', on_delete=models.CASCADE)
    nominal = models.BigIntegerField()#max_length=11)
    tahun = models.IntegerField(default=2022)#temporary field until solution been found

    class Meta:
        ordering = ['koperasi', 'akun', 'input_date']
        unique_together = [['koperasi', 'akun', 'tahun']]

    def __str__(self):
        return f'{self.koperasi} ({self.input_date}), {self.akun} = {self.nominal:,}'

    def nama_akun(self):
        return self.akun.namanya3()

    def nomornya1(self):
        return self.akun.nomornya1()

    def nomornya2(self):
        return self.akun.nomornya2()
        
    def nomornya3(self):
        return self.akun.nomornya3()

    def namanyaaja(self):
        return self.akun.namanyaaja()

        
class TerakhirInput(models.Model):
    koperasi = models.ForeignKey('dkoperasi.Koperasi', on_delete=models.CASCADE)
    input_date = models.DateField(default=datetime.now)
    akun = models.ForeignKey('dakun.Akun', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['koperasi', 'input_date', 'akun']]

# -----------------------------------

''' ----------------------------------- ants(draft)

pindah ke ants_dkoperasi
class Profil_Koperasi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nama = models.CharField(max_length=50)

pindah ke ants_dakun
class Akun_akun_tansi(models.Model):
    Akun_tansi = models.CharField(primary_key=True, max_length=50)
    Nama_Jelas = models.CharField(max_length=50)
    Deskripsi = models.TextField(blank=True)
    Kode_1 = models.IntegerField()#max_length=1)
    Kode_2 = models.IntegerField()#max_length=3)
    Kode_3 = models.IntegerField()#max_length=3)

    class Meta:
        ordering = ['Kode_1', 'Kode_2', 'Kode_3', 'Akun_tansi']
--------------------------------------------- '''




# -----------------------------------------------------------ANTS OLD DRAFT

#class Template_Akun_tansi_Nominal(models.Model):
#    Akun_tansi = models.ForeignKey(Akun_akun_tansi, on_delete=models.CASCADE)
#    Nominal_Akun_tansi = models.IntegerField()#max_length=11)

#    class Meta:
#        managed = False

#class Rekap_per_Koperasi(models.Model):
#    Koperasi = models.ForeignKey('ants_dkoperasi.Profil_Koperasi', on_delete=models.CASCADE, unique_for_year='Tanggal_Input')
#    Akun_akun_tansi_Nominal = models.ManyToManyField(Template_Akun_tansi_Nominal)
#    Tanggal_Input = models.DateTimeField(default=datetime.now, blank=True)


'''
---------------------------------------------
wip models

class Profil_Koperasi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nama_Koperasi = 
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
---------------------------------------------

---------------------------------------------
draft models

class Profil_Koperasi(models.Model):
    id (Primary_Key)
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
---------------------------------------------

----------------------------------------------------------------------------
yang ditunjukin ke darman
Profil_Koperasi
UUID Username Password Nama_Koperasi Jenis_Koperasi

Template_Akun
Akun Nama_Akun Deskripsi_Akun Bab Subbab Subsubbab Jenis Koperasi
aset Aset Aset adalah sesuatu yang dimiliki oleh suatu koperasi 1 0 0 Riil
aset_lancar Aset Lancar Aset lancar adalah ... 1 1 0 Riil
aset_lancar_kas Kas Kas adalah uang 1 1 1 Riil

Nominal_Akun
UUID Tahun Akun Nominal_Akun
1 2022 aset_lancar_kas 2.000.000
----------------------------------------------------------------------------
'''
# -------------------------------------------------------------------------
