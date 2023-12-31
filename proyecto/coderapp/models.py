from django.db import models

class Pelicula (models.Model):
    nombre = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    director = models.CharField(max_length=20)

class Libro (models.Model):
    nombre = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    escritor = models.CharField(max_length=20)

class Serie (models.Model):
    nombre = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    plataforma = models.CharField(max_length=20)
    cantidadDeCapitulos = models.IntegerField()


