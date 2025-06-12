from django.db import models
from Aplicaciones.Alimentos.models import Alimento
from Aplicaciones.Proveedor.models import Proveedor

class Lote(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, related_name='lotes')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='lotes')
    fecha_vencimiento = models.DateField()
    cantidad = models.PositiveIntegerField(default=0) 
    pdf_factura = models.FileField(upload_to='Lotes', null=True, blank=True)

    def __str__(self):
        return f"Lote de {self.alimento.nombre} por {self.proveedor.nombre} (vence {self.fecha_vencimiento})"
