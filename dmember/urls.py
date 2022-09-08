
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register'),
]