from dataclasses import fields
from pyexpat import model
from tkinter.tix import Select
from django.core import validators
from django import forms
from .models import kegiatan,absensi_kehadiran


class absensiForm(forms.ModelForm):
     class Meta:
        model = absensi_kehadiran
        fields = ['kegiatan','keterangan','status']
        widgets = { 
            'kegiatan': forms.Select(attrs={'class':'form-control'}),
            'keterangan': forms.Textarea(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            
        }

class rincianForm(forms.ModelForm):
     class Meta:
        model = absensi_kehadiran
        fields = ['kegiatan','status']
        widgets = { 
            'kegiatan': forms.Select(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            
        }

class dateForm(forms.ModelForm):
     class Meta:
        model = absensi_kehadiran
        fields = ['date_posted']
        widgets = { 
            'date_posted': forms.TextInput(attrs={'type':'date'}),          
        }



