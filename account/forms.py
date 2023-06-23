from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import Profile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','password1','password2')

class profilForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ['no_telpon','pendidikan_terakhir','jurusan']
        widgets = { 
            'no_telpon': forms.TextInput(attrs={'class':'form-control'}),          
            'pendidikan_terakhir': forms.TextInput(attrs={'class':'form-control'}),          
            'jurusan': forms.TextInput(attrs={'class':'form-control'}),          
        }

class informasiForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

        widgets = { 
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }


