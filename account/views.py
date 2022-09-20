#from urllib import request
from django.shortcuts import render
from django.contrib import messages


def login (request):
    return render(request, 'account/login.html')

def cadastro (request):
    print(request.POST)
    messages.success(request, 'Olá mundo')
    return render(request, 'account/cadastro.html')

def dashboard (request):
    return render(request, 'account/dashboard.html')
