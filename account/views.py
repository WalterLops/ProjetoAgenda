#from urllib import request
import email
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login (request):
    
    if request.method != 'POST':
        return render(request, 'account/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    
    user = auth.authenticate(request, username=usuario, password=senha)
    
    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'account/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login realizado com sucesso!')
        return redirect('dashboard')
    
def logout(request):
    auth.logout(request)
    return render(request, 'account/login.html')

def cadastro (request): 
    if request.method != 'POST': # se nada for postado
        return render(request, 'account/cadastro.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    
    if not nome or not sobrenome or not usuario or not senha or not senha2:
        messages.error(request, 'Todos os campos são obrigatórios!')
        return render(request, 'account/cadastro.html')
    
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'account/cadastro.html')
    
    if len(usuario) < 6:
        messages.error(request, 'Usuário precisa ser maior que 6 caracteres')
        return render(request, 'account/cadastro.html')
    
    if len(senha) < 6:
        messages.error(request, 'Senha precisa ser maior que 6 caracteres')
        return render(request, 'account/cadastro.html')
    
    if senha != senha2:
        messages.error(request, 'As senhas não conferem')
        return render(request, 'account/cadastro.html')
    
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'O usuário já existe')
        return render(request, 'account/cadastro.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, 'O email já existe')
        return render(request, 'account/cadastro.html')
    
    messages.success(request, 'Usuário registrado com sucesso! Agora faça login.')
    
    user = User.objects.create_user(username=usuario, password=senha, email=email, first_name=nome, last_name=sobrenome)
    
    user.save()
    return redirect('login')
    
@login_required(redirect_field_name='login')
def dashboard (request):
    return render(request, 'account/dashboard.html')
