import os
from django.contrib import messages
from django.db.models.query import QuerySet
from django.http import request,HttpRequest, Http404
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden
from cuentas.models import Usuario
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import DetailView, DeleteView, CreateView, ListView, UpdateView, View 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from .models import Pelicula, Director, Actor
from .forms import PeliculaForm, DirectorForm, ActorForm, VotacionForm, RegistroForm
 



class PeliculaListado(LoginRequiredMixin, ListView):             #Para ListView el nombre genérico para tener "objects.all()" es: "nombreModeloEnMinusculas"_list
    model = Pelicula                                             #Estos nombres se usan en los bucles for de los distintos templates de cada lista de objects
    template_name = 'peliculas/peliculas_list.html'              #En este caso se llama "pelicula_list"
    raise_exception = True

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        # PARTE DEL CÓDIGO PARA QUE FUNCIONE EL BUSCADOR 
        #----------------------------------------------#
        queryset = request.GET.get("Buscar")
        pelicula = str(queryset).strip()
        
        if queryset:
            peliculaEncontrada = False
            for obj in self.object_list:
                cadena = str(obj)
                elementos = cadena.split(sep='-')
                tituloPeli = elementos[0].strip()
                
                if tituloPeli == pelicula:
                    peliculaEncontrada = True
                    break
            
            if not peliculaEncontrada:
                self.object_list = QuerySet
            else:
                self.object_list = Pelicula.objects.filter(titulo = tituloPeli)
        #----------------------------------------------#
    

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)


    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(PeliculaListado, self).get_context_data(**kwargs)
        context['boton_activado'] = True                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context

    
    

class DirectorListado(LoginRequiredMixin, ListView):
    model = Director
    template_name = 'directores/director_list.html'
    raise_exception = True

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        # PARTE DEL CÓDIGO PARA QUE FUNCIONE EL BUSCADOR 
        #----------------------------------------------#
        queryset = request.GET.get("Buscar")
        director = str(queryset).strip()
        
        if queryset:
            directorEncontrado = False
            for obj in self.object_list:
                cadena = str(obj)
                elementos = cadena.split(sep='-')
                nombreDirector = elementos[0].strip()
                
                if nombreDirector == director:
                    directorEncontrado = True
                    break
            
            if not directorEncontrado:
                self.object_list = QuerySet
            else:
                self.object_list = Director.objects.filter(nombre = nombreDirector)
        #----------------------------------------------#
    

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)


    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(DirectorListado, self).get_context_data(**kwargs)
        context['boton_activado'] = True                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context



class ActorListado(LoginRequiredMixin, ListView):
    model = Actor
    template_name = 'actores/actor_list.html'
    raise_exception = True

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        # PARTE DEL CÓDIGO PARA QUE FUNCIONE EL BUSCADOR 
        #----------------------------------------------#
        queryset = request.GET.get("Buscar")
        actor = str(queryset).strip()
        
        if queryset:
            actorEncontrado = False
            for obj in self.object_list:
                cadena = str(obj)
                elementos = cadena.split(sep='-')
                nombreActor = elementos[0].strip()
                
                if nombreActor == actor:
                    actorEncontrado = True
                    break
            
            if not actorEncontrado:
                self.object_list = QuerySet
            else:
                self.object_list = Actor.objects.filter(nombre = nombreActor)
        #----------------------------------------------#
    

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(ActorListado, self).get_context_data(**kwargs)
        context['boton_activado'] = True                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context



