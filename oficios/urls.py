from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oficios_recebidos/<int:oficio_id>', views.oficio, name='oficio'),
    path('buscar', views.buscar, name='buscar'),
    path('oficio/novo', views.novo_oficio, name='novo_oficio'),
    path('oficio/responder', views.responde_oficio, name='responde_oficio'),
    path('apaga_oficio/<int:oficio_id>', views.apaga_oficio, name='apaga_oficio'),
    path('altera_oficio/<int:oficio_id>', views.altera_oficio, name='altera_oficio'),
    path('atualiza_oficio', views.atualiza_oficio, name='atualiza_oficio'),
    path('renumera_oficios', views.renumera_oficios, name='renumera_oficios'),
]
