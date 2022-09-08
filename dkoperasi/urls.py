
from django.urls import path
from . import views

urlpatterns = [
    path('daftar/', views.daftar_koperasi, name='daftar_koperasi'),
    path('welcome_koperasi', views.welcome_koperasi, name='welcome_koperasi'),
]

#    path('cek_koperasi/', views.cek_koperasi, name='cek_koperasi'),
#    path('', views.home, name='home'),
#    path('str:Nama(Koperasi)', views.laman_koperasi, name='laman_koperasi'),
# -----------------------------------

''' ----------------------------------- ants(draft)


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