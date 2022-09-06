from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oficios_recebidos/<int:oficio_id>', views.oficio, name='oficio'),
    path('buscar', views.buscar, name='buscar'),
]
