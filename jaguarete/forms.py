from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class Register(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):   
        model = User
        fields = ['username', 'email', 'password1', 'password2']        
        
        # help_texts= { k:"" for k in fields }
        # email_address = forms.CharField(max_length=50)
        # user_name = forms.CharField(max_length=50)
        # password = forms.CharField(max_length=50)