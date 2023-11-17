from django.db import models
from django.conf import settings
from django.utils import timezone

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    valoracion = models.CharField(max_length=200)
    descripcion = models.TextField()
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(default=timezone.now)
       

    def publish(self):
        self.save()

    def __str__(self):
        return self.titulo