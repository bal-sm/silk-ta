from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.
def home(request):
    context = {
        'nama_web' : 'SISTEM APLIKASI PELAPORAN KEUANGAN RAPAT ANGGOTA TAHUNAN KOPERASI DISKUK PROVINSI JAWA BARAT',
    }
    return render(request, 'home.html', context)

def welcome(request):

    return render(request, 'authenticate/welcome.html')

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, ("Gagal mengautentikasikan"))	
			return redirect('login')	


	else:
		return render(request, 'authenticate/login_user.html')

def logout_user(request):
	logout(request)
	return redirect('home')


def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('home')
	else:
		form = RegisterUserForm()

	return render(request, 'authenticate/register_user.html', {
		'form':form,
		})