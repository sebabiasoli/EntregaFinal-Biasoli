from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
      

class MiFormularioDeCreacionDeUsuarios(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)
    first_name = forms.CharField(label='Nombre', max_length=20)    
    last_name = forms.CharField(label='Apellido', max_length=20)  


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar']




class MiFormularioDeEdicionDeDatosDeUsuario(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', max_length=20)    
    last_name = forms.CharField(label='Apellido', max_length=20)  
    avatar = forms.ImageField(required=False)  
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']