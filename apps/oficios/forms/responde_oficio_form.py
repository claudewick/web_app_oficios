from dataclasses import fields
from django import forms
from django.forms import ModelForm
from ..models.SentOL import SentOL


class RespondeOficioForm(forms.ModelForm):

    class Meta:
        model = SentOL
        fields = ['creation_date', 'answer']
        widgets = {
            'creation_date': forms.DateInput(attrs={'class': "form-control col-12 col-lg-4", 'type':'date'}),
            'authority': forms.Select(attrs={'label': 'Autoridade Emitente', 'class': "form-control col-12 col-lg-9"}),
            'delivery_date_time': forms.DateTimeInput(attrs={'class': "form-control col-12 col-lg-4", 'type':'date'}),
        }