from dataclasses import fields
from pyexpat import model
from tkinter.tix import Select
from django.core import validators
from django import forms
from .models import survei
from django.forms import formset_factory

class jawabanForm(forms.ModelForm):
     class Meta:
        model = survei
        fields = ['nomor4']
        widgets = { 
            'nomor4': forms.RadioSelect,

        
        }




