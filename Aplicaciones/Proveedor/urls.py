from django.urls import path
from . import views

urlpatterns = [
    # Proveedores
    path('listaProveedor/', views.listaProveedor, name='listaProveedores'),
    path('listaProveedor/nuevoProveedor/', views.nuevoProveedor, name='nuevoProveedor'),
    path('guardarProveedor/', views.guardarProveedor, name='guardarProveedor'),
    path('eliminarProveedor/<int:id>/', views.eliminarProveedor, name='eliminarProveedor'),
    path('editarProveedor/<int:id>/', views.editarProveedor, name='editarProveedor'),
    path('procesarEdicionProveedor/', views.procesarEdicionProveedor, name='procesarEdicionProveedor'),
]
