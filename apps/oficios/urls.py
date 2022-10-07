from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('oficios_recebidos/<int:oficio_id>', views.oficio_recebido, name='oficio_recebido'),
    path('oficios_expedidos/<int:oficio_id>', views.oficio_expedido, name='oficio_expedido'),
    path('buscar_recebidos', views.buscar_recebidos, name='buscar_recebidos'),
    path('buscar_expedidos', views.buscar_expedidos, name='buscar_expedidos'),
    path('oficio/novo', views.novo_oficio_form, name='novo_oficio_form'),
    path('oficio_expedido/novo', views.novo_oficio_expedido_form, name='novo_oficio_expedido_form'),
    path('oficio/responder/<int:oficio_id>', views.responde_oficio, name='responde_oficio'),
    path('apaga_oficio/<int:oficio_id>', views.apaga_oficio, name='apaga_oficio'),
    path('atualiza_oficio_form/<int:oficio_id>', views.atualiza_oficio_form, name='atualiza_oficio_form'),
    path('renumera_oficios', views.renumera_oficios, name='renumera_oficios'),
    path('salva_oficio_resposta', views.salva_oficio_resposta, name='salva_oficio_resposta'),
    path('cadastra_autoridade', views.cadastra_autoridade, name='cadastra_autoridade'),
]
