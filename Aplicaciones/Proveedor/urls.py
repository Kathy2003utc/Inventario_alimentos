from django.urls import path
from . import views

urlpatterns = [
    # Proveedores
    path('listaProveedores/', views.listaProveedores, name='listaProveedores'),
    path('listaProveedores/nuevoProveedor/', views.nuevoProveedor, name='nuevoProveedor'),
    path('guardarProveedor/', views.guardarProveedor, name='guardarProveedor'),
    path('eliminarProveedor/<int:id>/', views.eliminarProveedor, name='eliminarProveedor'),
    path('editarProveedor/<int:id>/', views.editarProveedor, name='editarProveedor'),
    path('procesarEdicionProveedor/', views.procesarEdicionProveedor, name='procesarEdicionProveedor'),
]
