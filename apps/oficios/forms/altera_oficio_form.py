from dataclasses import fields
from django import forms
from django.forms import ModelForm
from ..models.ReceivedOL import ReceivedOL


class AlteraOficioForm(forms.ModelForm):

    class Meta:
        model = ReceivedOL
        exclude = ['author_type', 'accused_type', 'received_ol_number', 'answer_ol', 'created_at', 'updated_at']
        widgets = {
            'received_in': forms.DateInput(attrs={'class': "form-control col-12 col-lg-4"}),
            'ol_date': forms.DateInput(attrs={'class': "form-control col-12 col-lg-4"}),
            'authority': forms.Select(attrs={'label': 'Autoridade Emitente', 'class': "form-control col-12 col-lg-9"}),
            'deadline': forms.DateInput(attrs={'class': "form-control col-12 col-lg-4"}),
        }

