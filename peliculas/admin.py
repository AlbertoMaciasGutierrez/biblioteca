from django.contrib import admin
from .models import Director, Pelicula, Actor
from cuentas.models import Usuario



admin.site.register(Director)
admin.site.register(Pelicula)
admin.site.register(Actor)
