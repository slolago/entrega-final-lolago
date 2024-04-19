from django.shortcuts import render
from PagCoder.models import Producto , Usuario , Proveedor, Avatar
from django.http import HttpResponse
from django.template import loader
from PagCoder.forms import Producto_formulario , Usuario_formulario , Proveedor_formulario , UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        return render(request, "index.html", {"url":avatares[0].imagen.url})
    else:    
        return render(request, "index.html")

def productos(request):
    if request.method == "POST":
        mi_formulario = Producto_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data    
            producto = Producto(nombre=datos["nombre"], cantidad=datos["cantidad"])
            producto.save()
            return render(request, "productos.html")
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        return render(request, "productos.html", {"url":avatares[0].imagen.url})
    else:
        return render(request, "productos.html")

@login_required
def usuarios(request):
    if request.method == "POST":
        mi_formulario = Usuario_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            usuario = Usuario(nombre=datos["nombre"], email=datos["email"])
            usuario.save()
        return render(request, "usuarios.html")
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "usuarios.html",{"url":avatares[0].imagen.url})

@login_required
def proveedores(request):
    if request.method == "POST":
        mi_formulario = Proveedor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            usuario = Proveedor(nombre=datos["nombre"], empresa=datos["empresa"], email=datos["email"])
            usuario.save()
            return render(request, "proveedores.html")
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "proveedores.html",{"url":avatares[0].imagen.url})


def buscar_producto(request):
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user.id)
        return render(request, "buscar_producto.html", {"url":avatares[0].imagen.url})
    else:
        return render(request, "buscar_producto.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        producto = Producto.objects.filter (nombre__icontains=nombre)
        return render(request, "resultado_busqueda.html", {"productos":producto})
    else:
        return render(request, "buscar_producto.html")
    
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "lista_productos.html", {"producto":productos})


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "lista_usuarios.html", {"usuario":usuarios})


def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "lista_proveedores.html", {"proveedor":proveedores})


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

  
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Producto_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            producto.nombre = datos["nombre"]
            producto.cantidad = datos ["cantidad"]
            producto.save()
            producto = Producto.objects.all()
            return render(request, "lista_productos.html", {"producto":producto})
    else:
        mi_formulario = Producto_formulario(initial={"nombre":producto.nombre , "cantidad":producto.cantidad})
    
    return render(request, "editar_producto.html", {"mi_formulario":mi_formulario, "productos":producto})


def editar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Usuario_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            usuario.nombre = datos["nombre"]
            usuario.email = datos ["email"]
            usuario.save()
            usuario = Usuario.objects.all()
            return render(request, "lista_usuarios.html", {"usuario":usuario})
    else:
        mi_formulario = Usuario_formulario(initial={"nombre":usuario.nombre , "email":usuario.email})
    
    return render(request, "editar_usuario.html", {"mi_formulario":mi_formulario, "usuarios":usuario})


def editar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Proveedor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            proveedor.nombre = datos["nombre"]
            proveedor.empresa = datos ["empresa"]
            proveedor.email = datos ["email"]
            proveedor.save()
            proveedor = Proveedor.objects.all()
            return render(request, "lista_proveedores.html", {"proveedor":proveedor})
    else:
        mi_formulario = Proveedor_formulario(initial={"nombre":proveedor.nombre , "empresa":proveedor.empresa , "email":proveedor.email})
    
    return render(request, "editar_proveedor.html", {"mi_formulario":mi_formulario, "proveedores":proveedor})


def login_request (request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario , password=contra)
            if user is not None:
                login(request , user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render (request, "inicio.html" , {"url":avatares[0].imagen.url, "mensaje":f"Bienvenido/a {usuario}"})
            else:
                return HttpResponse(f"Usuario incorrecto")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")
    
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

def registrar (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")
        else:
            return HttpResponse(f"ALGO FUE MAL :( {form}")
    else:
        form = UserCreationForm()
    return render(request, "registrar.html", {"form":form})

@login_required
def editarPerfil(request):

    usuario = request.user
    if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})