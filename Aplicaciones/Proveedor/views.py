from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Proveedor

# Listar proveedores
def listaProveedor(request):
    proveedorListado = Proveedor.objects.all()
    return render(request, "listaProveedor.html", {'Proveedores': proveedorListado})

# Mostrar formulario para nuevo proveedor
def nuevoProveedor(request):
    return render(request, "nuevoProveedor.html")

# Guardar proveedor nuevo
def guardarProveedor(request):
    nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    pdf_certificado_sanitario = request.FILES.get('pdf_certificado_sanitario')

    Proveedor.objects.create(
        nombre=nombre,
        telefono=telefono,
        pdf_certificado_sanitario=pdf_certificado_sanitario
    )
    messages.success(request, "Proveedor guardado exitosamente")
    return redirect('/listaProveedor/')

# Eliminar proveedor
def eliminarProveedor(request, id):
    proveedorEliminar = Proveedor.objects.get(id=id)
    proveedorEliminar.delete()
    messages.success(request, "Proveedor eliminado exitosamente")
    return redirect('/listaProveedor/')

# Mostrar formulario para editar proveedor
def editarProveedor(request, id):
    proveedorEditar = Proveedor.objects.get(id=id)
    return render(request, "editarProveedor.html", {
        'proveedorEditar': proveedorEditar
    })

# Procesar edición de proveedor
def procesarEdicionProveedor(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    pdf_certificado_sanitario = request.FILES.get('pdf_certificado_sanitario')

    proveedor = Proveedor.objects.get(id=id)
    proveedor.nombre = nombre
    proveedor.telefono = telefono
    if pdf_certificado_sanitario:
        proveedor.pdf_certificado_sanitario = pdf_certificado_sanitario
    proveedor.save()

    messages.success(request, "Proveedor actualizado exitosamente")
    return redirect('/listaProveedor/')
