from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Pelicula, Director, Actor



class ActorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ("id", "nombre", "pais", "fecha_nacimiento", "biografia")
        model = Actor


class DirectorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ("id", "nombre", "pais", "fecha_nacimiento", "biografia")
        model = Director


class PeliculaSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.SlugRelatedField(queryset=Director.objects.all(), slug_field='nombre')
    actores = serializers.SlugRelatedField(queryset=Actor.objects.all(), slug_field='nombre', many=True )
    imagen = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    valoracionMedia = serializers.CharField(read_only=True)
    numVotos = serializers.CharField(read_only=True)
    duracion = serializers.CharField()


    class Meta:
        fields = ("id", "titulo", "fecha_publicacion", "categoria", "duracion", "director", "sinopsis", "actores", "imagen", "trailer", "valoracionMedia", "numVotos")
        model = Pelicula


class ValoracionSerializer(serializers.HyperlinkedModelSerializer):
    valoracion= serializers.ChoiceField(choices= Pelicula.VALORACION_CHOICES)


    class Meta:
        fields = ("id", "valoracion")
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



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def valoracion(request,pk):
    try:
        peli = Pelicula.objects.get(pk=pk)
    except Pelicula.DoesNotExist:
        return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    

    if request.method =="PUT":
        
        serializer = ValoracionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            peli.valoracion = serializer.validated_data["valoracion"]                   
            if peli.numVotos == 0:
                peli.voto_usuario = str(request.user)
                print(peli.voto_usuario)
                peli.numVotos += 1
                numVotos = peli.numVotos
                peli.valoracionTotal += peli.valoracion
                total =  peli.valoracionTotal
                peli.valoracionMedia = total/numVotos
                peli.save()

                response_serializer = ValoracionSerializer(peli)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
                
            else:
                usuariosVoto = peli.voto_usuario.split(sep='|')
                haVotado = False
                nombreUsuario= str(request.user)

                for v in usuariosVoto:
                    if nombreUsuario == v:
                        haVotado = True

                if haVotado:
                    print("El usario ",v, " ya ha votado.")
                    return Response({"detail": "El usuario ya ha votado"}, status=status.HTTP_304_NOT_MODIFIED)

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

                    response_serializer = ValoracionSerializer(peli)
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
    
            

            

    
