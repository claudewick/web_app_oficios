from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models.ReceivedOL import ReceivedOL, Authority
from .models.SentOL import SentOL
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    """Renderiza a página principal
    """
    return render(request, 'index.html')

def dashboard(request):
    """Renderiza o painel de controle do módulo de ofícios.
    """
    data_atual = date.today()
    oficios_ativos = ReceivedOL.objects.filter(status=True).order_by('received_in') 
    paginator = Paginator(oficios_ativos, 10)
    page = request.GET.get('page')
    oficios_por_pagina = paginator.get_page(page)
    dados = {
        "oficios_totais": oficios_ativos,
        "oficios": oficios_por_pagina,
        "data_atual": data_atual,
    }
    if request.user.is_authenticated:
        return render(request, 'oficios/dashboard.html', dados)
    else:
        return redirect('index')

def oficio(request, oficio_id):
    """Exibe todas as informações de um ofício
    """
    oficio = get_object_or_404(ReceivedOL, pk=oficio_id) 

    oficio_a_exibir = {
        'oficio': oficio
    }
    return render(request, 'oficios/oficio.html', oficio_a_exibir)

def buscar(request):
    oficios_buscados = ReceivedOL.objects.all()
    paginator = Paginator(oficios_buscados, 10)
    page = request.GET.get('page')
    oficios_por_pagina = paginator.get_page(page)
    if 'buscar' in request.GET:
        termo_a_buscar = request.GET['buscar']
        oficios_buscados = oficios_buscados.filter(ol_origin_id__icontains=termo_a_buscar)
    dados = {
        "oficios": oficios_por_pagina
    }
    return render(request, 'oficios/buscar.html', dados)

def novo_oficio(request):
    """Renderiza a página de cadastramento de novos ofícios
    recebidos e salva as informações no banco de dados.
    """
    if request.user.is_authenticated:
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
            status = request.POST['exige_resposta'] if 'exige_resposta' == True else False
            received_ol_number = define_numero_oficio(ReceivedOL)
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
                status=status,
                received_ol_number=received_ol_number,
                answer_ol=None,
            )
            oficio.save()
            messages.success(request, f'Ofício {received_ol_number} salvo com sucesso')
            return redirect('dashboard')
            
        autoridades = Authority.objects.all()
        dados = {
                'autoridades': autoridades
            }
        return render(request, 'oficios/novo_oficio.html', dados)
    else:
            return redirect('index')

def apaga_oficio(request, oficio_id):
    """Apaga o ofício selecionado do banco de dados
    """
    #TODO: incluir a possibilidade de apagar ofício expedido
    oficio = get_object_or_404(ReceivedOL, pk=oficio_id)
    oficio.delete()
    messages.success(request, f'Ofício {oficio.received_ol_number} apagado com sucesso.')
    return redirect('dashboard')

def altera_oficio(request, oficio_id):
    oficio = get_object_or_404(ReceivedOL, pk=oficio_id)
    autoridades = Authority.objects.all()
    oficio_a_editar = {
        'oficio': oficio,
        'autoridades': autoridades,
    }
    return render(request, 'oficios/altera_oficio.html', oficio_a_editar)

def atualiza_oficio(request):
    if request.method == 'POST':
        oficio_id = request.POST['oficio_id']
        oficio_alterado = ReceivedOL.objects.get(pk=oficio_id)
        #oficio_alterado.received_in = request.POST['received_in']
        #oficio_alterado.ol_date = request.POST['ol_date']
        oficio_alterado.ol_origin_id = request.POST['ol_origin_id']
        #oficio_alterado.authority = request.POST['authority']  
        oficio_alterado.lawsuit_number = request.POST['lawsuit_number']
        oficio_alterado.lawsuit_author = request.POST['lawsuit_author']
        oficio_alterado.author_doc_number = request.POST['author_doc_number']
        oficio_alterado.author_type = 2 if len(oficio_alterado.author_doc_number) == 14 else 1
        oficio_alterado.lawsuit_accused = request.POST['lawsuit_accused']
        oficio_alterado.accused_doc_number = request.POST['accused_doc_number']
        oficio_alterado.accused_type = 2 if len(oficio_alterado.accused_doc_number) == 14 else 1
        #oficio_alterado.deadline = request.POST['deadline']
        oficio_alterado.status = request.POST['exige_resposta'] if 'exige_resposta' == True else False
        oficio_alterado.save()
        return redirect('oficio', oficio_id)


def responde_oficio(request):
    pass

def define_numero_oficio(tipo_de_oficio):
    ano_corrente = date.today().year 
    if tipo_de_oficio == ReceivedOL:
        oficios = ReceivedOL.objects.filter(received_in__year=ano_corrente)
        numero = str(f'R-{len(oficios) + 1 }/{ano_corrente}')
    elif tipo_de_oficio == SentOL:
        oficios = SentOL.objects.filter(creation_date__year=ano_corrente)
        numero = str(f'E-{len(oficios) + 1 }/{ano_corrente}')
    return numero

def renumera_oficios(request):
    for ano in range(2000, date.today().year + 1):
        oficios_recebidos = ReceivedOL.objects.filter(received_in__year=ano)
        for contador in range(1, (len(oficios_recebidos) + 1)):
            oficio_alterado = ReceivedOL.objects.get(pk=oficios_recebidos[contador-1].id)
            received_ol_number = str(f'R-{contador}/{ano}')
            oficio_alterado.received_ol_number = received_ol_number
            oficio_alterado.save()
        oficios_enviados = SentOL.objects.filter(creation_date__year=ano)
        for contador in range(1, (len(oficios_enviados) + 1)):
            oficio_alterado = SentOL.objects.get(pk=oficios_enviados[contador -1].id)
            sent_ol_number = str(f'E-{contador}/{ano}')
            oficio_alterado.sent_ol_number = sent_ol_number
            oficio_alterado.save()
    return redirect('dashboard')