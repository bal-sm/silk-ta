from django.shortcuts import render, redirect, get_object_or_404

#from django.http import HttpResponse

from dkoperasi.models import Koperasi, KoperasiUser
from dakun.models import Akun
from .models import AkunNominal

from datetime import datetime

from django.db.models import Sum

#from .forms import NominalForm
# Create your views here.

def input_tahun(request):
    current_user = request.user
    koperasi_user = get_object_or_404(KoperasiUser, user=current_user)
    if request.method == "POST":
        tahun = request.POST.get('tahun')
        return redirect('input_akun_code_1', tahun)

    else:
        context = {
            'koperasi_user' : koperasi_user,
        }
        return render(request, 'input_tahun.html', context)

def input_akun_code_1(request, tahun):
    current_user = request.user
    koperasi_user = get_object_or_404(KoperasiUser, user=current_user)
    akun_code_1 = Akun.objects.filter(code_2=0, code_3=0).exclude(code_1=0).exclude(code_1=None).exclude(is_enabled=False)
    context = {
        'koperasi_user' : koperasi_user,
        'tahun' : tahun,
        'akun_code_1' : akun_code_1,
    }
    return render(request, 'input_akun_code_1.html', context)

def input_akun_code_2(request, tahun, pk_1):
    current_user = request.user
    koperasi_user = get_object_or_404(KoperasiUser, user=current_user)
    akun_code_1 = get_object_or_404(Akun, id=pk_1)
    akun_code_2 = Akun.objects.filter(code_1=akun_code_1.code_1, code_3=0).exclude(code_2=0).exclude(code_2=None).exclude(is_enabled=False)
    context = {
        'koperasi_user' : koperasi_user,
        'tahun' : tahun,
        'akun_code_1' : akun_code_1,
        'akun_code_2' : akun_code_2,
    }
    return render(request, 'input_akun_code_2.html', context)

def input_akun_code_3(request, tahun, pk_1, pk_2):
    current_user = request.user
    koperasi_user = KoperasiUser.objects.get(user=current_user)

    akun_code_1 = get_object_or_404(Akun, id=pk_1)
    akun_code_2 = get_object_or_404(Akun, id=pk_2)
    akun_code_3 = Akun.objects.filter(code_1=akun_code_1.code_1, code_2=akun_code_2.code_2).exclude(code_3=0).exclude(code_3=None).exclude(is_enabled=False)

    context = {
        'koperasi_user' : koperasi_user,
        'tahun' : tahun,
        'akun_code_1' : akun_code_1,
        'akun_code_2' : akun_code_2,
        'akun_code_3' : akun_code_3,
    }
    return render(request, 'input_akun_code_3.html', context)

def input_akun_specific(request, tahun, pk_1, pk_2, pk_3):
    current_user = request.user
    koperasi_user = KoperasiUser.objects.get(user=current_user)
    koperasi = koperasi_user.koperasi

    akun_code_1 = get_object_or_404(Akun, id=pk_1)
    akun_code_2 = get_object_or_404(Akun, id=pk_2)
    akun_code_3 = get_object_or_404(Akun, id=pk_3)

    if request.method == "POST":
        nominal_baru = request.POST.get('nominal')

        if AkunNominal.objects.filter(koperasi=koperasi, akun=akun_code_3, tahun=tahun).exists():
            pass
        else:
            AkunNominal.objects.create(koperasi=koperasi, akun=akun_code_3, tahun=tahun, nominal=0)

        if nominal_baru == '' :
            AkunNominal.objects.filter(koperasi=koperasi, akun=akun_code_3, tahun=tahun).delete()
        elif int(nominal_baru) == int(0):
            AkunNominal.objects.filter(koperasi=koperasi, akun=akun_code_3, tahun=tahun).delete()
        elif int(nominal_baru) != int(0):
            AkunNominal.objects.filter(koperasi=koperasi, akun=akun_code_3, tahun=tahun).update(nominal=nominal_baru, input_date=datetime.now())

        return redirect ('input_akun_code_3', tahun, pk_1, pk_2)

    else:
        if AkunNominal.objects.filter(koperasi=koperasi, akun=akun_code_3, tahun=tahun).exists():
            akunnominal_yang_ada = get_object_or_404(AkunNominal, koperasi=koperasi, akun=akun_code_3, tahun=tahun)
        else:
            akunnominal_yang_ada = None
    
        context = {
            'koperasi_user' : koperasi_user,
            'tahun' : tahun,
            'akun_code_1' : akun_code_1,
            'akun_code_2' : akun_code_2,
            'akun_code_3' : akun_code_3,
            'akunnominal_yang_ada' : akunnominal_yang_ada
        }
        return render(request, 'input_akun_specific.html', context)

