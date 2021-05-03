from django import forms
#from cuentas.models import UsuarioRegister
from .models import Pelicula, Director

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula
        fields = ('titulo','fecha_publicacion','trailer','categoria','director','sinopsis',)


class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = ('nombre','fecha_nacimiento','biografia',)



#class CustomUserForm(UsuarioRegister):
 #   pass       