import datetime

from django.db import models
from django.contrib.auth import get_user_model


                                                           

class Director(models.Model):
    biografia = models.TextField()
    fecha_nacimiento = models.DateField()
    nombre = models.CharField(max_length=50)             
                                                                                      
    def __str__(self):
        return self.nombre

                                                             




class Pelicula(models.Model):
    fecha_publicacion = models.DateField()
    trailer = models.CharField(max_length=300)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=30)
    titulo = models.CharField(max_length=50)
    sinopsis = models.TextField()

   

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.titulo} - {self.fecha_publicacion.strftime('%Y')} - {self.director}"

    @property
    def only_year(self):
        return self.fecha_publicacion.strftime('%Y')

