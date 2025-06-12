from django.urls import path
from . import views

urlpatterns = [
    path('listaAlimentos/', views.listaAlimentos, name='listaAlimentos'),
    path('listaAlimentos/nuevoAlimento/', views.nuevoAlimento, name='nuevoAlimento'),
    path('guardarAlimento/', views.guardarAlimento, name='guardarAlimento'),
    path('eliminarAlimento/<int:id>/', views.eliminarAlimento, name='eliminarAlimento'),
    path('editarAlimento/<int:id>/', views.editarAlimento, name='editarAlimento'),
    path('procesarEdicionAlimento/', views.procesarEdicionAlimento, name='procesarEdicionAlimento'),
]
