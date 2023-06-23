from dataclasses import fields
from pyexpat import model
from tkinter.tix import Select
from django.core import validators
from django import forms
from .models import kritik_saran


class JenisForm(forms.ModelForm):
     class Meta:
        model = kritik_saran
        fields = ['jenis','pembahasan']
        widgets = { 
            'jenis': forms.Select(attrs={'class':'form-control'}),
            'pembahasan': forms.Textarea(attrs={'class':'form-control'}),
            
        }

class TeknisiForm(forms.ModelForm):
     class Meta:
        model = kritik_saran
        fields = [ 'status' ]
        widgets = { 
            'status': forms.Select(attrs={'class':'form-control'}),
            
        }


