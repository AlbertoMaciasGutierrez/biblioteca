from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Pelicula, Director, Actor



class ActorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ("id","nombre", "pais", "fecha_nacimiento", "biografia")
        model = Actor

class DirectorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ("id","nombre", "pais", "fecha_nacimiento", "biografia")
        model = Director

class PeliculaSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.SlugRelatedField(slug_field="nombre", read_only=True)
    autores = serializers.SlugRelatedField(slug_field="nombre", read_only=True)

    class Meta:
        fields = ("id","titulo", "fecha_publicacion", "categoria", "duracion", "director", "sinopsis", "autores", "trailer")
        model = Pelicula





class ActoresView(generics.ListCreateAPIView):
 
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]


class ActorView(generics.RetrieveUpdateDestroyAPIView):
 
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]


class DirectoresView(generics.ListCreateAPIView):
 
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]


class DirectorView(generics.RetrieveUpdateDestroyAPIView):
 
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]


class PeliculasView(generics.ListCreateAPIView):
 
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticated]


class PeliculaView(generics.RetrieveUpdateDestroyAPIView):
 
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticated]



