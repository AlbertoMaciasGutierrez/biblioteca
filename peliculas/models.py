import datetime

from django.db import models
from django.contrib.auth import get_user_model


                                                           

class Director(models.Model):
    
    biografia = models.TextField()
    fecha_nacimiento = models.DateField()
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField( upload_to = 'directores' ,verbose_name='Imagen', blank=True)             
                                                                                      
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "director"
        verbose_name_plural = "directores"
        ordering = ['fecha_nacimiento']
                                                             

class Actor(models.Model):
    
    biografia = models.TextField()
    fecha_nacimiento = models.DateField()
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField( upload_to = 'actores' ,verbose_name='Imagen', blank=True)   



    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name = "actor"
        verbose_name_plural = "actores"
        ordering = ['-fecha_nacimiento']





class Pelicula(models.Model):
    
    CATEGORIAS_CHOICES = [
        ('Acción','Acción'),
        ('Aventura','Aventura'),
        ('Catástrofe','Catástrofe'),
        ('Ciencia Ficción','Ciencia Ficción'),
        ('Comedia','Comedia'),
        ('Documental','Documental'),
        ('Drama','Drama'),
        ('Fantasía','Fantasía'),
        ('Musical','Musical'),
        ('Suspense','Suspense'),
        ('Terror','Terror'),
        ('Infantil','Infantil'),
    ]



    fecha_publicacion = models.DateField()
    trailer = models.CharField(max_length=300)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=30,choices=CATEGORIAS_CHOICES,default='Acción')
    titulo = models.CharField(max_length=50)
    sinopsis = models.TextField()
    imagen = models.ImageField( upload_to = 'peliculas' ,verbose_name='Imagen', blank=True)
    actores = models.ManyToManyField(Actor, related_name='actores', blank=True)                          #"reloated_name =" : Parámetro para renombrar la relación
    

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.titulo} - {self.fecha_publicacion.strftime('%Y')} - {self.director}"

    @property
    def only_year(self):
        return self.fecha_publicacion.strftime('%Y')


    class Meta:
        verbose_name = "pelicula"
        verbose_name_plural = "peliculas"
        ordering = ['-fecha_publicacion']






