
from django import forms
from .models import Pelicula, Director, Actor

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula
        fields = ('titulo','fecha_publicacion','trailer','categoria','director','sinopsis','imagen',)
      


class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = ('nombre','fecha_nacimiento','biografia','imagen',)


class ActorForm(forms.ModelForm):

    class Meta:
        model = Actor
        fields = ('nombre','fecha_nacimiento','biografia','imagen','peliculas',)

    nombre = forms.TextInput()
    fecha_nacimiento = forms.DateInput()
    biografia = forms.TextInput()
    imagen = forms.ClearableFileInput()

    peliculas = forms.ModelMultipleChoiceField(
        queryset=Pelicula.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


      