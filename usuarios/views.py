from email import message
import re
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from oficios.models import Authority, ReceivedOL
from oficios.models.ReceivedOL import ReceivedOL
from datetime import date

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_esta_vazio(nome):
            messages.error(request, "O campo nome não pode ficar em branco")
            return redirect('cadastro')
        if campo_esta_vazio(email):
            messages.error(request, "O campo email não pode ficar em branco")
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, "As senhas não são iguais")
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Usuário já cadastrado")
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, "Usuário já cadastrado")
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, "Usuário criado com sucesso")
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')
        

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_esta_vazio(email) or campo_esta_vazio(senha):
            messages.error(request, 'Os campos email e/ou senha não podem estar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'login realizado com sucesso')
            return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    data_atual = date.today()
    oficios_ativos = ReceivedOL.objects.filter(status=True).order_by('received_in') 
    dados = {
        "oficios": oficios_ativos,
        "data_atual": data_atual
    }
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def campo_esta_vazio(campo):
    return not campo.strip()