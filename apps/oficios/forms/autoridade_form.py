from dataclasses import fields
from django import forms
from django.forms import ModelForm
from ..models.Authority import Authority

class AutoridadeForm(forms.ModelForm):

    class Meta:
        model = Authority
        exclude = ['status', 'created_at', 'updated_at']
        #widgets = {        }