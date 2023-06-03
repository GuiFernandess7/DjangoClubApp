from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, 
                            password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was a error logging In"))
            return redirect('login')
    else:
        return render(request, 'auth/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, "You were Logged Out")
    return redirect('home')
