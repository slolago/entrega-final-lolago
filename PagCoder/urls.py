from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("productos", views.productos, name="productos"),
    path("usuarios", views.usuarios, name="usuarios"),
    path("proveedores", views.proveedores, name="proveedores"),
    path("buscar_producto", views.buscar_producto, name="buscar_producto"),
    path("buscar", views.buscar, name="buscar"),
    path("lista_productos", views.lista_productos, name="lista_productos"),
    path("lista_usuarios", views.lista_usuarios, name="lista_usuarios"),
    path("lista_proveedores", views.lista_proveedores, name="lista_proveedores"),
    path("eliminar_producto/<int:id>", views.eliminar_producto, name="eliminar_producto"),
    path("eliminar_usuario/<int:id>", views.eliminar_usuario, name="eliminar_usuario"),
    path("eliminar_proveedor/<int:id>", views.eliminar_proveedor, name="eliminar_proveedor"),
    path("editar_producto/<int:id>", views.editar_producto, name="editar_producto"),
    path("editar_usuario/<int:id>", views.editar_usuario, name="editar_usuario"),
    path("editar_proveedor/<int:id>", views.editar_proveedor, name="editar_proveedor"),
    path("login", views.login_request, name="login_request"),
    path("registrar", views.registrar, name="registrar"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil"),
]
