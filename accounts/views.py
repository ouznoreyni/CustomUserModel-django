from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserCreationForm, UserLoginForm
# Create your views here.
@login_required(login_url='accounts:login')
def dashboard(request):
    return render(request,'accounts/dashboard.html') 

def index(request):
    return render(request,'accounts/index.html') 

def registerView(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    if request.method == 'POST':
        email = request.POST.get('email')
        firstName = request.POST.get('prenom')
        lastName = request.POST.get('nom')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password and password2 and password==password2:
            UserProfile.objects.create_user(email=email, first_name=firstName, last_name=lastName, password=password)
            return  redirect('accounts:home')
        else:
           return render(request,'accounts/register.html')
    else:
        return render(request,'accounts/register.html') 

def loginView(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('accounts:home')
        return render(request,'accounts/login.html', {'form': form}) 
    else:
        form = UserLoginForm()
        return render(request,'accounts/login.html', {'form': form}) 



"""
    **********<-- view when i use {{as_p}} tag in the template-->*********


def registerView(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():

            form.save()
            return redirect('accounts:home')
        else:
           return render(request,'accounts/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request,'accounts/register.html', {'form': form}) 


def loginView(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('accounts:home')
        return render(request,'accounts/login.html', {'form': form}) 
    else:
        form = UserLoginForm()
        return render(request,'accounts/login.html', {'form': form}) 
"""


@login_required(login_url='accounts:login')
def logoutView(request):
    logout(request)
    return redirect('accounts:login')