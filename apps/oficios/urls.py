from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('oficios_recebidos/<int:oficio_id>', views.oficio_recebido, name='oficio_recebido'),
    path('oficios_expedidos/<int:oficio_id>', views.oficio_expedido, name='oficio_expedido'),
    path('exibir_recebidos', views.exibir_recebidos, name='exibir_recebidos'),
    path('exibir_expedidos', views.exibir_expedidos, name='exibir_expedidos'),
    path('pesquisa_oficios', views.pesquisa_oficios, name='pesquisa_oficios'),
    path('lista_autoridades', views.lista_autoridades, name='lista_autoridades'),
    path('cadastra_autoridade', views.cadastra_autoridade, name='cadastra_autoridade'),
    path('autoridade/<int:autoridade_id>', views.autoridade, name='autoridade'),
    path('altera_autoridade/<int:autoridade_id>', views.altera_autoridade, name='altera_autoridade'),
    path('oficio_recebido/novo', views.novo_oficio_recebido_form, name='novo_oficio_recebido_form'),
    path('oficio_expedido/novo', views.novo_oficio_expedido_form, name='novo_oficio_expedido_form'),
    path('oficio/responder/<int:oficio_id>', views.responde_oficio, name='responde_oficio'),
    path('apaga_oficio_recebido/<int:oficio_id>', views.apaga_oficio_recebido, name='apaga_oficio_recebido'),
    path('apaga_oficio_expedido/<int:oficio_id>', views.apaga_oficio_expedido, name='apaga_oficio_expedido'),
    path('apaga_autoridade/<int:autoridade_id>', views.apaga_autoridade, name='apaga_autoridade'),
    path('atualiza_oficio_recebido/<int:oficio_id>', views.atualiza_oficio_recebido, name='atualiza_oficio_recebido'),
    path('atualiza_oficio_expedido/<int:oficio_id>', views.atualiza_oficio_expedido, name='atualiza_oficio_expedido'),
    path('renumera_oficios', views.renumera_oficios, name='renumera_oficios'),
    path('salva_oficio_resposta', views.salva_oficio_resposta, name='salva_oficio_resposta'),
]
