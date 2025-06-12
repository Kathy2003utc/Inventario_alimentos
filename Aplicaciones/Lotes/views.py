from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Lote, Alimento, Proveedor

# Listar todos los lotes
def listaLotes(request):
    lotes = Lote.objects.select_related('alimento', 'proveedor').all()
    return render(request, "listaLotes.html", {'Lotes': lotes})

# Mostrar formulario para crear un nuevo lote
def nuevoLote(request):
    alimentos = Alimento.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, "nuevoLote.html", {
        'Alimentos': alimentos,
        'Proveedores': proveedores
    })

# Guardar un nuevo lote
def guardarLote(request):
    if request.method == 'POST':
        alimento_id = request.POST['alimento_id']
        proveedor_id = request.POST['proveedor_id']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        cantidad = request.POST['cantidad']
        pdf_factura = request.FILES.get('pdf_factura')

        alimento = get_object_or_404(Alimento, id=alimento_id)
        proveedor = get_object_or_404(Proveedor, id=proveedor_id)

        Lote.objects.create(
            alimento=alimento,
            proveedor=proveedor,
            fecha_vencimiento=fecha_vencimiento,
            cantidad=cantidad,
            pdf_factura=pdf_factura
        )
        messages.success(request, "Lote guardado exitosamente")
        return redirect('/listaLotes/')
    else:
        messages.error(request, "Método no permitido")
        return redirect('/nuevoLote/')

# Eliminar lote
def eliminarLote(request, id):
    lote = get_object_or_404(Lote, id=id)
    lote.delete()
    messages.success(request, "Lote eliminado exitosamente")
    return redirect('/listaLotes/')

# Mostrar formulario para editar lote
def editarLote(request, id):
    lote = get_object_or_404(Lote, id=id)
    alimentos = Alimento.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, "editarLote.html", {
        'loteEditar': lote,
        'alimentos': alimentos,
        'proveedores': proveedores
    })

# Procesar la edición de lote
def procesarEdicionLote(request):
    if request.method == 'POST':
        id = request.POST['id']
        lote = get_object_or_404(Lote, id=id)

        alimento_id = request.POST['alimento_id']
        proveedor_id = request.POST['proveedor_id']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        cantidad = request.POST['cantidad']
        pdf_factura = request.FILES.get('pdf_factura')

        lote.alimento = get_object_or_404(Alimento, id=alimento_id)
        lote.proveedor = get_object_or_404(Proveedor, id=proveedor_id)
        lote.fecha_vencimiento = fecha_vencimiento
        lote.cantidad = cantidad

        if pdf_factura:
            lote.pdf_factura = pdf_factura

        lote.save()
        messages.success(request, "Lote actualizado exitosamente")
        return redirect('/listaLotes/')
    else:
        messages.error(request, "Método no permitido")
        return redirect('/listaLotes/')
