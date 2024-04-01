from django import forms

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