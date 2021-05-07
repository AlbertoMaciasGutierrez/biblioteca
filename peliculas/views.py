import os
from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import DetailView, DeleteView, CreateView, ListView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from .models import Pelicula, Director, Actor
from .forms import PeliculaForm, DirectorForm, ActorForm   



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

   
class DirectorDetalles(LoginRequiredMixin ,DetailView):
    model = Director
    template_name = 'directores/director_detail.html'   

class ActorDetalles(LoginRequiredMixin ,DetailView):
    model = Actor
    template_name = 'actores/actor_detail.html' 



class PeliculaNueva(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'peliculas/peliculas_edit.html'
    

    def get_success_url(self):
        return reverse('detallesPelicula',args=(self.object.id,))




@login_required
def pelicula_editar(request,pk):
    post = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        form = PeliculaForm(request.POST, request.FILES, instance=post)           #"request.FILES" : Es necesario para que se guarde la imagen, para que se pueda subir
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detallesPelicula', pk=post.pk)
    else:
        form = PeliculaForm(instance=post)
    return render(request, os.path.join("peliculas", "peliculas_edit.html"), {'form':form})


class PeliculaEliminar(LoginRequiredMixin,DeleteView):
    model = Pelicula
    template_name = 'peliculas/pelicula_confirm_delete.html'
    success_url = reverse_lazy('listadoPeliculas')         #Cuando elimina redirige a la lista de películas
    




class DirectorNuevo(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'directores/director_edit.html'
    

    def get_success_url(self):
        return reverse('detallesDirector',args=(self.object.id,))


@login_required
def director_editar(request,pk):
    post = get_object_or_404(Director, pk=pk)
    if request.method == "POST":
        form = DirectorForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detallesDirector', pk=post.pk)
    else:
        form = DirectorForm(instance=post)
    return render(request, os.path.join("directores", "director_edit.html"), {'form':form})



class DirectorEliminar(LoginRequiredMixin,DeleteView):
    model = Director
    template_name = 'directores/director_confirm_delete.html'
    success_url = reverse_lazy('listadoDirectores')           #Cuando elimina redirige a la lista de directores




class ActorNuevo(CreateView):
    model = Actor
    form_class = ActorForm
    template_name = 'actores/actor_edit.html'
    

    def get_success_url(self):
        return reverse('detallesActor',args=(self.object.id,))



@login_required
def actor_editar(request,pk):
    post = get_object_or_404(Actor, pk=pk)
    if request.method == "POST":
        form = ActorForm(request.POST, request.FILES, instance=post)           #"request.FILES" : Es necesario para que se guarde la imagen, para que se pueda subir
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detallesActor', pk=post.pk)
    else:
        form = ActorForm(instance=post)
    return render(request, os.path.join("actores", "actor_edit.html"), {'form':form})


class ActorEliminar(LoginRequiredMixin,DeleteView):
    model = Actor
    template_name = 'actores/actor_confirm_delete.html'
    success_url = reverse_lazy('listadoActores')         #Cuando elimina redirige a la lista de películas













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