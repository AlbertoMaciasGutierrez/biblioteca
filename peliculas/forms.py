
from django import forms
from .models import Pelicula, Director, Actor

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula
        fields = ('titulo','fecha_publicacion','pais','duracion','trailer','categoria','director','sinopsis','imagen','actores',)

    #nombre = forms.TextInput()
    #fecha_nacimiento = forms.DateInput()
    #biografia = forms.TextInput()
    #imagen = forms.ClearableFileInput()



    actores = forms.ModelMultipleChoiceField(
        queryset=Actor.objects.all(),
        widget=forms.CheckboxSelectMultiple
    ) 

class VotacionForm(forms.ModelForm):
    
    class Meta:
        model = Pelicula
        fields = ('valoracion',)


class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = ('nombre','fecha_nacimiento','pais','biografia','imagen',)


class ActorForm(forms.ModelForm):

    class Meta:
        model = Actor
        fields = ('nombre','fecha_nacimiento','pais','biografia','imagen',)

 




      