def penyingkatan_display_akun(request, tahun):
    current_user = request.user
    koperasi_user = KoperasiUser.objects.get(user=current_user)
    koperasi = koperasi_user.koperasi

    tanggal_input = AkunNominal.objects.filter(koperasi=koperasi, tahun=tahun).latest('input_date')

    akun_1 = Akun.objects.get(code_1=1, code_2=0, code_3=0)
    akun_1_1 = Akun.objects.get(code_1=1, code_2=1, code_3=0)
    akun_1_2 = Akun.objects.get(code_1=1, code_2=2, code_3=0)

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=1, akun__code_2=1, tahun=tahun).exists():
        akun_1_1_ = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=1, akun__code_2=1, tahun=tahun)
        
        akun_1_1_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=1, akun__code_2=1, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_1_1_ = None
        akun_1_1_sum = 0

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=1, akun__code_2=2, tahun=tahun).exists():
        akun_1_2_ = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=1, akun__code_2=2, tahun=tahun)
        
        akun_1_2_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=1, akun__code_2=2, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_1_2_ = None
        akun_1_2_sum = 0

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=1, tahun=tahun).exists():
        akun_1_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=1, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_1_sum = 0

    akun_2 = Akun.objects.get(code_1=2, code_2=0, code_3=0)
    akun_2_1 = Akun.objects.get(code_1=2, code_2=1, code_3=0)
    akun_2_2 = Akun.objects.get(code_1=2, code_2=2, code_3=0)

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=2, akun__code_2=1, tahun=tahun).exists():
        akun_2_1_ = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=2, akun__code_2=1, tahun=tahun)
        
        akun_2_1_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=2, akun__code_2=1, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_2_1_ = None
        akun_2_1_sum = 0


    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=2, akun__code_2=2, tahun=tahun).exists():
        akun_2_2_ = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=2, akun__code_2=2, tahun=tahun)
        
        akun_2_2_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=2, akun__code_2=2, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_2_2_ = None
        akun_2_2_sum = 0

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=2, tahun=tahun).exists():
        akun_2_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=2, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_2_sum = 0

    akun_3 = Akun.objects.get(code_1=3, code_2=0, code_3=0)
    akun_3_1 = Akun.objects.get(code_1=3, code_2=1, code_3=0)

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=3, akun__code_2=1, tahun=tahun).exists():
        akun_3_1_ = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=3, akun__code_2=1, tahun=tahun)
        
        akun_3_1_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=3, akun__code_2=1, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_3_1_ = None
        akun_3_1_sum = 0

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=3, tahun=tahun).exists():
        akun_3_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=3, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_3_sum = 0


    akun_4 = Akun.objects.get(code_1=4, code_2=0, code_3=0)
    akun_4_1 = Akun.objects.get(code_1=4, code_2=1, code_3=0)
    akun_4_2 = Akun.objects.get(code_1=4, code_2=2, code_3=0)
    akun_4_3 = Akun.objects.get(code_1=4, code_2=3, code_3=0)

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, akun__code_2=1, tahun=tahun).exists():
        akun_4_1_ = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, akun__code_2=1, tahun=tahun)
        
        akun_4_1_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, akun__code_2=1, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_4_1_ = None
        akun_4_1_sum = 0

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, akun__code_2=2, tahun=tahun).exists():
        akun_4_2_ = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, akun__code_2=2, tahun=tahun)
        
        akun_4_2_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, akun__code_2=2, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_4_2_ = None
        akun_4_2_sum = 0

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, akun__code_2=3, tahun=tahun).exists():
        akun_4_3_ = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, akun__code_2=3, tahun=tahun)
        
        akun_4_3_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, akun__code_2=3, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_4_3_ = None
        akun_4_3_sum = 0

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, tahun=tahun).exists():
        akun_4_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=4, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_4_sum = 0

    akun_5 = Akun.objects.get(code_1=5, code_2=0, code_3=0)
    akun_5_1 = Akun.objects.get(code_1=5, code_2=1, code_3=0)
    akun_5_2 = Akun.objects.get(code_1=5, code_2=2, code_3=0)

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=5, akun__code_2=1, tahun=tahun).exists():
        akun_5_1_ = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=5, akun__code_2=1, tahun=tahun)
        
        akun_5_1_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=5, akun__code_2=1, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_5_1_ = None
        akun_5_1_sum = 0


    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=5, akun__code_2=2, tahun=tahun).exists():
        akun_5_2_ = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=5, akun__code_2=2, tahun=tahun)
        
        akun_5_2_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=5, akun__code_2=2, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_5_2_ = None
        akun_5_2_sum = 0

    if AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=5, tahun=tahun).exists():
        akun_5_sum = AkunNominal.objects.filter(koperasi=koperasi, akun__code_1=5, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_5_sum = 0

    if AkunNominal.objects.filter(koperasi=koperasi, tahun=tahun).exists():
        akun_sum = AkunNominal.objects.filter(koperasi=koperasi, tahun=tahun).aggregate(Sum('nominal'))
    else:
        akun_sum = 0

    context = {
        'koperasi_user' : koperasi_user,
        'koperasi' : koperasi,

        'tanggal_input' : tanggal_input,
        'tahun' : tahun,


        'akun_1' : akun_1,

        'akun_1_1' : akun_1_1,
        'akun_1_1_' : akun_1_1_,
        'akun_1_1_sum' : akun_1_1_sum,

        'akun_1_2' : akun_1_2,
        'akun_1_2_' : akun_1_2_,
        'akun_1_2_sum' : akun_1_2_sum,
        
        'akun_1_sum' : akun_1_sum,

        'akun_2' : akun_2,

        'akun_2_1' : akun_2_1,
        'akun_2_1_' : akun_2_1_,
        'akun_2_1_sum' : akun_2_1_sum,

        'akun_2_2' : akun_2_2,
        'akun_2_2_' : akun_2_2_,
        'akun_2_2_sum' : akun_2_2_sum,
        
        'akun_2_sum' : akun_2_sum,


        'akun_3' : akun_3,

        'akun_3_1' : akun_3_1,
        'akun_3_1_' : akun_3_1_,
        'akun_3_1_sum' : akun_3_1_sum,
        
        'akun_3_sum' : akun_3_sum,

        'akun_4' : akun_4,

        'akun_4_1' : akun_4_1,
        'akun_4_1_' : akun_4_1_,
        'akun_4_1_sum' : akun_4_1_sum,

        'akun_4_2' : akun_4_2,
        'akun_4_2_' : akun_4_2_,
        'akun_4_2_sum' : akun_4_2_sum,

        'akun_4_3' : akun_4_3,
        'akun_4_3_' : akun_4_3_,
        'akun_4_3_sum' : akun_4_3_sum,
        
        'akun_4_sum' : akun_4_sum,


        'akun_5' : akun_5,

        'akun_5_1' : akun_5_1,
        'akun_5_1_' : akun_5_1_,
        'akun_5_1_sum' : akun_5_1_sum,

        'akun_5_2' : akun_5_2,
        'akun_5_2_' : akun_5_2_,
        'akun_5_2_sum' : akun_5_2_sum,
        
        'akun_5_sum' : akun_5_sum,

        'akun_sum' : akun_sum
    }
    return context

def rekapitulasi_input_akun(request, tahun):
    
    return render(request, 'rekapitulasi_input_akun.html', penyingkatan_display_akun(request, tahun))

def download_hasil_input_laporan(request, tahun):
    current_user = request.user
    koperasi_user = KoperasiUser.objects.get(user=current_user)

    context = {
        'koperasi_user' : koperasi_user,
        'tahun' : tahun,
    }

    return render(request, 'download_hasil_input_laporan.html', context)
# -----------------------------------
    #akun_1_2 = Akun.objects.get(code_1=1, code_2=2, code_3=0)
    #akun_1_2_ = AkunNominal.objects.filter(akun(code_1=1, code_2=2))

def rekapitulasi_input_akun_daris(request, nama_kop):
    koperasi = Koperasi.objects.get(name=nama_kop)
    akun_template_all = Akun.objects.all()

    akun_all = AkunNominal.objects.filter(koperasi=koperasi).exclude(akun__code_3=0).exclude(akun__code_3=None)
    # definisi variabel berupa dictionary
    akun_all_bab1_title = {}
    akun_all_bab2_title = {}
    akun_all_bab1 = {}
    akun_all_bab2 = {}
    akun_all_bab3 = {}
    
    for i in range(1,6): # karena terdapat sebanyak 5 akun bab pertama (1,2,3,4,5)
        if akun_all.filter(akun__code_1=i).exists():
            akun_all_bab1_title[str(i)] = akun_template_all.get(code_1=i, code_2=0, code_3=0)
            akun_all_bab1[str(i)] = akun_all.filter(akun__code_1=i)

    for i,value in akun_all_bab1.items():
        for j in range(1,4): # karena terdapat sebanyak 4 akun bab kedua (1,2,3)
            if value.filter(akun__code_2=j).exists():
                akun_all_bab2_title[str(i)] = {}
                akun_all_bab2_title[str(i)][str(j)] = akun_template_all.get(code_1=i, code_2=j, code_3=0)
                akun_all_bab2[str(i)] = {}
                akun_all_bab2[str(i)][str(j)] = value.filter(akun__code_1=i, akun__code_2=j)

    for i,value_unused in akun_all_bab2.items():
        for j,value in value_unused.items():
            for k in range(1,30): # karena banyaknya nominal kemungkinan bertambah sesuai kebutuhan
                if value.filter(akun__code_3=k).exists():
                    akun_all_bab3[str(i)] = {}
                    akun_all_bab3[str(i)][str(j)] = {}
                    akun_all_bab3[str(i)][str(j)][str(k)] = value.get(akun__code_3=k)

    context = {
        'akun_all_bab1_title' : akun_all_bab1_title,
        'akun_all_bab2_title' : akun_all_bab2_title,
        'akun_all_bab1' : akun_all_bab1,
        'akun_all_bab2' : akun_all_bab2,
        'akun_all_bab3' : akun_all_bab3,
        'akun_all' : akun_all,
        'akun_template_all' : akun_template_all,
    }
    return render(request, 'rekapitulasi_input_akun.html', context)

def inputted(request, pk_1, pk_2, pk_3):
    current_user = request.user
    koperasi_user = get_object_or_404(KoperasiUser, user=current_user)
    koperasi = koperasi_user.koperasi

    akun_code_3 = get_object_or_404(Akun, id=pk_3)

    nominal_baru = request.POST.get('nominal')

    if AkunNominal.objects.filter(koperasi=koperasi, akun=akun_code_3).exists():
        pass
    else:
        AkunNominal.objects.create(koperasi=koperasi, akun=akun_code_3, nominal=0)

    if nominal_baru == '' :
        AkunNominal.objects.filter(koperasi=koperasi, akun=akun_code_3).delete()
    elif int(nominal_baru) == int(0):
        AkunNominal.objects.filter(koperasi=koperasi, akun=akun_code_3).delete()
    elif int(nominal_baru) != int(0):
        AkunNominal.objects.filter(koperasi=koperasi, akun=akun_code_3).update(nominal=nominal_baru, input_date=datetime.now())

    return redirect ('input_akun_code_3', pk_1, pk_2)

''' ----------------------------------- ants(draft)
def input_akun(request, nama_kop, Kod_1, Kod_2, Kod_3):
    Profil_Nama_Koperasi = Koperasi.objects.get(koperasi=nama_kop)
    Akun_tansi_1 = Akun.objects.get(code_1=Kod_1, code_2=0, code_3=0)
    Nama_Akun_tansi_1 = Akun_tansi_1.namanya1()
    Akun_tansi_2 = Akun.objects.get(code_1=Kod_1, code_2=Kod_2, code_3=0)
    Nama_Akun_tansi_2 = Akun_tansi_2.namanya2()
    Akun_tansi_3 = Akun.objects.get(code_1=Kod_1, code_2=Kod_2, code_3=Kod_3)
    Nama_Akun_tansi_3 = Akun_tansi_3.namanya3()
    Deskripsi_Akun_tansi = Akun_tansi_3.deskripsinya()
    context = {
        'nama1' : Nama_Akun_tansi_1,
        'nama2' : Nama_Akun_tansi_2,
        'nama3' : Nama_Akun_tansi_3 ,
        'desk1' : Deskripsi_Akun_tansi,
    }
    return render(request, 'input_akun.html', context)

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

def cek_koperasi(request):#, nama_koperasi_new_old):
    Nama_Koperasi_Baru_Lama = request.POST.get('nama_koperasi')

    if Profil_Koperasi.objects.filter(Nama=Nama_Koperasi_Baru_Lama).exists():
        return redirect('/'+str(Nama_Koperasi_Baru_Lama)+'/home/')
    else:
        Nama_Koperasi_Baru = Profil_Koperasi.objects.create(Nama=Nama_Koperasi_Baru_Lama)
        Nama_Koperasi_Baru.save()
        return redirect('/'+str(Nama_Koperasi_Baru_Lama)+'/home/')
--------------------------------------------- '''