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
    appellidoP = models.CharField(max_length=60)
    appellidoM = models.CharField(max_length=60)
    puesto = models.CharField(max_length=60)
    empresa = models.CharField(max_length=60)
    email = models.EmailField(max_length=70)
    telefono = models.IntegerField()
    intereses = models.ManyToManyField(Interes)
    participaciones = models.ForeignKey(Tipo_participacion, on_delete=models.CASCADE)
    horaRegistro = models.DateTimeField(default=timezone.now)
    asistencia = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Publicaciones(models.Model):
    nombre_expositor = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos')
    titulo_exposicion = models.CharField(max_length=100)
    resumen = models.CharField(max_length=900)

    def __str__(self):
        return self.titulo_exposicion

class AutoresRelevantes(models.Model):
    nombre_expositor = models.CharField(max_length=100)
    fotografia = models.ImageField(upload_to='autores')
    def __str__(self):
        return self.nombre_expositor

class TextoAdicional(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=100)
    def __str__(self):
        return self.titulo

class dns(models.Model):
    sitio = models.CharField(max_length=1000)

    def __str__(self):
        return self.sitio

class Saludo(models.Model):
    persona = models.CharField(max_length=1000)

    def __str__(self):
        return self.persona