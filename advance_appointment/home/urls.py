from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('patient_form',views.patient_form,name='patient_form'),
    path('doctor_dash',views.doctor_dash,name='doctor_dash'),
]
