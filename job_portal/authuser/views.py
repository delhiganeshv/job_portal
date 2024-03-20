from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from HR.models import Hr
# Create your views here.
def home(request):
    return render(request,'home.html')
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if Hr.objects.filter(user=user).exists():
                return redirect('hrdash')
            return redirect('dash')
        else:
            msg = "InValid Username or Password"
            return render(request,'authuser/login.html',{'msg':msg})
    return render(request,'authuser/login.html')


def candidateregister(request):
    return render(request,'authuser/candidate_register.html')

def hrregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 
        if password != cpassword:
            msg = "Password did't match"
            return render(request,'authuser/hr_register.html',{'msg':msg})
        user = User.objects.create_user(username=username, email=email, password=password)
        Hr(user=user).save()
        login(request, user) 
        return redirect('hrdash') 

    return render(request,'authuser/hr_register.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 
        if password != cpassword:
            msg = "Password did't match"
            return render(request,'authuser/hr_register.html',{'msg':msg})
        user = User.objects.create_user(username=username, email=email, password=password)
        
        login(request, user) 
        return redirect('dash')
    return render(request,'authuser/candidate_register.html')


def logoutUser(request):
    logout(request)
    return redirect('login')