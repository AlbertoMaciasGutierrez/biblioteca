import os
from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .models import Pelicula, Director
from .forms import PeliculaForm, DirectorForm   



@login_required
def listadoPeliculas(request):
    peliculasOrdenadas = Pelicula.objects.order_by('fecha_publicacion')[:5]            
    context = {"peliculasOrdenadas": peliculasOrdenadas}
    return render(request, os.path.join("peliculas", "peliculas_list.html"), context=context)

@login_required
def listadoDirectores(request):
    directoresOrdenadas = Director.objects.order_by('fecha_nacimiento')[:5]            
    context = {"directoresOrdenados": directoresOrdenadas}
    return render(request, os.path.join("directores", "director_list.html"), context=context)


class PeliculaDetalles(LoginRequiredMixin, DetailView):
    model = Pelicula
    template_name = 'peliculas/peliculas_detail.html'

   
class DirectorDetalles(LoginRequiredMixin ,DetailView):
    model = Director
    template_name = 'directores/director_detail.html'   

@login_required
def pelicula_nueva(request):
    if request.method == "POST":
        form = PeliculaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detallesPelicula', pk=post.pk)
    else:
        form = PeliculaForm()
    return render(request, os.path.join("peliculas", "peliculas_edit.html"), {'form':form})



@login_required
def pelicula_editar(request,pk):
    post = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        form = PeliculaForm(request.POST, instance=post)
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
    


@login_required
def director_nuevo(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detallesDirector',pk=post.pk)
    else:
        form = DirectorForm()
    return render(request, os.path.join("directores", "director_edit.html"), {'form':form})

@login_required
def director_editar(request,pk):
    post = get_object_or_404(Director, pk=pk)
    if request.method == "POST":
        form = DirectorForm(request.POST, instance=post)
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