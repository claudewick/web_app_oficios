import re
from django.shortcuts import render, redirect
from django.contrib import auth
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
    oficios_ativos = ReceivedOL.objects.filter(status=True).order_by('received_in') 
    dados = {
        "oficios": oficios_ativos
    }
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def novo_oficio(request):
    #TODO: criar pop-up informando o número do ofício
    #TODO: incluir seletor PF/PJ no form
    if request.method == 'POST':
        received_in = request.POST['received_in']
        ol_date = request.POST['ol_date']
        ol_origin_id = request.POST['ol_origin_id']
        authority = request.POST['authority']  
        lawsuit_number = request.POST['lawsuit_number']
        lawsuit_author = request.POST['lawsuit_author']
        author_doc_number = request.POST['author_doc_number']
        author_type = 2 if len(author_doc_number) == 14 else 1
        lawsuit_accused = request.POST['lawsuit_accused']
        accused_doc_number = request.POST['accused_doc_number']
        accused_type = 2 if len(accused_doc_number) == 14 else 1
        deadline = request.POST['deadline']
        received_ol_number = define_numero_oficio()
        #TODO: incluir no form se o ofício requer resposta
        #status = 
        if request.user.is_authenticated:
            oficio = ReceivedOL.objects.create(
                received_in=received_in, 
                ol_date=ol_date, 
                ol_origin_id=ol_origin_id,
                authority_id=authority,
                lawsuit_number=lawsuit_number,
                lawsuit_author=lawsuit_author,
                author_type=author_type,
                author_doc_number=author_doc_number,
                lawsuit_accused=lawsuit_accused,
                accused_type=accused_type,
                accused_doc_number=accused_doc_number,
                deadline=deadline,
                received_ol_number=received_ol_number,
                answer_ol=None,
                status=True,
            )
            oficio.save()
            print(f'Ofício {received_ol_number} salvo com sucesso')
            return redirect('dashboard')
        else:
            return redirect('index')

    autoridades = Authority.objects.all()
    dados = {
        'autoridades': autoridades
    }
    return render(request, 'usuarios/novo_oficio.html', dados)

def compara_ano(ano_oficio):
    ano_corrente = date.today().year
    if ano_oficio == ano_corrente:
        return True
    else:
        return False

def define_numero_oficio():
    ano_corrente = date.today().year
    oficios = ReceivedOL.objects.filter(received_in__year=ano_corrente)
    numero = str(f'R-{len(oficios) + 1 }/{ano_corrente}')
    return numero