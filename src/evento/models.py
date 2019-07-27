from django.db import models
from django.utils import timezone
from PIL import Image

class Interes(models.Model):
    interes = models.CharField(max_length=100)
    def __str__(self):
        return self.interes

class Tipo_participacion(models.Model):
    tipo_parti = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo_parti

class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    puesto = models.CharField(max_length=60)
    empresa = models.CharField(max_length=60)
    email = models.EmailField(max_length=70)
    telefono = models.IntegerField()
    intereses = models.ManyToManyField(Interes)
    participaciones = models.ForeignKey(Tipo_participacion, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=60, blank=True)
    horaRegistro = models.DateTimeField(default=timezone.now)
    asistencia = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Publicaciones(models.Model):
    nombre_expositor = models.CharField(max_length=100)

