from django.db import models

class Alimento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    foto_alimento = models.ImageField(upload_to='Alimentos', null=True, blank=True)

