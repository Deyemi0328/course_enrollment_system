from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.

def Register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.saved()
            return redirect('login')
    else:
        form = RegisterForm()
    return render (request, 'register_page.html', { 'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (
            request, username = username, password = password
        )
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login_page.html', {'error':'invalid your access is denied...'})
    return render(request, 'login_page.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def homePage_view(request):
    return render(request, 'home_page.html')
        
