from django.urls import path
from . import views

urlpatterns = [
    path('listaLotes/', views.listaLotes, name='listaLotes'),
    path('listaLotes/nuevoLote/', views.nuevoLote, name='nuevoLote'),
    path('guardarLote/', views.guardarLote, name='guardarLote'),
    path('listaLotes/eliminarLote/<int:id>/', views.eliminarLote, name='eliminarLote'),
    path('editarLote/<int:id>/', views.editarLote, name='editarLote'),
    path('procesarEdicionLote/', views.procesarEdicionLote, name='procesarEdicionLote'),
]
