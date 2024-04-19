from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    def __str__(self):
        return f"Producto: {self.nombre}   Cantidad: {self.cantidad}"
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    def __str__(self):
        return f"Usuario: {self.nombre}   Email: {self.email}"
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=40)
    empresa = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return f"Usuario: {self.nombre}   Empresa:{self.empresa}   Email: {self.email}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True, blank=True)
    def __str__(self):
        return f"User: {self.user}   Imagen:{self.imagen}"