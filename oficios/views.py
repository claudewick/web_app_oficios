from django.shortcuts import render, get_list_or_404, get_object_or_404

from oficios.models import Authority, ReceivedOL
from .models.ReceivedOL import ReceivedOL


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