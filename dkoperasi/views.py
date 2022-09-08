from django.shortcuts import render, redirect

from .models import Koperasi, KoperasiUser

from django.contrib.auth.models import User

def daftar_koperasi(request):
    current_user = request.user
    if KoperasiUser.objects.filter(user=current_user).exists():
        return redirect('input_tahun')
    elif request.method == "POST":
        name_new_old = request.POST.get('nama_koperasi')

        if Koperasi.objects.filter(name=name_new_old).exists():
            koperasi = Koperasi.objects.get(name=name_new_old)
            if KoperasiUser.objects.filter(koperasi=koperasi).exists():
                pass
            else:
                koperasi_user = KoperasiUser.objects.create(user=current_user, koperasi=koperasi)
                koperasi_user.save()
                return redirect('input_tahun')
        else:
            koperasi = Koperasi.objects.create(name=name_new_old)
            koperasi.save()
            koperasi_user = KoperasiUser.objects.create(user=current_user, koperasi=koperasi)
            koperasi_user.save()
            return redirect('input_tahun')
        
    else:
        return render(request, 'daftar_koperasi.html')

def welcome_koperasi(request):
    current_user = request.user
    koperasi_user = KoperasiUser.objects.get(user=current_user)
    koperasi = koperasi_user.koperasi
    context = {
        'koperasi' : koperasi
    }
    return render(request, 'welcome_koperasi.html', context)

#------------------------------------------------------

'''
def cek_koperasi(request):#, nama_koperasi_new_old):
    name_new_old = request.POST.get('nama_koperasi')

    if Koperasi.objects.filter(name=name_new_old).exists():
        return redirect('/'+str(name_new_old))
    else:
        Nama_Koperasi_Baru = Koperasi.objects.create(name=name_new_old)
        Nama_Koperasi_Baru.save()
        return redirect('/'+str(name_new_old))
'''