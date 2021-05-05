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

urlpatterns = [
    path('peliculas/', views.listadoPeliculas, name ="listadoPeliculas"),                              #path('peliculas/', PeliculasView.as_view(), name="listado-peliculas"),
    path('peliculas/<int:pk>/', views.PeliculaDetalles.as_view(), name="detallesPelicula"),
    path('director/', views.listadoDirectores, name ="listadoDirectores"),
    path('director/<int:pk>/', views.DirectorDetalles.as_view(), name="detallesDirector"),
    path('admin/', admin.site.urls),
    path('peliculas/nueva',views.pelicula_nueva , name='pelicula_nueva'),
    path('peliculas/<int:pk>/editar/', views.pelicula_editar, name='pelicula_editar'),
    path('peliculas/<int:pk>/eliminar/',views.PeliculaEliminar.as_view(), name='pelicula_eliminar'),
    path('director/nuevo',views.director_nuevo , name='director_nuevo'),
    path('director/<int:pk>/editar/', views.director_editar, name='director_editar'),
    path('director/<int:pk>/eliminar/', views.DirectorEliminar.as_view(), name='director_eliminar'),
    #path('registro/',views.registro_usuario, name='registro_usuario'),
    path('accounts/', include('django.contrib.auth.urls')),                                      #Add Django site authentication urls (for login, logout, password management)
]
