from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.models import User
from usuarios.views import dashboard
from .models.ReceivedOL import ReceivedOL, Authority
from .models.SentOL import SentOL
from datetime import date

def index(request):
    return render(request, 'index.html')

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
        return render(request, 'novo_oficio.html', dados)
    else:
            return redirect('index')

def apaga_oficio(request, oficio_id):
    oficio = get_object_or_404(ReceivedOL, pk=oficio_id)
    oficio.delete()
    return redirect('dashboard')

def altera_oficio(request, oficio_id):
    oficio = get_object_or_404(ReceivedOL, pk=oficio_id)
    autoridades = Authority.objects.all()
    oficio_a_editar = {
        'oficio': oficio,
        'autoridades': autoridades,
    }
    return render(request, 'altera_oficio.html', oficio_a_editar)

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
        oficio_alterado.save()
        return redirect('oficio', oficio_id)


def responde_oficio(request):
    pass

def define_numero_oficio(tipo_de_oficio, ano):
    ano_corrente = date.today().year if not ano else ano
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