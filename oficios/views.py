from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models.ReceivedOL import ReceivedOL, Authority
from datetime import date

def index(request):
    # TODO: criar estrutura que verifica se há ofícios pendentes de resposta
    # Usar essa estrutura pra renderizar as linhas da tabela
    oficios_ativos = ReceivedOL.objects.filter(status=True) 
    dados = {
        "oficios": oficios_ativos
    }
    return render(request, 'index.html', dados)

def oficio(request, oficio_id):
    oficio = get_object_or_404(ReceivedOL, pk=oficio_id) 

    oficio_a_exibir = {
        'oficio': oficio
    }
    return render(request, 'oficio.html', oficio_a_exibir)

def buscar(request):
    oficios_buscados = ReceivedOL.objects.all()
    if 'buscar' in request.GET:
        termo_a_buscar = request.GET['buscar']
        oficios_buscados = oficios_buscados.filter(ol_origin_id__icontains=termo_a_buscar)
    dados = {
        "oficios": oficios_buscados
    }
    return render(request, 'buscar.html', dados)

def novo_oficio(request):
    #TODO: criar pop-up informando o número do ofício
    #TODO: incluir seletor PF/PJ no form
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
            received_ol_number = define_numero_oficio()
            #TODO: incluir no form se o ofício requer resposta
            #status = 
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
            
        autoridades = Authority.objects.all()
        dados = {
                'autoridades': autoridades
            }
        return render(request, 'usuarios/novo_oficio.html', dados)
    else:
            return redirect('index')

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