from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):                #Esto se hace por si se necesitan añadir más campos a la clase Usuario
    pass                                    #Se debe hacer al principio porque sino más adelante no se puede
                                            #"telefono = models.  "