class PeliculaDetalles(LoginRequiredMixin, DetailView):
    model = Pelicula
    template_name = 'peliculas/peliculas_detail.html'
    raise_exception = True

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(PeliculaDetalles, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context


   
class DirectorDetalles(LoginRequiredMixin, DetailView):
    model = Director
    template_name = 'directores/director_detail.html'   
    raise_exception = True

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(DirectorDetalles, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context

class ActorDetalles(LoginRequiredMixin, DetailView):
    model = Actor
    template_name = 'actores/actor_detail.html' 
    raise_exception = True

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(ActorDetalles, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context



class PeliculaNueva(LoginRequiredMixin, CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'peliculas/peliculas_new.html'
    raise_exception = True    

    def get_success_url(self):
        return reverse('detallesPelicula',args=(self.object.id,))

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(PeliculaNueva, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context



class PeliculaEditar(LoginRequiredMixin, UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'peliculas/peliculas_edit.html'
    raise_exception = True    

    def get_success_url(self):
        return reverse('detallesPelicula',args=(self.object.id,))

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(PeliculaEditar, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context





class PeliculaEliminar(LoginRequiredMixin, DeleteView):
    model = Pelicula
    template_name = 'peliculas/pelicula_confirm_delete.html'
    success_url = reverse_lazy('listadoPeliculas')         #Cuando elimina redirige a la lista de películas
    raise_exception = True  

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(PeliculaEliminar, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context
    

 




class DirectorNuevo(LoginRequiredMixin, CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'directores/director_new.html'
    raise_exception = True   

    def get_success_url(self):
        return reverse('detallesDirector',args=(self.object.id,))

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(DirectorNuevo, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context


class DirectorEditar(LoginRequiredMixin, UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = 'directores/director_edit.html'
    raise_exception = True    

    def get_success_url(self):
        return reverse('detallesDirector',args=(self.object.id,))

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(DirectorEditar, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context




class DirectorEliminar(LoginRequiredMixin,DeleteView):
    model = Director
    template_name = 'directores/director_confirm_delete.html'
    success_url = reverse_lazy('listadoDirectores')           #Cuando elimina redirige a la lista de directores
    raise_exception = True

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(DirectorEliminar, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context


class ActorNuevo(LoginRequiredMixin,CreateView):
    model = Actor
    form_class = ActorForm
    template_name = 'actores/actor_new.html'
    raise_exception = True

    def get_success_url(self):
        return reverse('detallesActor',args=(self.object.id,))

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(ActorNuevo, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context


class ActorEditar(LoginRequiredMixin,UpdateView):
    model = Actor
    form_class = ActorForm
    template_name = 'actores/actor_edit.html'
    raise_exception = True

    def get_success_url(self):
        return reverse('detallesActor',args=(self.object.id,))
    
   #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(ActorEditar, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context
    



class ActorEliminar(LoginRequiredMixin,DeleteView):
    model = Actor
    template_name = 'actores/actor_confirm_delete.html'
    success_url = reverse_lazy('listadoActores')         #Cuando elimina redirige a la lista de películas
    raise_exception = True

   #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(ActorEliminar, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context


@login_required
def valoracion(request,pk):
    peli = get_object_or_404(Pelicula, pk=pk)
    boton_activado = False

    if request.method =="POST":
        
        form = VotacionForm(request.POST,request.FILES, instance=peli)
        if form.is_valid():

            peli = form.save(commit=False)                     #Devuelve el objeto que todavia no está guardado en la base de datos
            if peli.numVotos == 0:
                peli.voto_usuario = str(request.user)
                print(peli.voto_usuario)
                peli.numVotos += 1
                numVotos = peli.numVotos
                peli.valoracionTotal += peli.valoracion
                total =  peli.valoracionTotal
                peli.valoracionMedia = total/numVotos
                peli.save()
                
            else:
                usuariosVoto = peli.voto_usuario.split(sep='|')
                haVotado = False
                nombreUsuario= str(request.user)

                for v in usuariosVoto:
                    if nombreUsuario == v:
                        haVotado = True

                if haVotado:
                    print("El usario ",v, " ya ha votado.")
                    return render(request, os.path.join("peliculas", "usuario_ha_votado.html"),{'peli':peli, 'boton_activado':boton_activado})

                else:

                    nombre = "|"
                    nombre += nombreUsuario
                    peli.voto_usuario += nombre
                    print(peli.voto_usuario)
                    peli.numVotos += 1
                    numVotos = peli.numVotos
                    peli.valoracionTotal += peli.valoracion
                    total =  peli.valoracionTotal
                    peli.valoracionMedia = total/numVotos
                    peli.save()
    
            

            return redirect('detallesPelicula', pk=peli.pk)

    else:
        form = VotacionForm(instance = peli)
        return render(request, os.path.join("peliculas", "pelicula_vote.html"),{'form':form, 'peli':peli, 'boton_activado':boton_activado})



class RegistroUsuario(CreateView):
    model = Usuario
    template_name = 'registration/registrar.html'
    form_class = RegistroForm
    

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
       # messages.success(request, "Registro completado correctamente")
        return redirect('listadoPeliculas')

    #Pasamos una nueva variable al Template base.html
    def get_context_data(self, **kwargs):
        context = super(RegistroUsuario, self).get_context_data(**kwargs)
        context['boton_activado'] = False                                      #Si boton_activado es verdadero el botón del buscador funciona, si es falso no
        return context    



def error_404(request, exception=None):
    return HttpResponseNotFound(render(request, os.path.join("errores", "404.html")))
    
def error_500(request): 
    return HttpResponseServerError(render(request, os.path.join("errores", "500.html")))

def error_403(request, exception=None):
    return HttpResponseForbidden(render(request, os.path.join("errores", "403.html")))

def error_400(request, exception=None):
    return HttpResponseBadRequest(render(request, os.path.join("errores", "400.html")))



