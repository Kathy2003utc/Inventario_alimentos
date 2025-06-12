from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    pdf_certificado_sanitario = models.FileField(upload_to='Proveedores', null=True, blank=True)

    def __str__(self):
        return self.nombre
