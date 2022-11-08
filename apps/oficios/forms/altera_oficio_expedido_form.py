from dataclasses import fields
from django import forms
from django.forms import ModelForm
from ..models.SentOL import SentOL


class AlteraOficioExpedidoForm(forms.ModelForm):

    class Meta:
        model = SentOL
        exclude = ['author_type', 'accused_type', 'created_at', 'updated_at', 'sent_ol_number', 'answer_to_ol', 'status']
        widgets = {
            'delivery_date_time': forms.DateTimeInput(attrs={'class': "form-control col-12 col-lg-4", 'type': 'datetime-local'}),
            'creation_date': forms.DateInput(attrs={'class': "form-control col-12 col-lg-4"}),
            'authority': forms.Select(attrs={'label': 'Autoridade Emitente', 'class': "form-control col-12 col-lg-9"}),
        }

