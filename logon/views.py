from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def baseView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'templates/home.html')
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('home')
        
        else:
           messages.success(request, ("Invalid username or password"))
           return redirect('login')
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,'templates/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Loged out"))
    return redirect('login')