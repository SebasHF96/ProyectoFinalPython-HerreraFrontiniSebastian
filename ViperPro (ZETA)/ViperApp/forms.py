from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30)
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User  
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]  

#---------------------------------------------------------------------------------

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    sku = forms.IntegerField()
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=200)
    precio = forms.IntegerField()
    imagen = forms.ImageField()



#---------------------------------------------------------------------------------        

class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=15)
    email = forms.CharField(max_length=20)
