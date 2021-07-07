from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.models import ModelForm 
from .models import Product

class NewProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'image_file': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):   
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        


