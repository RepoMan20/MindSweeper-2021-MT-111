from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        name_patient = request.POST['name_patient']
        email = request.POST['email']
        gender = request.POST['gender']

        x = Patients_appointment_Details(name_patient=name_patient,email=email,gender=gender)
    return render(request,'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        if User.objects.filter(username=username).exists():
            x=auth.authenticate(username=username,password= password)
            if x is not None:
                auth.login(request,x)
                return redirect('home')
                print('login failed')
            else:
                messages.info(request,'Email Id or Password not Matching')
                return redirect('login')
        else:
            t = User.objects.create_user(username = username,password = password)
            t.save()
            print('user created with username',username)
            return redirect('home')
    else:
        return render(request,'login.html')
            

def logout(request):
    
    auth.logout(request)
    return redirect('home')

def patient_form(request):
    return render(request, 'patient_form.html')

def doctor_dash(request):
    return render(request,'doctor_dash.html')