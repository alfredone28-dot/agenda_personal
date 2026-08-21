from django.db import models

# Create your models here.
class cliente (models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nombre
class servicio (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    duracion_min = models.IntegerField(default=30)

    def __str__(self):
        return self.nombre