from django import forms
from django.forms import ModelForm
from ..models.ReceivedOL import ReceivedOL

class NovoOficioForm(forms.ModelForm):

    class Meta:
        model = ReceivedOL
        exclude = ['author_type', 'accused_type', 'received_ol_number', 'answer_ol', 'created_at', 'updated_at']
        widgets = {
            'received_in': forms.DateInput(attrs={'label': 'Recebido Em',  'class': "form-control col-12 col-lg-3", 'type':'date'}),
            'ol_date': forms.DateInput(attrs={'class': "form-control col-12 col-lg-3", 'type':'date'}),
            'authority': forms.Select(attrs={'label': 'Autoridade Emitente', 'class': "form-control col-12 col-lg-6"}),
            'deadline': forms.DateInput(attrs={'class': "form-control col-12 col-lg-3", 'type':'date'}),
            'status': forms.CheckboxInput(attrs={'name': 'exige_resposta', 'value': 'on'}),
        }
