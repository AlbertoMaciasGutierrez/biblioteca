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

    VALORACION_CHOICES = [
        (0.0,0),
        (1.0,1),
        (2.0,2),
        (3.0,3),
        (4.0,4),
        (5.0,5),
        (6.0,6),
        (7.0,7),
        (8.0,8),
        (9.0,9),
        (10.0,10),
    ]
    


    fecha_publicacion = models.DateField()
    trailer = models.CharField(max_length=300)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=30,choices=CATEGORIAS_CHOICES,default='Acción')
    titulo = models.CharField(max_length=50)
    sinopsis = models.TextField()
    imagen = models.ImageField( upload_to = 'peliculas' ,verbose_name='Imagen', blank=True)
    actores = models.ManyToManyField(Actor, related_name='actores', blank=True)                          #"reloated_name =" : Parámetro para renombrar la relación
    valoracion = models.DecimalField(choices=VALORACION_CHOICES, default=0.0, decimal_places=1, max_digits=3)
    valoracionMedia =models.DecimalField(default=0.0, decimal_places=1, max_digits=3)
    numVotos = models.IntegerField(default=0)
    valoracionTotal = models.DecimalField(default=0.0, decimal_places=1, max_digits=10)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.titulo} - {self.fecha_publicacion.strftime('%Y')} - {self.director}"







    class Meta:
        verbose_name = "pelicula"
        verbose_name_plural = "peliculas"
        ordering = ['-fecha_publicacion']






