from django.shortcuts import render, HttpResponse


def hellowold(request):
    return render(request, 'index.html')

