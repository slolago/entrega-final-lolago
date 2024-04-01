from django.shortcuts import render
from PagCoder.models import Producto
from PagCoder.models import Usuario
from PagCoder.models import Proveedor
from django.http import HttpResponse
from django.template import loader
from PagCoder.forms import Producto_formulario
from PagCoder.forms import Usuario_formulario
from PagCoder.forms import Proveedor_formulario

# Create your views here.

def home(request):
    return render(request, "index.html")

def productos(request):
    if request.method == "POST":
        mi_formulario = Producto_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data    
            producto = Producto(nombre=datos["nombre"], cantidad=datos["cantidad"])
            producto.save()
            return render(request, "productos.html")
    return render(request, "productos.html")

def usuarios(request):
    if request.method == "POST":
        mi_formulario = Usuario_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            usuario = Usuario(nombre=datos["nombre"], email=datos["email"])
            usuario.save()
        return render(request, "usuarios.html")
    return render(request, "usuarios.html")

def proveedores(request):
    if request.method == "POST":
        mi_formulario = Proveedor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            usuario = Proveedor(nombre=datos["nombre"], empresa=datos["empresa"], email=datos["email"])
            usuario.save()
            return render(request, "proveedores.html")
    return render(request, "proveedores.html")

def buscar_producto(request):
    
    return render(request, "buscar_producto.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        producto = Producto.objects.filter (nombre__icontains=nombre)
        return render(request, "resultado_busqueda.html", {"productos":producto})
    else:
        return HttpResponse("Ingrese el nombre del producto")
    
def lista_productos(request):
    productos = Producto.objects.all()
    dicc = {"producto":productos}
    plantilla = loader.get_template("lista_productos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    dicc = {"usuario":usuarios}
    plantilla = loader.get_template("lista_usuarios.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    dicc = {"proveedor":proveedores}
    plantilla = loader.get_template("lista_proveedores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def eliminar_producto(request, id):
    productos = Producto.objects.get(id=id)
    productos.delete()
    
    productos = Producto.objects.all()
    return render(request, "lista_productos.html", {"producto":productos})

def eliminar_usuario(request, id):
    usuarios = Usuario.objects.get(id=id)
    usuarios.delete()
    
    usuarios = Usuario.objects.all()
    return render(request, "lista_usuarios.html", {"usuario":usuarios})

def eliminar_proveedor(request, id):
    proveedores = Proveedor.objects.get(id=id)
    proveedores.delete()
    
    proveedores = Proveedor.objects.all()
    return render(request, "lista_proveedores.html", {"proveedor":proveedores})
    