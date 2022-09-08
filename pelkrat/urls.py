from django.urls import path
from . import views


urlpatterns = [
    path('input_tahun/', views.input_tahun, name='input_tahun'),
    path('input/<str:tahun>/', views.input_akun_code_1, name='input_akun_code_1'),
    path('input/<str:tahun>/<str:pk_1>/', views.input_akun_code_2, name='input_akun_code_2'),
    path('input/<str:tahun>/<str:pk_1>/<str:pk_2>/', views.input_akun_code_3, name='input_akun_code_3'),
    path('input/<str:tahun>/<str:pk_1>/<str:pk_2>/<str:pk_3>/', views.input_akun_specific, name='input_akun_specific'),
    path('input/<str:tahun>/<str:pk_1>/<str:pk_2>/<str:pk_3>/inputted/', views.inputted, name='inputted'),
    path('rekap/<str:tahun>/', views.rekapitulasi_input_akun, name='rekapitulasi_input_akun'),
    path('rekap/<str:tahun>/download/', views.download_hasil_input_laporan, name='download_hasil_input_laporan'),
]

# -----------------------------------

#    path('<str:nama_kop>/input/<str:Kod_1>.<str:Kod_2>.<str:Kod_3>/', views.input_akun, name='input_akun'),
#    path('<str:nama_kop>/input/cek', views.cek_terakhir_input_akun, name='cek_terakhir_input_akun'),

''' ----------------------------------- ants(draft)
urlpatterns = [
    path('<str:nama_kop>/, views.input_akun, name='laman_koperasi'),
]

urlpatterns = [
    path('input', views.input_akun, name='input_akun'),
    path('rekap', views.rekapitulasi_input_akun, name='rekapitulasi_input_akun'),
]

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
--------------------------------------------- '''