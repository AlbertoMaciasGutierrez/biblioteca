from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Pelicula, Director, Actor
from drf_extra_fields.fields import Base64ImageField






class ImagenSerializer(serializers.Serializer):
    imagen = Base64ImageField(required=False)
    created = serializers.DateTimeField()



class ActorSerializer(serializers.HyperlinkedModelSerializer):
    imagen = serializers.ImageField(required=False, max_length=None, allow_empty_file=True, use_url=False)


    class Meta:
        fields = ("id", "nombre", "pais", "fecha_nacimiento", "imagen", "biografia")
        model = Actor


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    imagen = serializers.ImageField(required=False, max_length=None, allow_empty_file=True, use_url=False)


    class Meta:
        fields = ("id", "nombre", "pais", "fecha_nacimiento", "imagen", "biografia")
        model = Director


class PeliculaSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.SlugRelatedField(queryset=Director.objects.all(), slug_field='nombre')
    actores = serializers.SlugRelatedField(queryset=Actor.objects.all(), slug_field='nombre', many=True )
    imagen = serializers.ImageField(required=False, max_length=None, allow_empty_file=True, use_url=False)
    #imagen = Base64ImageField(required=False, max_length=None, use_url=True)
    valoracionMedia = serializers.CharField(read_only=True)
    numVotos = serializers.CharField(read_only=True)
    duracion = serializers.CharField()


    class Meta:
        fields = ("id", "titulo", "fecha_publicacion", "pais", "categoria", "duracion", "director", "sinopsis", "actores", "imagen", "trailer", "valoracionMedia", "numVotos")
        model = Pelicula



class ValoracionSerializer(serializers.HyperlinkedModelSerializer):
    valoracion= serializers.ChoiceField(choices= Pelicula.VALORACION_CHOICES, write_only=True)
    valoracionMedia = serializers.CharField(read_only=True)
    numVotos = serializers.CharField(read_only=True)
    titulo = serializers.CharField(read_only=True)


    class Meta:
        fields = ("id", "titulo", "valoracionMedia", "numVotos", "valoracion")
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






@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def valoracion(request,pk):
    try:
        peli = Pelicula.objects.get(pk=pk)
    except Pelicula.DoesNotExist:
        return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    

    if request.method =="GET":
        serializer = ValoracionSerializer(peli)
        return Response(serializer.data)


    if request.method =="PUT":
        
        serializer = ValoracionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            peli.valoracion = serializer.validated_data["valoracion"]                   
            if peli.numVotos == 0:
                peli.voto_usuario = str(request.user)
                peli.numVotos += 1
                numVotos = peli.numVotos
                peli.valoracionTotal = float(peli.valoracionTotal) + float(peli.valoracion)
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
                    return Response({"detail": "El usuario " + v + " ya ha votado" }, status=status.HTTP_400_BAD_REQUEST)

                else:

                    nombre = "|"
                    nombre += nombreUsuario
                    peli.voto_usuario += nombre
                    peli.numVotos += 1
                    numVotos = peli.numVotos
                    peli.valoracionTotal = float(peli.valoracionTotal) + float(peli.valoracion)
                    total =  peli.valoracionTotal
                    peli.valoracionMedia = total/numVotos
                    peli.save()

                    response_serializer = ValoracionSerializer(peli)
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
    
            

            

    
