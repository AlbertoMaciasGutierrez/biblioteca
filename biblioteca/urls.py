"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from peliculas import views
from peliculas.api import ActoresView, ActorView, DirectorView, DirectoresView, PeliculaView, PeliculasView, valoracion
from django.conf.urls import handler404, handler500, handler403, handler400

handler404 = 'peliculas.views.error_404'
handler500 = 'peliculas.views.error_500'
handler403 = 'peliculas.views.error_403'
handler400 = 'peliculas.views.error_400'


urlpatterns = [
    path('peliculas/<int:pk>/', views.PeliculaDetalles.as_view(), name="detallesPelicula"),
    path('peliculas/', views.PeliculaListado.as_view(), name="listadoPeliculas"),
    path('director/', views.DirectorListado.as_view(), name ="listadoDirectores"),
    path('director/<int:pk>/', views.DirectorDetalles.as_view(), name="detallesDirector"),
    path('actores/', views.ActorListado.as_view(), name ="listadoActores"), 
    path('actores/<int:pk>/', views.ActorDetalles.as_view(), name="detallesActor"),
    path('admin/', admin.site.urls),
    path('peliculas/nueva',views.PeliculaNueva.as_view() , name='pelicula_nueva'),
    path('peliculas/<int:pk>/editar/', views.PeliculaEditar.as_view(), name='pelicula_editar'),
    path('peliculas/<int:pk>/eliminar/',views.PeliculaEliminar.as_view(), name='pelicula_eliminar'),
    path('peliculas/<int:pk>/valorar/', views.valoracion , name='votacionPelicula'),
    path('director/nuevo',views.DirectorNuevo.as_view() , name='director_nuevo'),
    path('director/<int:pk>/editar/', views.DirectorEditar.as_view(), name='director_editar'),
    path('director/<int:pk>/eliminar/', views.DirectorEliminar.as_view(), name='director_eliminar'),
    path('actores/nuevo',views.ActorNuevo.as_view() , name='actor_nuevo'),                                    
    path('actores/<int:pk>/editar/', views.ActorEditar.as_view(), name='actor_editar'),                       
    path('actores/<int:pk>/eliminar/', views.ActorEliminar.as_view(), name='actor_eliminar'),        
    path('registro/',views.RegistroUsuario.as_view(), name='registro_usuario'),
    path('accounts/', include('django.contrib.auth.urls')),                                      #Add Django site authentication urls (for login, logout, password management)
    #Api Django Rest Framework
    path('api/', include("rest_framework.urls", namespace="rest_framework")),                    
    path('api/actores/', ActoresView.as_view(), name="apiView_listadoActores"),
    path('api/actores/<int:pk>/', ActorView.as_view(), name="apiView_detallesActor"),
    path('api/directores/', DirectoresView.as_view(), name ="apiView_listadoDirectores"),
    path('api/directores/<int:pk>/', DirectorView.as_view(), name="apiView_detallesDirector"),
    path('api/peliculas/', PeliculasView.as_view(), name="apiView_listadoPeliculas"),
    path('api/peliculas/<int:pk>/', PeliculaView.as_view(), name="apiView_detallesPelicula"),
    path('api/peliculas/<int:pk>/valorar/', valoracion , name='apiView_votacionPelicula'),

    
    
]

