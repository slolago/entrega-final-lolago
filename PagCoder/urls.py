from django.urls import path
from . import views

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
]
