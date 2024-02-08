from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def helloworld(request):
    all_products = Product.objects.all()

    return render(request, 'index.html', {'products': all_products})


def about_us(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You logged in successfully.')
            return redirect('home')
        else:
            messages.warning(request, 'Username or password is invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('home')
