from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo', views.novo_oficio, name='novo_oficio'),
]
