from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
        else:
            messages.error(request, 'An error occured during registration')
            return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in as {username}')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')
