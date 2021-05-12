import os
from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import DetailView, DeleteView, CreateView, ListView, UpdateView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from .models import Pelicula, Director, Actor
from .forms import PeliculaForm, DirectorForm, ActorForm, VotacionForm   



class PeliculaListado(LoginRequiredMixin, ListView):             #Para ListView el nombre genérico para tener "objects.all()" es: "nombreModeloEnMinusculas"_list
    model = Pelicula                                             #Estos nombres se usan en los bucles for de los distintos templates de cada lista de objects
    template_name = 'peliculas/peliculas_list.html'              #En este caso se llama "pelicula_list"


class DirectorListado(LoginRequiredMixin, ListView):
    model = Director
    template_name = 'directores/director_list.html'



class ActorListado(LoginRequiredMixin, ListView):
    model = Actor
    template_name = 'actores/actor_list.html'




class PeliculaDetalles(LoginRequiredMixin, DetailView):
    model = Pelicula
    template_name = 'peliculas/peliculas_detail.html'


   
class DirectorDetalles(LoginRequiredMixin, DetailView):
    model = Director
    template_name = 'directores/director_detail.html'   

class ActorDetalles(LoginRequiredMixin, DetailView):
    model = Actor
    template_name = 'actores/actor_detail.html' 




class PeliculaNueva(LoginRequiredMixin, CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'peliculas/peliculas_edit.html'
    

    def get_success_url(self):
        return reverse('detallesPelicula',args=(self.object.id,))


class PeliculaEditar(LoginRequiredMixin, UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'peliculas/peliculas_edit.html'
    

    def get_success_url(self):
        return reverse('detallesPelicula',args=(self.object.id,))




class PeliculaEliminar(LoginRequiredMixin, DeleteView):
    model = Pelicula
    template_name = 'peliculas/pelicula_confirm_delete.html'
    success_url = reverse_lazy('listadoPeliculas')         #Cuando elimina redirige a la lista de películas
    




class DirectorNuevo(LoginRequiredMixin, CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'directores/director_edit.html'
    

    def get_success_url(self):
        return reverse('detallesDirector',args=(self.object.id,))


class DirectorEditar(LoginRequiredMixin, UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = 'directores/director_edit.html'
    

    def get_success_url(self):
        return reverse('detallesDirector',args=(self.object.id,))




class DirectorEliminar(LoginRequiredMixin,DeleteView):
    model = Director
    template_name = 'directores/director_confirm_delete.html'
    success_url = reverse_lazy('listadoDirectores')           #Cuando elimina redirige a la lista de directores




class ActorNuevo(LoginRequiredMixin,CreateView):
    model = Actor
    form_class = ActorForm
    template_name = 'actores/actor_edit.html'
    

    def get_success_url(self):
        return reverse('detallesActor',args=(self.object.id,))



class ActorEditar(LoginRequiredMixin,UpdateView):
    model = Actor
    form_class = ActorForm
    template_name = 'actores/actor_edit.html'

    def get_success_url(self):
        return reverse('detallesActor',args=(self.object.id,))
    



class ActorEliminar(LoginRequiredMixin,DeleteView):
    model = Actor
    template_name = 'actores/actor_confirm_delete.html'
    success_url = reverse_lazy('listadoActores')         #Cuando elimina redirige a la lista de películas


@login_required
def valoracion(request,pk):
    peli = get_object_or_404(Pelicula, pk=pk)

    if request.method =="POST":
        form = VotacionForm(request.POST,request.FILES, instance=peli)
        if form.is_valid():
            peli = form.save(commit=False)                     #Devuelve el objeto que todavia no está guardado en la base de datos
            peli.numVotos += 1
            numVotos = peli.numVotos
            peli.valoracionTotal += peli.valoracion
            total =  peli.valoracionTotal
            peli.valoracionMedia = total/numVotos
            peli.save()

            return redirect('detallesPelicula', pk=peli.pk)

    else:
        form = VotacionForm(instance = peli)
        return render(request, os.path.join("peliculas", "pelicula_vote.html"),{'form':form, 'peli':peli})






"""def registro_usuario(request):
    data = {
        'form':UserCreationForm()
    }


    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data('username')
            password = formulario.cleaned_data('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('listadoPeliculas')

    return render(request, 'registration/registrar.html',data) """