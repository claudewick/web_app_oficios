from django.shortcuts import render


def index(request):
    # TODO: criar estrutura que verifica se há ofícios pendentes de resposta
    # Usar essa estrutura pra renderizar as linhas da tabela
    return render(request, 'index.html')

def novo_oficio(request):
    return render(request, 'novo.html')