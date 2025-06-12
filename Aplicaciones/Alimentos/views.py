from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Alimento

# Listar alimentos
def listaAlimentos(request):
    alimentoListado = Alimento.objects.all()
    return render(request, "listaAlimentos.html", {'Alimentos': alimentoListado})

# Mostrar formulario para nuevo alimento
def nuevoAlimento(request):
    return render(request, "nuevoAlimento.html")

# Guardar alimento nuevo
def guardarAlimento(request):
    nombre = request.POST['nombre']
    tipo = request.POST['tipo']
    foto_alimento = request.FILES.get('foto_alimento')

    Alimento.objects.create(
        nombre=nombre,
        tipo=tipo,
        foto_alimento=foto_alimento
    )
    messages.success(request, "Alimento guardado exitosamente")
    return redirect('/listaAlimentos/')

# Eliminar alimento
def eliminarAlimento(request, id):
    alimentoEliminar = Alimento.objects.get(id=id)
    alimentoEliminar.delete()
    messages.success(request, "Alimento eliminado exitosamente")
    return redirect('/listaAlimentos/')

# Mostrar formulario para editar alimento
def editarAlimento(request, id):
    alimentoEditar = Alimento.objects.get(id=id)
    return render(request, "editarAlimento.html", {
        'alimentoEditar': alimentoEditar
    })

# Procesar edición de alimento
def procesarEdicionAlimento(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    tipo = request.POST['tipo']
    foto_alimento = request.FILES.get('foto_alimento')

    alimento = Alimento.objects.get(id=id)
    alimento.nombre = nombre
    alimento.tipo = tipo
    if foto_alimento:
        alimento.foto_alimento = foto_alimento
    alimento.save()

    messages.success(request, "Alimento actualizado exitosamente")
    return redirect('/listaAlimentos/')
