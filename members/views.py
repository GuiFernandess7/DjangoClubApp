from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

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

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username, password=password)
            auth_login(request, user)
            messages.success(request, ("Regitration Successfull"))
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'auth/register_user.html', {'form': form})