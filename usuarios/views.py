import re
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from oficios.models import Authority, ReceivedOL
from oficios.models.ReceivedOL import ReceivedOL

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print("O campo nome não pode ficar em branco")
            return redirect('cadastro')
        if not email.strip():
            print("O campo email não pode ficar em branco")
            return redirect('cadastro')
        if senha != senha2:
            print("As senhas não são iguais")
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print("Usuário já cadastrado")
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print("Usuário criado com sucesso")
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')
        

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            print('Os campos email e/ou senha não podem estar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
        if user is not None:
            auth.login(request, user)
            print('login realizado com sucesso')
            return redirect('dashboard')
    return render(request, 'usuarios/login.html')
def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    # TODO: criar estrutura que verifica se há ofícios pendentes de resposta
    # Usar essa estrutura pra renderizar as linhas da tabela
    oficios_ativos = ReceivedOL.objects.filter(status=True) 
    dados = {
        "oficios": oficios_ativos
    }
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def novo_oficio(request):
    return render(request, 'usuarios/novo_oficio.html')
