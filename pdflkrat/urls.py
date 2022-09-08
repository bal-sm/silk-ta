
from django.urls import path
from . import views

urlpatterns = [
#    path('<str:nama_kop>/rekap/hasil/', views.hasil_input_akun, name='hasil_input_akun'),
    path('rekap/<str:tahun>/hasil/laporan_neraca/', views.laporan_neraca, name='laporan_neraca'),
    path('rekap/<str:tahun>/hasil/laporan_laba_rugi/', views.laporan_laba_rugi, name='laporan_laba_rugi'),
]