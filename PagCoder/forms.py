from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Producto_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    cantidad = forms.IntegerField()
    
class Usuario_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    email = forms.CharField(max_length=100)
    
class Proveedor_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    empresa = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}
