from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignupForm


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


def signup_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Your account created successfully.')
            return redirect('home')

        # else:
        #     messages.error(request, 'There was a problem in your signup process')
        #     return redirect('signup')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def product(request, pk):
    product = Product.objects.filter(id=pk).first()
    return render(request, 'product.html', {'product': product})


def category(request, cat):
    cat = cat.replace('-', ' ')

    # try:
    category = Category.objects.get(name=cat)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'products': products, 'category': category})


    # except:
    #     messages.warning(request, 'No such a category')
    #     return redirect('home')
